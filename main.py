from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import QAction
from .test import Test


class Main:
  def __init__(self):
    showInfo("Addon has been initilialized!")
 
  def initialize(self):
    action = QAction("test",mw)
    qconnect(action.triggered, Test.testFunction)
    mw.form.menuTools.addAction(action)