import sys
import subprocess
import importlib.resources

import PySide6 as ref_mod


__all__ = ["qt_tool_wrapper", "rcc"]


def qt_tool_wrapper(qt_tool: str, args: list[str], libexec: bool = False):
    # Taking care of pyside6-uic, pyside6-rcc, and pyside6-designer
    # listed as an entrypoint in setup.py
    pyside_dir = importlib.resources.files(ref_mod)
    if libexec and sys.platform != "win32":
        exe = pyside_dir / "Qt" / "libexec" / qt_tool
    else:
        exe = pyside_dir / qt_tool

    cmd = [str(exe)] + args
    returncode = subprocess.call(cmd)
    if returncode != 0:
        command = " ".join(cmd)
        print(f"'{command}' returned {returncode}", file=sys.stderr)


def rcc(args: list[str]):
    if "--binary" not in args:
        args.extend(["-g", "python"])
    qt_tool_wrapper("rcc", args, True)
