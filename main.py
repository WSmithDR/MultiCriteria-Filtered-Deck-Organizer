from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import QAction
from .ui import ConfigDialog
from aqt import gui_hooks
from .constants import GeneralConstants


class Main:
  def __init__(self):
    #showInfo("Addon has been initilialized!")
    pass 
  
  def initialize(self):
    action = QAction(GeneralConstants.ADDON_NAME,mw)
    config_dialog = ConfigDialog()
    qconnect(action.triggered, lambda: config_dialog.exec())
    mw.form.menuTools.addAction(action)

    gui_hooks.editor_did_load_note.append(self.__onOpenCard)

  def __onOpenCard(self, editor):
    showInfo("Hinchando las pelotas")