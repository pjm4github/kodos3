# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\PJM\PycharmProjects\kodos\modules\referenceBA.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.referenceListView = QtWidgets.QListView(self.centralwidget)
        self.referenceListView.setObjectName("referenceListView")
        self.gridLayout.addWidget(self.referenceListView, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.MenuBar = QtWidgets.QMenuBar(MainWindow)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.MenuBar.setObjectName("MenuBar")
        self.fileMenu = QtWidgets.QMenu(self.MenuBar)
        self.fileMenu.setObjectName("fileMenu")
        self.editMenu = QtWidgets.QMenu(self.MenuBar)
        self.editMenu.setObjectName("editMenu")
        self.helpMenu = QtWidgets.QMenu(self.MenuBar)
        self.helpMenu.setObjectName("helpMenu")
        self.fileNewAction = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image1"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileNewAction.setIcon(icon)
        self.fileNewAction.setProperty("name", "fileNewAction")
        self.fileNewAction.setObjectName("fileNewAction")
        self.fileOpenAction = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../image2"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileOpenAction.setIcon(icon1)
        self.fileOpenAction.setProperty("name", "fileOpenAction")
        self.fileOpenAction.setObjectName("fileOpenAction")
        self.fileSaveAction = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../image3"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileSaveAction.setIcon(icon2)
        self.fileSaveAction.setProperty("name", "fileSaveAction")
        self.fileSaveAction.setObjectName("fileSaveAction")
        self.fileSaveAsAction = QtWidgets.QAction(MainWindow)
        self.fileSaveAsAction.setShortcut("")
        self.fileSaveAsAction.setProperty("name", "fileSaveAsAction")
        self.fileSaveAsAction.setObjectName("fileSaveAsAction")
        self.filePrintAction = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../image4"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filePrintAction.setIcon(icon3)
        self.filePrintAction.setProperty("name", "filePrintAction")
        self.filePrintAction.setObjectName("filePrintAction")
        self.fileExitAction = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../image5"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileExitAction.setIcon(icon4)
        self.fileExitAction.setShortcut("")
        self.fileExitAction.setProperty("name", "fileExitAction")
        self.fileExitAction.setObjectName("fileExitAction")
        self.editUndoAction = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../image6"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editUndoAction.setIcon(icon5)
        self.editUndoAction.setProperty("name", "editUndoAction")
        self.editUndoAction.setObjectName("editUndoAction")
        self.editRedoAction = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../image7"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editRedoAction.setIcon(icon6)
        self.editRedoAction.setProperty("name", "editRedoAction")
        self.editRedoAction.setObjectName("editRedoAction")
        self.editCutAction = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../image8"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editCutAction.setIcon(icon7)
        self.editCutAction.setProperty("name", "editCutAction")
        self.editCutAction.setObjectName("editCutAction")
        self.editCopyAction = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../image9"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editCopyAction.setIcon(icon8)
        self.editCopyAction.setProperty("name", "editCopyAction")
        self.editCopyAction.setObjectName("editCopyAction")
        self.editPasteAction = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../image10"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editPasteAction.setIcon(icon9)
        self.editPasteAction.setProperty("name", "editPasteAction")
        self.editPasteAction.setObjectName("editPasteAction")
        self.editFindAction = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../image11"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editFindAction.setIcon(icon10)
        self.editFindAction.setProperty("name", "editFindAction")
        self.editFindAction.setObjectName("editFindAction")
        self.helpContentsAction = QtWidgets.QAction(MainWindow)
        self.helpContentsAction.setShortcut("")
        self.helpContentsAction.setProperty("name", "helpContentsAction")
        self.helpContentsAction.setObjectName("helpContentsAction")
        self.helpIndexAction = QtWidgets.QAction(MainWindow)
        self.helpIndexAction.setShortcut("")
        self.helpIndexAction.setProperty("name", "helpIndexAction")
        self.helpIndexAction.setObjectName("helpIndexAction")
        self.helpAboutAction = QtWidgets.QAction(MainWindow)
        self.helpAboutAction.setShortcut("")
        self.helpAboutAction.setProperty("name", "helpAboutAction")
        self.helpAboutAction.setObjectName("helpAboutAction")
        self.helpAction = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../image12"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpAction.setIcon(icon11)
        self.helpAction.setProperty("name", "helpAction")
        self.helpAction.setObjectName("helpAction")
        self.helpPythonAction = QtWidgets.QAction(MainWindow)
        self.helpPythonAction.setProperty("name", "helpPythonAction")
        self.helpPythonAction.setObjectName("helpPythonAction")
        MainWindow.setMenuBar(self.MenuBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileExitAction)
        self.editMenu.addAction(self.editPasteAction)
        self.editMenu.addSeparator()
        self.helpMenu.addAction(self.helpAction)
        self.helpMenu.addAction(self.helpPythonAction)
        self.MenuBar.addAction(self.fileMenu.menuAction())
        self.MenuBar.addAction(self.editMenu.menuAction())
        self.MenuBar.addAction(self.helpMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fileMenu.setTitle(_translate("MainWindow", "&File"))
        self.editMenu.setTitle(_translate("MainWindow", "&Edit"))
        self.helpMenu.setTitle(_translate("MainWindow", "&Help"))
        self.fileNewAction.setText(_translate("MainWindow", "&New"))
        self.fileNewAction.setIconText(_translate("MainWindow", "New"))
        self.fileNewAction.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.fileOpenAction.setText(_translate("MainWindow", "&Open..."))
        self.fileOpenAction.setIconText(_translate("MainWindow", "Open"))
        self.fileOpenAction.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.fileSaveAction.setText(_translate("MainWindow", "&Save"))
        self.fileSaveAction.setIconText(_translate("MainWindow", "Save"))
        self.fileSaveAction.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.fileSaveAsAction.setText(_translate("MainWindow", "Save &As..."))
        self.fileSaveAsAction.setIconText(_translate("MainWindow", "Save As"))
        self.filePrintAction.setText(_translate("MainWindow", "&Print..."))
        self.filePrintAction.setIconText(_translate("MainWindow", "Print"))
        self.filePrintAction.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.fileExitAction.setText(_translate("MainWindow", "E&xit"))
        self.fileExitAction.setIconText(_translate("MainWindow", "Exit"))
        self.editUndoAction.setText(_translate("MainWindow", "&Undo"))
        self.editUndoAction.setIconText(_translate("MainWindow", "Undo"))
        self.editUndoAction.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.editRedoAction.setText(_translate("MainWindow", "&Redo"))
        self.editRedoAction.setIconText(_translate("MainWindow", "Redo"))
        self.editRedoAction.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.editCutAction.setText(_translate("MainWindow", "&Cut"))
        self.editCutAction.setIconText(_translate("MainWindow", "Cut"))
        self.editCutAction.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.editCopyAction.setText(_translate("MainWindow", "C&opy"))
        self.editCopyAction.setIconText(_translate("MainWindow", "Copy"))
        self.editCopyAction.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.editPasteAction.setText(_translate("MainWindow", "&Paste"))
        self.editPasteAction.setIconText(_translate("MainWindow", "Paste"))
        self.editPasteAction.setToolTip(_translate("MainWindow", "Paste selection into Kodos"))
        self.editPasteAction.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.editFindAction.setText(_translate("MainWindow", "&Find..."))
        self.editFindAction.setIconText(_translate("MainWindow", "Find"))
        self.editFindAction.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.helpContentsAction.setText(_translate("MainWindow", "&Contents..."))
        self.helpContentsAction.setIconText(_translate("MainWindow", "Contents"))
        self.helpIndexAction.setText(_translate("MainWindow", "&Index..."))
        self.helpIndexAction.setIconText(_translate("MainWindow", "Index"))
        self.helpAboutAction.setText(_translate("MainWindow", "&About"))
        self.helpAboutAction.setIconText(_translate("MainWindow", "About"))
        self.helpAction.setText(_translate("MainWindow", "&Help"))
        self.helpAction.setIconText(_translate("MainWindow", "Help"))
        self.helpPythonAction.setText(_translate("MainWindow", "&Python Regex Help"))
        self.helpPythonAction.setIconText(_translate("MainWindow", "Python Regex Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

