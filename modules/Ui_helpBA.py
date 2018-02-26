# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\PJM\PycharmProjects\kodos\modules\helpBA.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 608)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.toolBar = QtWidgets.QWidget(self.centralwidget)
        self.toolBar.setObjectName("toolBar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.toolBar)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(502, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addWidget(self.toolBar, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 541, 21))
        self.menubar.setObjectName("menubar")
        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.setObjectName("fileMenu")
        self.fileHomeAction = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image0"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileHomeAction.setIcon(icon)
        self.fileHomeAction.setProperty("name", "fileHomeAction")
        self.fileHomeAction.setObjectName("fileHomeAction")
        self.fileBackAction = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../image1"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileBackAction.setIcon(icon1)
        self.fileBackAction.setProperty("name", "fileBackAction")
        self.fileBackAction.setObjectName("fileBackAction")
        self.fileForwardAction = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../image2"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileForwardAction.setIcon(icon2)
        self.fileForwardAction.setProperty("name", "fileForwardAction")
        self.fileForwardAction.setObjectName("fileForwardAction")
        self.fileExitAction = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../image3"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileExitAction.setIcon(icon3)
        self.fileExitAction.setProperty("name", "fileExitAction")
        self.fileExitAction.setObjectName("fileExitAction")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileHomeAction)
        self.fileMenu.addAction(self.fileBackAction)
        self.fileMenu.addAction(self.fileForwardAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileExitAction)
        self.menubar.addAction(self.fileMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fileMenu.setTitle(_translate("MainWindow", "&File"))
        self.fileHomeAction.setText(_translate("MainWindow", "Home"))
        self.fileHomeAction.setIconText(_translate("MainWindow", "Home"))
        self.fileHomeAction.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.fileBackAction.setText(_translate("MainWindow", "Back"))
        self.fileBackAction.setIconText(_translate("MainWindow", "Back"))
        self.fileBackAction.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.fileForwardAction.setText(_translate("MainWindow", "Forward"))
        self.fileForwardAction.setIconText(_translate("MainWindow", "Forward"))
        self.fileForwardAction.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.fileExitAction.setText(_translate("MainWindow", "Exit"))
        self.fileExitAction.setIconText(_translate("MainWindow", "Exit"))
        self.fileExitAction.setShortcut(_translate("MainWindow", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

