#  reportBug.py: -*- Python -*-  DESCRIPTIVE TEXT.

from modules.UI_reportBugBA import Ui_reportBugBA
from modules.util import *
from PyQt5.QtGui import *
import PyQt5.Qt as qt
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QMenuBar, QMenu, QToolBar, QAction


import sys
import string
import smtplib
from modules.version import VERSION
import modules.xpm as xpm

AUTHOR_ADDR = "phil_schwartz@users.sourceforge.net"

class reportBug(Ui_reportBugBA):
    def __init__(self, parent=None, name=None):
        Ui_reportBugBA.__init__(self, parent, name)
        self.parent = parent
        self.kodos_main = parent.kodos_main
        self.populate()


    def populate(self):
        self.OSEdit.setText(sys.platform)
        pyvers = string.replace(sys.version, "\n", " - ")
        self.pythonVersionEdit.setText(pyvers)
        self.PyQtVersionEdit.setText(qt.QT_VERSION_STR)
        self.regexMultiLineEdit.setText(self.kodos_main.regexMultiLineEdit.text())
        self.stringMultiLineEdit.setText(self.kodos_main.stringMultiLineEdit.text())


    def cancel_slot(self):
        self.parent.close()

    def submit_slot(self):
        addr = str(self.emailAddressEdit.text())
        if not addr:
            msg = self.tr(
                "An email address is necessary so that the author "
                "can contact you.  Your email address will not "
                "be used for any other purposes.")

            QMessageBox.information(None,
                                    self.tr("You must supply a valid email address"),
                                    msg)
            return

        msg = "Subject: Kodos bug report\n\n"
        msg += "Kodos Version: %s\n" % VERSION
        msg += "Operating System: %s\n" % str(self.OSEdit.text())
        msg += "Python Version: %s\n" % str(self.pythonVersionEdit.text())
        msg += "PyQt Version: %s\n" % str(self.PyQtVersionEdit.text())
        msg += "\n" + "=" * 70 + "\n"
        msg += "Regex:\n%s\n" % str(self.regexMultiLineEdit.text())
        msg += "=" * 70 + "\n"
        msg += "String:\n%s\n" % str(self.stringMultiLineEdit.text())
        msg += "=" * 70 + "\n"
        msg += "Comments:\n%s\n" % str(self.commentsMultiLineEdit.text())
        email_server = str(self.kodos_main.prefs.emailServerEdit.text()) or "localhost"
        try:
            server = smtplib.SMTP(email_server)
            server.sendmail(addr, AUTHOR_ADDR, msg)
            server.quit()
            QMessageBox.information(None,
                                    self.tr("Bug report sent"),
                                    self.tr("Your bug report has been sent."))
            self.parent.close()
        except Exception as e:
            QMessageBox.information(None,
                                    self.tr("An exception occurred sending bug report"),
                                    str(e))


class reportBugWindow(QMainWindow):
    def __init__(self, kodos_main):
        self.kodos_main = kodos_main

        QMainWindow.__init__(self, None, None,
                             qt.WType_TopLevel | qt.WDestructiveClose)

        self.setGeometry(100, 50, 800, 600)
        self.setCaption(self.tr("Report a Bug"))
        #self.setWindowIcon(getPixmap("kodos_icon.png", "PNG"))
        self.setWindowIcon(QPixmap(xpm.kodosIcon))
        self.bug_report = reportBug(self)
        self.setCentralWidget(self.bug_report)


        self.createMenu()
        self.createToolBar()

        self.show()


    def createMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        closeButton = QAction('Close',self)
        closeButton.setShortcut('Ctrl+C')
        closeButton.setStatusTip('Close the file')
        closeButton.triggered.connection(self.close)
        fileMenu.addAction(closeButton)

    def createToolBar(self):
        toolbar = QToolBar(self)
        toolbar.setStretchableWidget(self.menubar)
        self.logolabel = kodos_toolbar_logo(toolbar)

