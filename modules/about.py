#  about.py: -*- Python -*-  DESCRIPTIVE TEXT.

from PyQt5  import *
from modules.Ui_aboutBA import Ui_AboutBA
from modules.util import getPixmap
import modules.version

class About(Ui_AboutBA):
    def __init__(self):
        Ui_AboutBA.__init__(self)
        self.image0 = getPixmap("kodos.png")
        self.versionLabel.setText(modules.version.VERSION)

