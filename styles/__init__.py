import os

class _Styles:
    """Clase que contiene todos los estilos CSS para la aplicación"""
    
    @staticmethod
    def _load_qss_file(filename: str) -> str:
        """Carga el contenido de un archivo QSS"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return ""
    
    @property
    def GROUPBOX(self) -> str:
        """Estilos para QGroupBox desde groupbox.qss"""
        return _Styles._load_qss_file('groupbox.qss')
    
    @property
    def BUTTON(self) -> str:
        """Estilos para QPushButton desde button.qss"""
        return _Styles._load_qss_file('button.qss')
    
    @property
    def INPUT(self) -> str:
        """Estilos para widgets de entrada desde input.qss"""
        return _Styles._load_qss_file('input.qss')
    
    @property
    def DIALOG(self) -> str:
        """Estilos para el diálogo principal desde dialog.qss"""
        return _Styles._load_qss_file('dialog.qss')

# Instancia global para acceso
styles = _Styles()
