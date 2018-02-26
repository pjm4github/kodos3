# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\PJM\PycharmProjects\kodos\modules\newUserDialogBA.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

class Ui_NewUserDialog(object):
    def setupUi(self, NewUserDialog):
        NewUserDialog.setObjectName("NewUserDialog")
        NewUserDialog.resize(342, 326)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewUserDialog.sizePolicy().hasHeightForWidth())
        NewUserDialog.setSizePolicy(sizePolicy)
        self.vboxlayout = QtWidgets.QVBoxLayout(NewUserDialog)
        self.vboxlayout.setContentsMargins(11, 11, 11, 11)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.textLabel1 = QtWidgets.QLabel(NewUserDialog)
        self.textLabel1.setAlignment(QtCore.Qt.AlignVCenter)
        self.textLabel1.setWordWrap(True)
        self.textLabel1.setObjectName("textLabel1")
        self.vboxlayout1.addWidget(self.textLabel1)
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.pixmapLabel2 = QtWidgets.QLabel(NewUserDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixmapLabel2.sizePolicy().hasHeightForWidth())
        self.pixmapLabel2.setSizePolicy(sizePolicy)
        self.pixmapLabel2.setPixmap(QtGui.QPixmap("../image1"))
        self.pixmapLabel2.setScaledContents(True)
        self.pixmapLabel2.setWordWrap(False)
        self.pixmapLabel2.setObjectName("pixmapLabel2")
        self.gridlayout.addWidget(self.pixmapLabel2, 1, 1, 1, 1)
        self.textLabel4 = QtWidgets.QLabel(NewUserDialog)
        self.textLabel4.setWordWrap(False)
        self.textLabel4.setObjectName("textLabel4")
        self.gridlayout.addWidget(self.textLabel4, 1, 0, 1, 1)
        self.pixmapLabel1 = QtWidgets.QLabel(NewUserDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixmapLabel1.sizePolicy().hasHeightForWidth())
        self.pixmapLabel1.setSizePolicy(sizePolicy)
        self.pixmapLabel1.setPixmap(QtGui.QPixmap("../image2"))
        self.pixmapLabel1.setScaledContents(True)
        self.pixmapLabel1.setWordWrap(False)
        self.pixmapLabel1.setObjectName("pixmapLabel1")
        self.gridlayout.addWidget(self.pixmapLabel1, 0, 1, 1, 1)
        self.textLabel3 = QtWidgets.QLabel(NewUserDialog)
        self.textLabel3.setWordWrap(False)
        self.textLabel3.setObjectName("textLabel3")
        self.gridlayout.addWidget(self.textLabel3, 0, 0, 1, 1)
        self.vboxlayout1.addLayout(self.gridlayout)
        self.vboxlayout.addLayout(self.vboxlayout1)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem = QtWidgets.QSpacerItem(241, 21, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.okButton = QtWidgets.QPushButton(NewUserDialog)
        self.okButton.setDefault(True)
        self.okButton.setObjectName("okButton")
        self.hboxlayout.addWidget(self.okButton)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(NewUserDialog)
        self.okButton.clicked.connect(NewUserDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(NewUserDialog)

    def retranslateUi(self, NewUserDialog):
        _translate = QtCore.QCoreApplication.translate
        NewUserDialog.setWindowTitle(_translate("NewUserDialog", "Kodos new user information"))
        self.textLabel1.setText(_translate("NewUserDialog", "<h3>Welcome to Kodos.</h3>\n"
"<p></p>\n"
"It appears that this is your first time using \n"
"Kodos - The Python Regular Expression Debugger.\n"
"<p></p>\n"
"In order to help you familiarize yourself with Kodos, you may wish to explore\n"
"the Regex Library.  Additionally, Kodos contains a Python Regex Reference Guide. \n"
"You can access these tools by clicking on the appropriate toolbar icon."))
        self.textLabel4.setText(_translate("NewUserDialog", "<b>Regex Reference Guide</b>"))
        self.textLabel3.setText(_translate("NewUserDialog", "<b>Regex Library</b>"))
        self.okButton.setText(_translate("NewUserDialog", "&OK"))
        self.okButton.setShortcut(_translate("NewUserDialog", "Alt+O"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewUserDialog = QtWidgets.QDialog()
    ui = Ui_NewUserDialog()
    ui.setupUi(NewUserDialog)
    NewUserDialog.show()
    sys.exit(app.exec_())

