from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import QAction
from .test import Test
from aqt import gui_hooks
from .constans import Constants


class Main:
  def __init__(self):
    #showInfo("Addon has been initilialized!")
    pass 
  
  def initialize(self):
    action = QAction(Constants.ADDON_NAME,mw)
    qconnect(action.triggered, Test.testFunction)
    mw.form.menuTools.addAction(action)

    gui_hooks.editor_did_load_note.append(self.__onOpenCard)

  def __onOpenCard(self, editor):
    showInfo("Hinchando las pelotas")
    