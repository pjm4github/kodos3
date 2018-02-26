# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\PJM\PycharmProjects\kodos\modules\resultsBA.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form3(object):
    def setupUi(self, Form3):
        Form3.setObjectName("Form3")
        Form3.resize(715, 250)
        self.gridlayout = QtWidgets.QGridLayout(Form3)
        self.gridlayout.setContentsMargins(11, 11, 11, 11)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.infoTabWidget = QtWidgets.QTabWidget(Form3)
        self.infoTabWidget.setObjectName("infoTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.tab)
        self.vboxlayout.setContentsMargins(11, 11, 11, 11)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupListView = Q3ListView(self.tab)
        self.groupListView.setProperty("allColumnsShowFocus", True)
        self.groupListView.setProperty("showSortIndicator", True)
        self.groupListView.setObjectName("groupListView")
        self.vboxlayout.addWidget(self.groupListView)
        self.infoTabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.tab1)
        self.vboxlayout1.setContentsMargins(11, 11, 11, 11)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.matchTextBrowser = Q3TextBrowser(self.tab1)
        self.matchTextBrowser.setObjectName("matchTextBrowser")
        self.vboxlayout1.addWidget(self.matchTextBrowser)
        self.infoTabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.vboxlayout2 = QtWidgets.QVBoxLayout(self.tab2)
        self.vboxlayout2.setContentsMargins(11, 11, 11, 11)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.codeTextBrowser = Q3TextBrowser(self.tab2)
        self.codeTextBrowser.setObjectName("codeTextBrowser")
        self.vboxlayout2.addWidget(self.codeTextBrowser)
        self.infoTabWidget.addTab(self.tab2, "")
        self.gridlayout.addWidget(self.infoTabWidget, 1, 0, 1, 1)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.TextLabel3 = QtWidgets.QLabel(Form3)
        self.TextLabel3.setWordWrap(False)
        self.TextLabel3.setObjectName("TextLabel3")
        self.hboxlayout.addWidget(self.TextLabel3)
        self.matchNumberSpinBox = QtWidgets.QSpinBox(Form3)
        self.matchNumberSpinBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matchNumberSpinBox.sizePolicy().hasHeightForWidth())
        self.matchNumberSpinBox.setSizePolicy(sizePolicy)
        self.matchNumberSpinBox.setMinimum(1)
        self.matchNumberSpinBox.setObjectName("matchNumberSpinBox")
        self.hboxlayout.addWidget(self.matchNumberSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.gridlayout.addLayout(self.hboxlayout, 0, 0, 1, 1)

        self.retranslateUi(Form3)
        self.matchNumberSpinBox.valueChanged['int'].connect(self.matchNumberSpinBox.match_num_slot)
        QtCore.QMetaObject.connectSlotsByName(Form3)

    def retranslateUi(self, Form3):
        _translate = QtCore.QCoreApplication.translate
        Form3.setWindowTitle(_translate("Form3", "Form3"))
        self.infoTabWidget.setTabText(self.infoTabWidget.indexOf(self.tab), _translate("Form3", "Group"))
        self.infoTabWidget.setTabText(self.infoTabWidget.indexOf(self.tab1), _translate("Form3", "Match"))
        self.infoTabWidget.setTabText(self.infoTabWidget.indexOf(self.tab2), _translate("Form3", "Sample Code"))
        self.TextLabel3.setText(_translate("Form3", "Match number:"))

from q3listview import Q3ListView
from q3textbrowser import Q3TextBrowser

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form3 = QtWidgets.QWidget()
    ui = Ui_Form3()
    ui.setupUi(Form3)
    Form3.show()
    sys.exit(app.exec_())

