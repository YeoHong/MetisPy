from PySide2 import QtWidgets, QtCore


class EscapableQListWidget(QtWidgets.QListWidget):
    def keyPressEvent(self, event):
        super(EscapableQListWidget, self).keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_Escape:
            self.clearSelection()


class UniqueLabelQListWidget(EscapableQListWidget):
    def mousePressEvent(self, event):
        super(UniqueLabelQListWidget, self).mousePressEvent(event)
        if not self.indexAt(event.pos()).isValid():
            self.clearSelection()

    def findItemsByLabel(self, label):
        items = []
        for row in range(self.count()):
            item = self.item(row)
            if item.data(QtCore.Qt.UserRole) == label:
                items.append(item)
        return items

    def createItemFromLabel(self, label):
        item = QtWidgets.QListWidgetItem()
        item.setData(QtCore.Qt.UserRole, label)
        return item

    def setItemLabel(self, item, label, color=None):
        qlabel = QtWidgets.QLabel()
        if color is None:
            qlabel.setText("{}".format(label))
        else:
            qlabel.setText(
                '{} <font color="#{:02x}{:02x}{:02x}">●</font>'.format(
                    label, *color
                )
            )
        qlabel.setAlignment(QtCore.Qt.AlignBottom)

        item.setSizeHint(qlabel.sizeHint())

        self.setItemWidget(item, qlabel)
