# pyright: reportMissingTypeArgument=none, reportUnknownArgumentType=none, reportUnknownVariableType=none

import logging
import os
import sys
import threading
from pathlib import Path
from PySide6.QtCore import (
    qInstallMessageHandler,
    QtMsgType,
    QDateTime,
    QSysInfo,
)

_logging: logging.Logger
_fileHandler: logging.FileHandler | None = None
_formatFileHandler: logging.FileHandler | None = None
_stdoutHandler: logging.StreamHandler
_formatStdoutHandler: logging.StreamHandler


class _CustomFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord):
        record.threadId = threading.get_ident()
        return super().format(record)


# noinspection PyPep8Naming
def _getLevelByMsgType(msgType: QtMsgType):
    if msgType == QtMsgType.QtFatalMsg:
        return logging.FATAL
    if msgType == QtMsgType.QtCriticalMsg:
        return logging.CRITICAL
    if msgType == QtMsgType.QtWarningMsg:
        return logging.WARNING
    if msgType == QtMsgType.QtInfoMsg:
        return logging.INFO
    if msgType == QtMsgType.QtDebugMsg:
        return logging.DEBUG
    return logging.DEBUG


# noinspection PyPep8Naming
def _openFormat():
    _logging.removeHandler(_stdoutHandler)
    _logging.addHandler(_formatStdoutHandler)
    if _fileHandler is not None and _formatFileHandler is not None:
        _logging.removeHandler(_fileHandler)
        _logging.addHandler(_formatFileHandler)


# noinspection PyPep8Naming
def _closeFormat():
    _logging.removeHandler(_formatStdoutHandler)
    _logging.addHandler(_stdoutHandler)
    if _fileHandler is not None and _formatFileHandler is not None:
        _logging.removeHandler(_formatFileHandler)
        _logging.addHandler(_fileHandler)


# noinspection PyPep8Naming
def _messageHandler(msgType: QtMsgType, context: ..., message: str):
    global _logging
    global _fileHandler
    global _formatFileHandler
    global _stdoutHandler
    global _formatStdoutHandler
    _closeFormat()
    fileAndLineLogStr = ""
    if context.file:
        strFileTmp = context.file
        ptr = strFileTmp.rfind("/")
        if ptr != -1:
            strFileTmp = strFileTmp[ptr + 1 :]
        ptrTmp = strFileTmp.rfind("\\")
        if ptrTmp != -1:
            strFileTmp = strFileTmp[ptrTmp + 1 :]
        fileAndLineLogStr = f"[{strFileTmp}:{str(context.line)}]"
    level = _getLevelByMsgType(msgType)
    finalMessage = f"{QDateTime.currentDateTime().toString('yyyy/MM/dd hh:mm:ss.zzz')}[{logging.getLevelName(level)}]{fileAndLineLogStr}[{threading.get_ident()}]:{message}"
    _logging.log(level, finalMessage)
    _openFormat()


# noinspection PyPep8Naming
def LogSetup(name: str, level: int = logging.DEBUG, log_path: str | Path | None = None):
    global _logging
    global _fileHandler
    global _formatFileHandler
    global _stdoutHandler
    global _formatStdoutHandler

    _logging = logging.getLogger(name)
    _logging.setLevel(level)
    _stdoutHandler = logging.StreamHandler(sys.stdout)
    _formatStdoutHandler = logging.StreamHandler(sys.stdout)
    fmt = _CustomFormatter(
        "%(asctime)s[%(levelname)s][%(filename)s:%(lineno)s][%(threadId)d] %(message)s"
    )
    _formatStdoutHandler.setFormatter(fmt)
    _logging.addHandler(_formatStdoutHandler)

    if log_path is not None:
        log_path = Path(log_path)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        _fileHandler = logging.FileHandler(log_path.as_posix())
        _formatFileHandler = logging.FileHandler(log_path.as_posix())
        _formatFileHandler.setFormatter(fmt)
        _logging.addHandler(_formatFileHandler)

    qInstallMessageHandler(_messageHandler)
    _logging.info("===================================================")
    _logging.info(f"[AppName] {name}")
    _logging.info(f"[AppPath] {sys.argv[0]}")
    _logging.info(f"[ProcessId] {os.getpid()}")
    _logging.info("[DeviceInfo]")
    _logging.info(f"  [DeviceId] {QSysInfo.machineUniqueId().toStdString()}")
    _logging.info(f"  [Manufacturer] {QSysInfo.productVersion()}")
    _logging.info(f"  [CPU_ABI] {QSysInfo.currentCpuArchitecture()}")
    _logging.info(f"[LOG_LEVEL] {logging.getLevelName(level)}")
    _logging.info(f"[LOG_PATH] {log_path}") if log_path is not None else None
    _logging.info("===================================================")


# noinspection PyPep8Naming
def Logger():
    return _logging
