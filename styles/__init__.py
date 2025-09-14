import os
from aqt.theme import theme_manager


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
    
    @staticmethod
    def _is_dark_mode() -> bool:
        """Detecta si Anki está en modo oscuro usando theme_manager"""
        try:
            # Usar directamente el theme_manager de aqt
            if hasattr(theme_manager, 'night_mode'):
                return theme_manager.night_mode
            elif hasattr(theme_manager, 'dark_mode'):
                return theme_manager.dark_mode
        except Exception:
            pass
        return False  # Default a modo claro
    
    @staticmethod
    def _get_theme_suffix() -> str:
        """Retorna el sufijo para archivos de estilos según el tema actual"""
        return '_dark' if _Styles._is_dark_mode() else ''
    
    @property
    def DIALOG(self) -> str:
        """Estilos para el diálogo principal según el tema actual"""
        suffix = _Styles._get_theme_suffix()
        return _Styles._load_qss_file(f'dialog{suffix}.qss')
    
    @property
    def BUTTON(self) -> str:
        """Estilos para botones según el tema actual"""
        suffix = _Styles._get_theme_suffix()
        return _Styles._load_qss_file(f'button{suffix}.qss')
    
    @property
    def INPUT(self) -> str:
        """Estilos para widgets de entrada según el tema actual"""
        suffix = _Styles._get_theme_suffix()
        return _Styles._load_qss_file(f'input{suffix}.qss')
    
    @property
    def GROUPBOX(self) -> str:
        """Estilos para QGroupBox según el tema actual"""
        suffix = _Styles._get_theme_suffix()
        return _Styles._load_qss_file(f'groupbox{suffix}.qss')
    
    @property
    def LABEL(self) -> str:
        """Estilos para QLabel según el tema actual"""
        suffix = _Styles._get_theme_suffix()
        return _Styles._load_qss_file(f'label{suffix}.qss')
    
    # Métodos de conveniencia
    def get_theme_info(self) -> dict:
        """Retorna información sobre el tema actual"""
        suffix = _Styles._get_theme_suffix()
        return {
            'dark_mode': _Styles._is_dark_mode(),
            'stylesheet_suffix': suffix
        }

# Instancia global para acceso
styles = _Styles()
