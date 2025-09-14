

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
