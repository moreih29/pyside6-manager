# pyright: basic, reportRedeclaration=none


from PySide6.QtCore import (
    Signal,
    Property,
    QSortFilterProxyModel,
    Slot,
    QMetaObject,
    Q_RETURN_ARG,
    Q_ARG,
    Qt,
    QAbstractItemModel,
)
from PySide6.QtQml import QJSValue


# noinspection PyCallingNonCallable,PyPep8Naming,PyShadowingBuiltins
class FluTableSortProxyModel(QSortFilterProxyModel):
    modelChanged = Signal()

    # noinspection PyTypeChecker
    @Property(QAbstractItemModel, notify=modelChanged)
    def model(self):
        return self._model

    @model.setter
    def model(self, value: QAbstractItemModel):
        self._model = value
        self.modelChanged.emit()

    def __init__(self):
        QSortFilterProxyModel.__init__(self)
        self._model = None
        self._filter = None
        self._comparator = None
        self.modelChanged.connect(lambda: self.setSourceModel(self._model))  # pyright: ignore[reportArgumentType]

    # noinspection PyTypeChecker
    @Slot(int, result=dict)
    def getRow(self, rowIndex: int):
        if self._model is None:
            return {}
        return QMetaObject.invokeMethod(
            self._model,
            "getRow",
            Q_RETURN_ARG("QVariantMap"),
            Q_ARG(int, self.mapToSource(self.index(rowIndex, 0)).row()),
        )

    # noinspection PyTypeChecker
    @Slot(int, dict)
    def setRow(self, rowIndex: int, val: dict):
        if self._model is None:
            return
        QMetaObject.invokeMethod(
            self._model,
            "setRow",
            Q_ARG(int, self.mapToSource(self.index(rowIndex, 0)).row()),
            Q_ARG("QVariantMap", val),
        )

    @Slot(int, int)
    def removeRow(self, rowIndex: int, rows: int):
        if self._model is None:
            return
        QMetaObject.invokeMethod(
            self._model,
            "removeRow",
            Q_ARG(int, self.mapToSource(self.index(rowIndex, 0)).row()),
            Q_ARG(int, rows),
        )

    @Slot(QJSValue)
    def setComparator(self, comparator: QJSValue):
        if self._model is None:
            return
        column = 0
        if comparator.isUndefined():
            column = -1
        self._comparator = comparator
        if self.sortOrder() == Qt.SortOrder.AscendingOrder:
            self.sort(column, Qt.SortOrder.DescendingOrder)
        else:
            self.sort(column, Qt.SortOrder.AscendingOrder)

    @Slot(QJSValue)
    def setFilter(self, filter: QJSValue):
        self._filter = filter
        self.invalidateFilter()

    def filterAcceptsColumn(self, source_column: ..., source_parent: ...):
        return True

    def filterAcceptsRow(self, source_row: ..., source_parent: ...):
        if self._filter is None or self._filter.isUndefined():
            return True
        data: list[int] = [source_row]
        return self._filter.call(data).toBool()

    def lessThan(self, source_left, source_right):
        if self._comparator is None or self._comparator.isUndefined():
            return True
        data: list[int] = [source_left.row(), source_right.row()]
        flag = self._comparator.call(data).toBool()
        if self.sortOrder() == Qt.SortOrder.AscendingOrder:
            return not flag
        else:
            return flag
