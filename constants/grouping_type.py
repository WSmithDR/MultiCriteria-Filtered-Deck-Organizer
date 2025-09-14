from enum import Enum

class GroupingType(Enum):
    """Tipos de agrupamiento para los mazos filtrados"""
    NONE = "none"
    NOTE_TYPE = "note_type"
    TEMPLATE = "template"
    FIELD_CONTENT = "field_content"
    TAG = "tag"
    DECK = "deck"
    FLAG = "flag"