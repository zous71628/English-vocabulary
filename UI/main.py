import sys
from keepaccount import Ui_MainWindow
from Record import Ui_RecordWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.Qt import QStandardItem, QStandardItemModel


class RecordWindow(QtWidgets.QMainWindow, Ui_RecordWindow):
    def __init__(self, parent=None):
        super(RecordWindow, self).__init__(parent)
        self.setupUi(self)
        # click confirm and cancel btn
        self.pushButton.clicked.connect(self.record_confirm_button_clicked)
        self.pushButton_2.clicked.connect(self.record_cancel_button_clicked)

        # set effect sound
        self.sound_effect = QSoundEffect(self)
        self.sound_effect.setSource(QUrl.fromLocalFile(r"C:\Windows\Media\Windows Background.wav"))
        self.sound_effect.setVolume(1.0)

        # set treeView
        treeviewmodel = QStandardItemModel()
        self.parentitem = treeviewmodel.invisibleRootItem()
        self.rootitem1 = QStandardItem("食")
        self.childitem1 = QStandardItem("早餐")
        self.childitem2 = QStandardItem("午餐")
        self.childitem3 = QStandardItem("晚餐")
        self.rootitem2 = QStandardItem("衣")
        self.childitem4 = QStandardItem("治裝")
        self.childitem5 = QStandardItem("首飾")
        self.rootitem3 = QStandardItem("住")
        self.childitem6 = QStandardItem("房租")
        self.childitem7 = QStandardItem("房貸")
        self.childitem8 = QStandardItem("水費")
        self.childitem9 = QStandardItem("電費")
        self.childitem10 = QStandardItem("油費")
        self.rootitem4 = QStandardItem("行")
        self.childitem11 = QStandardItem("捷運")
        self.childitem12 = QStandardItem("公車")
        self.rootitem5 = QStandardItem("樂")
        self.childitem13 = QStandardItem("娛樂")
        self.rootitem6 = QStandardItem("其他")
        self.childitem14 = QStandardItem("醫療")

        self.listrootitem = [self.rootitem1, self.rootitem2, self.rootitem3,
                             self.rootitem4, self.rootitem5, self.rootitem6]
        self.listchilditem = [self.childitem1, self.childitem2, self.childitem3,
                              self.childitem4, self.childitem5, self.childitem6,
                              self.childitem7, self.childitem8, self.childitem9,
                              self.childitem10, self.childitem11, self.childitem12,
                              self.childitem13, self.childitem14]
        for i in range(6):
            self.parentitem.appendRow(self.listrootitem[i])
        for i in range(3):
            self.rootitem1.appendRow(self.listchilditem[i])
        for i in range(3, 5):
            self.rootitem2.appendRow(self.listchilditem[i])
        for i in range(5, 9):
            self.rootitem3.appendRow(self.listchilditem[i])
        for i in range(9, 12):
            self.rootitem4.appendRow(self.listchilditem[i])
        for i in range(12, 13):
            self.rootitem5.appendRow(self.listchilditem[i])
        for i in range(13, 14):
            self.rootitem6.appendRow(self.listchilditem[i])
        self.treeView.setHeaderHidden(True)
        self.treeView.setModel(treeviewmodel)

        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.show_contextmenu)
        self.treeView.doubleClicked.connect(self.double_clicked)

        # set datetime edit
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

    # set confirm btn and cancel btn def
    def record_confirm_button_clicked(self):
        self.lineEdit.text()
        self.close()

    def record_cancel_button_clicked(self):
        self.close()

    # set mouse rightbutton click
    def show_contextmenu(self, pos):
        self.cursorpos = QtGui.QCursor.pos()
        self.treeView.contextMenu = QMenu(self)
        self.indexat = self.treeView.indexAt(pos)

        if self.indexat.isValid() == False:
            self.action = self.treeView.contextMenu.addAction("新增主分類")
            self.treeView.contextMenu.exec_(self.cursorpos)

        if self.indexat.isValid():
            self.action = self.treeView.contextMenu.addAction("新增次分類")
            self.action = self.treeView.contextMenu.addAction("刪除次分類")
            self.action = self.treeView.contextMenu.addAction("刪除主分類")
            self.treeView.contextMenu.exec_(self.cursorpos)

        self.tvcurrentindex = self.treeView.currentIndex()
        indexsibling = self.tvcurrentindex.sibling(self.tvcurrentindex.row(), 0)
        if indexsibling.isValid():
            print("1")

    def double_clicked(self):
        if  self.indexat.isValid():
            self.label_6.setText("1")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.record_window = RecordWindow()
        self.pushButton.clicked.connect(self.new_record_button_clicked)

    def new_record_button_clicked(self):
        self.record_window.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
