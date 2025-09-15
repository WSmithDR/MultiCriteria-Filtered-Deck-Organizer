from typing import Dict, Any, List, Optional, Callable
from aqt.qt import (QCheckBox, QComboBox, QPushButton, QFormLayout,
                    QGroupBox, QLabel)
from ....constants.ui import UIConstants
from ....styles import styles


class FieldGroupingSection(QGroupBox):
    """Sección para configurar el agrupamiento por campo"""
    
    def __init__(self, parent=None):
        super().__init__(UIConstants.GROUP_BY_FIELD, parent)
        self.field_names = []  # Lista de campos disponibles
        self.on_add_rule_callback: Optional[Callable] = None
        self._create_widgets()
        self._setup_layout()
    
    def _create_widgets(self):
        """Crea los widgets para la sección de agrupamiento por campo"""
        # Checkbox para habilitar agrupamiento por campo
        self.field_grouping_enabled = self._create_styled_checkbox(
            UIConstants.GROUP_BY_FIELD_VALUE,
            UIConstants.GROUP_BY_FIELD_DESCRIPTION
        )
        
        # Combobox para seleccionar el campo
        self.field_selector = QComboBox()
        self.field_selector.setStyleSheet(styles.INPUT)
        self.field_selector.addItem(UIConstants.SELECT_FIELD_PLACEHOLDER)
        
        # Opciones adicionales para agrupamiento por campo
        self.field_case_sensitive = self._create_styled_checkbox(
            UIConstants.CHECKBOX_CASE_SENSITIVE,
            UIConstants.CHECKBOX_CASE_SENSITIVE_DESCRIPTION
        )
        
        self.field_trim_values = self._create_styled_checkbox(
            UIConstants.CHECKBOX_TRIM_WHITESPACE,
            UIConstants.CHECKBOX_TRIM_WHITESPACE_DESCRIPTION
        )
        
        # Botón para agregar regla de campo
        self.add_field_rule_button = self._create_styled_button(UIConstants.BUTTON_ADD_FIELD_RULE)
        self.add_field_rule_button.clicked.connect(self._on_add_rule)
    
    def _setup_layout(self):
        """Configura el layout de la sección"""
        layout = QFormLayout()
        
        # Agregar widgets al layout
        layout.addRow(self.field_grouping_enabled)
        layout.addRow(UIConstants.LABEL_FIELD, self.field_selector)
        layout.addRow(self.field_case_sensitive)
        layout.addRow(self.field_trim_values)
        layout.addRow(self.add_field_rule_button)
        
        self.setLayout(layout)
    
    def _create_styled_checkbox(self, text: str, tooltip: str = "") -> QCheckBox:
        """Crea un checkbox con estilo estándar"""
        checkbox = QCheckBox(text)
        checkbox.setStyleSheet(styles.CHECKBOX)
        if tooltip:
            checkbox.setToolTip(tooltip)
        return checkbox
    
    def _create_styled_button(self, text: str) -> QPushButton:
        """Crea un botón con estilo estándar"""
        button = QPushButton(text)
        button.setStyleSheet(styles.BUTTON)
        return button
    
    def _on_add_rule(self):
        """Maneja el evento de agregar regla de campo"""
        if not self.field_selector.currentText() or self.field_selector.currentText() == UIConstants.SELECT_FIELD_PLACEHOLDER:
            return
        
        rule = {
            'type': 'field',
            'field_name': self.field_selector.currentText(),
            'case_sensitive': self.field_case_sensitive.isChecked(),
            'trim_values': self.field_trim_values.isChecked()
        }
        
        if self.on_add_rule_callback:
            self.on_add_rule_callback(rule)
    
    def set_available_fields(self, field_names: List[str]):
        """Establece los campos disponibles para agrupamiento"""
        self.field_names = field_names
        self.field_selector.clear()
        self.field_selector.addItem(UIConstants.SELECT_FIELD_PLACEHOLDER)
        self.field_selector.addItems(field_names)
    
    def set_add_rule_callback(self, callback: Callable):
        """Establece el callback para cuando se agrega una regla"""
        self.on_add_rule_callback = callback
    
    def get_field_rule_data(self) -> Optional[Dict[str, Any]]:
        """Retorna los datos de la regla de campo actual, o None si no es válida"""
        if not self.field_selector.currentText() or self.field_selector.currentText() == UIConstants.SELECT_FIELD_PLACEHOLDER:
            return None
        
        return {
            'type': 'field',
            'field_name': self.field_selector.currentText(),
            'case_sensitive': self.field_case_sensitive.isChecked(),
            'trim_values': self.field_trim_values.isChecked()
        }
    
    def clear_selection(self):
        """Limpia la selección actual"""
        self.field_selector.setCurrentIndex(0)
        self.field_case_sensitive.setChecked(False)
        self.field_trim_values.setChecked(False)
