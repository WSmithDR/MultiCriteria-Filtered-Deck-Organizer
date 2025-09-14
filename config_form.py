from aqt import mw
from aqt.utils import showInfo
from aqt.qt import QDialog, QLineEdit, QPushButton, QVBoxLayout

class ConfigForm(QDialog):

  def __init__(self, parent=None):
    super(ConfigForm, self).__init__(parent)

    self.edit = QLineEdit("Write my name here")
    self.button = QPushButton("Show greeting")
    
    self.setWindowTitle("Config Form")

    layout = QVBoxLayout()
    layout.addWidget(self.edit)
    layout.addWidget(self.button)

    self.setLayout(layout)

    self.button.clicked.connect(self.__greetings)

  def __greetings(self):
    showInfo(f"Hello {self.edit.text()}")
 