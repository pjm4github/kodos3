# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\PJM\PycharmProjects\kodos\modules\helpBA_.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelpBA(object):
    def setupUi(self, HelpBA):
        HelpBA.setObjectName("HelpBA")
        HelpBA.resize(494, 585)
        self.verticalLayout = QtWidgets.QVBoxLayout(HelpBA)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menubar = QtWidgets.QMenuBar(HelpBA)
        self.menubar.setObjectName("menubar")
        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.setObjectName("fileMenu")
        self.verticalLayout.addWidget(self.menubar)
        self.fileHomeAction = QtWidgets.QAction(HelpBA)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image0"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileHomeAction.setIcon(icon)
        self.fileHomeAction.setProperty("name", "fileHomeAction")
        self.fileHomeAction.setObjectName("fileHomeAction")
        self.fileBackAction = QtWidgets.QAction(HelpBA)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../image1"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileBackAction.setIcon(icon1)
        self.fileBackAction.setProperty("name", "fileBackAction")
        self.fileBackAction.setObjectName("fileBackAction")
        self.fileForwardAction = QtWidgets.QAction(HelpBA)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../image2"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileForwardAction.setIcon(icon2)
        self.fileForwardAction.setProperty("name", "fileForwardAction")
        self.fileForwardAction.setObjectName("fileForwardAction")
        self.fileExitAction = QtWidgets.QAction(HelpBA)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../image3"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileExitAction.setIcon(icon3)
        self.fileExitAction.setProperty("name", "fileExitAction")
        self.fileExitAction.setObjectName("fileExitAction")
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileHomeAction)
        self.fileMenu.addAction(self.fileBackAction)
        self.fileMenu.addAction(self.fileForwardAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileExitAction)
        self.menubar.addAction(self.fileMenu.menuAction())

        self.retranslateUi(HelpBA)
        self.fileExitAction.activated.connect(HelpBA.exitSlot)
        self.fileBackAction.activated.connect(HelpBA.backSlot)
        self.fileForwardAction.activated.connect(HelpBA.forwardSlot)
        self.fileHomeAction.activated.connect(HelpBA.homeSlot)
        QtCore.QMetaObject.connectSlotsByName(HelpBA)

    def retranslateUi(self, HelpBA):
        _translate = QtCore.QCoreApplication.translate
        HelpBA.setWindowTitle(_translate("HelpBA", "MainWindow"))
        self.fileMenu.setTitle(_translate("HelpBA", "&File"))
        self.fileHomeAction.setText(_translate("HelpBA", "Home"))
        self.fileHomeAction.setIconText(_translate("HelpBA", "Home"))
        self.fileHomeAction.setShortcut(_translate("HelpBA", "Ctrl+H"))
        self.fileBackAction.setText(_translate("HelpBA", "Back"))
        self.fileBackAction.setIconText(_translate("HelpBA", "Back"))
        self.fileBackAction.setShortcut(_translate("HelpBA", "Ctrl+B"))
        self.fileForwardAction.setText(_translate("HelpBA", "Forward"))
        self.fileForwardAction.setIconText(_translate("HelpBA", "Forward"))
        self.fileForwardAction.setShortcut(_translate("HelpBA", "Ctrl+F"))
        self.fileExitAction.setText(_translate("HelpBA", "Exit"))
        self.fileExitAction.setIconText(_translate("HelpBA", "Exit"))
        self.fileExitAction.setShortcut(_translate("HelpBA", "Ctrl+Q"))

from q3mainwindow import Q3MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelpBA = QtWidgets.Q3MainWindow()
    ui = Ui_HelpBA()
    ui.setupUi(HelpBA)
    HelpBA.show()
    sys.exit(app.exec_())

