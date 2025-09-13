from aqt import mw
from aqt.utils import showInfo

class Test:

  @staticmethod
  def testFunction()->None:
    cardCount = mw.col.card_count()
    showInfo(f"Card count {cardCount}")