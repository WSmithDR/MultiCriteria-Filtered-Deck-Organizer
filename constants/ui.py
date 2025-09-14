

class UIConstants:
    """Constantes para la interfaz de usuario"""
    
    # Tamaños y márgenes
    SECTION_MARGIN = 10
    SECTION_SPACING = 15
    BUTTON_WIDTH = 120
    BUTTON_HEIGHT = 32
    
    # Márgenes y espaciados del diálogo principal
    DIALOG_MAIN_MARGIN = 20
    DIALOG_MAIN_SPACING = 15
    DIALOG_CONTENT_MARGIN = 15
    DIALOG_CONTENT_SPACING = 15
    
    # Tamaños fijos y dimensiones
    DIALOG_MIN_WIDTH = 600
    DIALOG_MIN_HEIGHT = 700
    BUTTON_WIDTH_EXTENDED = BUTTON_WIDTH + 40  # Para botones principales
    LIST_MAX_HEIGHT = 120
    TEXT_EDIT_MAX_HEIGHT = 100
    
    # Colores y estilos CSS
    COLOR_TEXT_MUTED = "#666666"
    COLOR_TEXT_ERROR = "#d32f2f"
    COLOR_BG_LIGHT = "#f5f5f5"
    FONT_SIZE_SMALL = "11px"
    FONT_SIZE_MEDIUM = "12px"
    BORDER_RADIUS_SMALL = "3px"
    PADDING_SMALL = "5px"
    
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
    PLACEHOLDER_FIELD_NAME_ACTIVE = "Field name to group by"
    PLACEHOLDER_FIELD_NAME_INACTIVE = "Not applicable for this type"
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
    DIALOG_TITLE_MAIN = "Create Configuration"
    DIALOG_TITLE_EDIT = "Edit Configuration"
    
    # Textos de la interfaz - Mensajes de validación
    ERROR_NO_GROUPS = "Must add at least one grouping group"
    ERROR_NO_FIELD_NAME = "Must specify a field name for content grouping"
    
    # Textos de la interfaz - Mensajes de estado
    STATUS_PROCESSING = "Processing..."
    STATUS_CONFIGURATION_COMPLETED = "Configuration completed"
    STATUS_TESTING_CONFIGURATION = "Testing configuration..."
    STATUS_TEST_COMPLETED = "Test completed"
    
    # Textos de la interfaz - Mensajes informativos
    INFO_CONFIG_SAVED = "Configuration '{name}' saved successfully.\nQuery: {query}\nGroups configured: {groups}"
    INFO_CONFIG_TEST = "Configuration test '{name}'.\nThe search would look for: {query}\n{groups} deck groups would be created."
    
    # Textos de la interfaz - Mensajes del addon
    INFO_ADDON_INITIALIZED = "Addon has been initialized!"
    INFO_CARD_OPENED = "Card opened"
    
    # Nombres de objetos UI para selectores CSS
    OBJECT_NAME_SECONDARY = "secondary"
    OBJECT_NAME_STATUS_LABEL = "status_label"
    OBJECT_NAME_DESCRIPTION_LABEL = "description_label"
    OBJECT_NAME_EXAMPLE_LABEL = "example_label"
    OBJECT_NAME_MAIN_WIDGET = "main_widget"
