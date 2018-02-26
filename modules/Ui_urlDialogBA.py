# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\PJM\PycharmProjects\kodos\modules\urlDialogBA.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_URLDialogBA(object):
    def setupUi(self, URLDialogBA):
        URLDialogBA.setObjectName("URLDialogBA")
        URLDialogBA.resize(443, 170)
        URLDialogBA.setSizeGripEnabled(True)
        self.gridlayout = QtWidgets.QGridLayout(URLDialogBA)
        self.gridlayout.setContentsMargins(11, 11, 11, 11)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        self.buttonHelp = QtWidgets.QPushButton(URLDialogBA)
        self.buttonHelp.setAutoDefault(True)
        self.buttonHelp.setObjectName("buttonHelp")
        self.hboxlayout.addWidget(self.buttonHelp)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.buttonOk = QtWidgets.QPushButton(URLDialogBA)
        self.buttonOk.setShortcut("")
        self.buttonOk.setAutoDefault(True)
        self.buttonOk.setDefault(True)
        self.buttonOk.setObjectName("buttonOk")
        self.hboxlayout.addWidget(self.buttonOk)
        self.buttonCancel = QtWidgets.QPushButton(URLDialogBA)
        self.buttonCancel.setShortcut("")
        self.buttonCancel.setAutoDefault(True)
        self.buttonCancel.setObjectName("buttonCancel")
        self.hboxlayout.addWidget(self.buttonCancel)
        self.gridlayout.addLayout(self.hboxlayout, 1, 0, 1, 1)
        self.groupBox1 = QtWidgets.QGroupBox(URLDialogBA)
        self.groupBox1.setObjectName("groupBox1")
        self.gridlayout1 = QtWidgets.QGridLayout(self.groupBox1)
        self.gridlayout1.setContentsMargins(11, 11, 11, 11)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")
        self.URLTextEdit = QtWidgets.QTextEdit(self.groupBox1)
        self.URLTextEdit.setObjectName("URLTextEdit")
        self.gridlayout1.addWidget(self.URLTextEdit, 0, 0, 1, 1)
        self.gridlayout.addWidget(self.groupBox1, 0, 0, 1, 1)

        self.retranslateUi(URLDialogBA)
        QtCore.QMetaObject.connectSlotsByName(URLDialogBA)

    def retranslateUi(self, URLDialogBA):
        _translate = QtCore.QCoreApplication.translate
        URLDialogBA.setWindowTitle(_translate("URLDialogBA", "Import URL"))
        self.buttonHelp.setText(_translate("URLDialogBA", "&Help"))
        self.buttonHelp.setShortcut(_translate("URLDialogBA", "F1"))
        self.buttonOk.setText(_translate("URLDialogBA", "&OK"))
        self.buttonCancel.setText(_translate("URLDialogBA", "&Cancel"))
        self.groupBox1.setTitle(_translate("URLDialogBA", "Enter URL to import"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    URLDialogBA = QtWidgets.QDialog()
    ui = Ui_URLDialogBA()
    ui.setupUi(URLDialogBA)
    URLDialogBA.show()
    sys.exit(app.exec_())

