from aqt import mw
from aqt.utils import showInfo
from aqt.qt import QDialog, QLineEdit, QPushButton, QVBoxLayout
from ..constans import Constants

class ConfigDialog(QDialog):

  def __init__(self, parent=None):
    super(ConfigDialog, self).__init__(parent)
    
    self.setWindowTitle(Constants.ADDON_NAME)

 