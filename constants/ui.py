

class UIConstants:
    """Constantes para la interfaz de usuario"""
    # Estilos CSS
    SECTION_STYLE = """
        QGroupBox {
            font-weight: bold;
            border: 2px solid #cccccc;
            border-radius: 6px;
            margin-top: 6px;
            padding-top: 10px;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 7px;
            padding: 0px 5px 0px 5px;
        }
    """
    
    INPUT_STYLE = """
        QLineEdit, QComboBox, QSpinBox {
            padding: 5px;
            border: 1px solid #cccccc;
            border-radius: 3px;
            background-color: #ffffff;
        }
        
        QLineEdit:focus, QComboBox:focus, QSpinBox:focus {
            border: 2px solid #4a90e2;
        }
    """
    
    BUTTON_STYLE = """
        QPushButton {
            background-color: #4a90e2;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            font-weight: bold;
        }
        
        QPushButton:hover {
            background-color: #357abd;
        }
        
        QPushButton:pressed {
            background-color: #2968a3;
        }
    """
    
    # Tamaños y márgenes
    SECTION_MARGIN = 10
    SECTION_SPACING = 15
    BUTTON_WIDTH = 120
    BUTTON_HEIGHT = 32
    
    # Textos de la interfaz - Secciones
    SECTION_ACTIONS = "Actions"
    SECTION_BASIC_CONFIG = "Basic Configuration"
    SECTION_SEARCH = "Search - WHERE"
    SECTION_GROUPING = "Grouping - GROUP BY"
    
    # Textos de la interfaz - Botones
    BUTTON_CREATE_FILTERED_DECKS = "Create Filtered Decks"
    BUTTON_TEST_CONFIGURATION = "Test Configuration"
    BUTTON_CANCEL = "Cancel"
    BUTTON_UPDATE_CONFIGURATION = "Update Configuration"
    
    # Textos de la interfaz - Etiquetas y placeholders
    STATUS_READY = "Ready to create filtered decks"
    PLACEHOLDER_CONFIG_NAME = "Enter configuration name..."
    LABEL_NAME = "Name:"
    LABEL_CONFIG_DESCRIPTION = "Name that will identify this filtered deck configuration"
    LABEL_SEARCH_QUERY = "Search Query:"
    PLACEHOLDER_SEARCH_EXAMPLE = "Ex: deck:Current OR tag:important is:due"
    PLACEHOLDER_FIELD_NAME = "Field name to group by..."
    CHECKBOX_ENABLE_MULTIPLE = "Enable multiple groups"
    
    # Textos de la interfaz - Ejemplos de búsqueda
    SEARCH_EXAMPLES_TITLE = "<b>Examples:</b><br>"
    SEARCH_EXAMPLE_DECK = "• <code>deck:Spanish</code> - Specific deck<br>"
    SEARCH_EXAMPLE_DUE = "• <code>is:due</code> - Due cards<br>"
    SEARCH_EXAMPLE_TAG = "• <code>tag:important</code> - By tag<br>"
    SEARCH_EXAMPLE_CONTENT = "• <code>Front:*vocabulary*</code> - By content<br>"
    SEARCH_EXAMPLE_RATED = "• <code>is:rated</code> - Rated cards"
    
    # Textos de la interfaz - Botones de agrupamiento
    BUTTON_ADD_GROUP = "Add Group"
    BUTTON_REMOVE_GROUP = "Remove Group"
    
    # Textos de la interfaz - Diálogos
    DIALOG_TITLE_EDIT = "Edit Configuration"
