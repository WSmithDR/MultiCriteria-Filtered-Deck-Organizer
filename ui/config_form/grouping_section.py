from typing import Dict, Any, List, Optional
from aqt.qt import (QCheckBox, QComboBox, QPushButton, QListWidget, 
                    QListWidgetItem, QVBoxLayout, QHBoxLayout, QFormLayout,
                    QGroupBox, QLabel, QSpinBox, QRadioButton, QButtonGroup,
                    QAbstractItemView)
from .base_section_abs import BaseSection
from ...constants.ui import UIConstants
from ...styles import styles


class GroupingSection(BaseSection):
    """Sección para configurar el agrupamiento de mazos filtrados"""
    
    def __init__(self, parent=None):
        super().__init__(UIConstants.SECTION_GROUPING, parent)
        self.grouping_rules = []
        self.field_names = []  # Lista de campos disponibles
        self.notetypes = []    # Lista de notetypes disponibles
        self.create_widgets()
        self.setup_layout()
    
    def create_widgets(self):
        """Crea los widgets para la sección de agrupamiento"""
        # Widget principal de agrupamiento
        self.grouping_enabled_checkbox = self._create_styled_checkbox(
            UIConstants.CHECKBOX_ENABLE_GROUPING, 
            UIConstants.CHECKBOX_ENABLE_GROUPING_DESCRIPTION
        )
        
        # Sección de agrupamiento por campo
        self.field_grouping_section = self._create_field_grouping_section()
        
        # Sección de agrupamiento por notetype
        self.notetype_grouping_section = self._create_notetype_grouping_section()
        
        # Lista de reglas de agrupamiento (para ordenamiento)
        self.rules_list_widget = QListWidget()
        self.rules_list_widget.setMaximumHeight(150)
        self.rules_list_widget.setStyleSheet(styles.INPUT)
        
        # Botones para manejar el orden de las reglas
        self.move_up_button = self._create_styled_button(UIConstants.BUTTON_MOVE_UP)
        self.move_down_button = self._create_styled_button(UIConstants.BUTTON_MOVE_DOWN)
        self.remove_rule_button = self._create_styled_button(UIConstants.BUTTON_REMOVE_RULE)
        
        # Conectar eventos
        self.grouping_enabled_checkbox.stateChanged.connect(self._on_grouping_enabled_changed)
        self.move_up_button.clicked.connect(self._move_rule_up)
        self.move_down_button.clicked.connect(self._move_rule_down)
        self.remove_rule_button.clicked.connect(self._remove_rule)
        
        # Actualizar estado inicial
        self._update_grouping_ui_state()
    
    def _create_field_grouping_section(self) -> QGroupBox:
        """Crea la sección de agrupamiento por campo"""
        section = QGroupBox(UIConstants.GROUP_BY_FIELD)
        layout = QFormLayout()
        
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
        self.add_field_rule_button.clicked.connect(self._add_field_rule)
        
        # Agregar widgets al layout
        layout.addRow(self.field_grouping_enabled)
        layout.addRow(UIConstants.LABEL_FIELD, self.field_selector)
        layout.addRow(self.field_case_sensitive)
        layout.addRow(self.field_trim_values)
        layout.addRow(self.add_field_rule_button)
        
        section.setLayout(layout)
        return section
    
    def _create_notetype_grouping_section(self) -> QGroupBox:
        """Crea la sección de agrupamiento por notetype"""
        section = QGroupBox(UIConstants.GROUP_BY_NOTE_TYPE)
        layout = QVBoxLayout()
        
        # Checkbox para habilitar agrupamiento por notetype
        self.notetype_grouping_enabled = self._create_styled_checkbox(
            UIConstants.GROUP_BY_NOTE_TYPE,
            UIConstants.GROUP_BY_NOTE_TYPE_DESCRIPTION
        )
        
        # Lista de notetypes disponibles
        self.notetype_list_widget = QListWidget()
        self.notetype_list_widget.setMaximumHeight(120)
        self.notetype_list_widget.setStyleSheet(styles.INPUT)
        self.notetype_list_widget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        
        # Botón para agregar regla de notetype
        self.add_notetype_rule_button = self._create_styled_button(UIConstants.BUTTON_ADD_NOTE_TYPE_RULE)
        self.add_notetype_rule_button.clicked.connect(self._add_notetype_rule)
        
        # Agregar widgets al layout
        layout.addWidget(self.notetype_grouping_enabled)
        layout.addWidget(QLabel(UIConstants.LABEL_SELECT_NOTE_TYPES))
        layout.addWidget(self.notetype_list_widget)
        layout.addWidget(self.add_notetype_rule_button)
        
        section.setLayout(layout)
        return section
    
    def setup_layout(self):
        """Configura el layout de la sección"""
        # Layout principal
        main_layout = self._create_vertical_layout()
        
        # Checkbox principal
        main_layout.addWidget(self.grouping_enabled_checkbox)
        
        # Layout horizontal para las secciones de agrupamiento
        grouping_options_layout = self._create_horizontal_layout()
        grouping_options_layout.addWidget(self.field_grouping_section)
        grouping_options_layout.addWidget(self.notetype_grouping_section)
        
        main_layout.addLayout(grouping_options_layout)
        
        # Sección de reglas y ordenamiento
        rules_section = QGroupBox(UIConstants.GROUPING_RULES_ORDER)
        rules_layout = QVBoxLayout()
        
        # Lista de reglas
        rules_layout.addWidget(QLabel(UIConstants.RULES_ORDER_DESCRIPTION))
        rules_layout.addWidget(self.rules_list_widget)
        
        # Botones de control
        buttons_layout = self._create_horizontal_layout()
        buttons_layout.addWidget(self.move_up_button)
        buttons_layout.addWidget(self.move_down_button)
        buttons_layout.addWidget(self.remove_rule_button)
        buttons_layout.addStretch()
        
        rules_layout.addLayout(buttons_layout)
        rules_section.setLayout(rules_layout)
        
        main_layout.addWidget(rules_section)
        main_layout.addStretch()
        
        # Establecer el layout principal
        self.layout.addLayout(main_layout)
    
    def _on_grouping_enabled_changed(self, state):
        """Maneja el cambio de estado del checkbox principal"""
        self._update_grouping_ui_state()
    
    def _update_grouping_ui_state(self):
        """Actualiza el estado de la UI basado en si el agrupamiento está habilitado"""
        enabled = self.grouping_enabled_checkbox.isChecked()
        
        # Habilitar/deshabilitar todas las secciones de agrupamiento
        self.field_grouping_section.setEnabled(enabled)
        self.notetype_grouping_section.setEnabled(enabled)
        self.rules_list_widget.setEnabled(enabled)
        self.move_up_button.setEnabled(enabled)
        self.move_down_button.setEnabled(enabled)
        self.remove_rule_button.setEnabled(enabled)
    
    def _add_field_rule(self):
        """Agrega una regla de agrupamiento por campo"""
        if not self.field_selector.currentText() or self.field_selector.currentText() == UIConstants.SELECT_FIELD_PLACEHOLDER:
            return
        
        rule = {
            'type': 'field',
            'field_name': self.field_selector.currentText(),
            'case_sensitive': self.field_case_sensitive.isChecked(),
            'trim_values': self.field_trim_values.isChecked()
        }
        
        self.grouping_rules.append(rule)
        self._update_rules_list()
    
    def _add_notetype_rule(self):
        """Agrega una regla de agrupamiento por notetype"""
        selected_items = self.notetype_list_widget.selectedItems()
        if not selected_items:
            return
        
        selected_notetypes = [item.text() for item in selected_items]
        
        rule = {
            'type': 'notetype',
            'notetypes': selected_notetypes
        }
        
        self.grouping_rules.append(rule)
        self._update_rules_list()
    
    def _update_rules_list(self):
        """Actualiza la lista visual de reglas"""
        self.rules_list_widget.clear()
        
        for i, rule in enumerate(self.grouping_rules):
            if rule['type'] == 'field':
                text = f"{UIConstants.RULE_PREFIX_FIELD}{rule['field_name']}"
                if rule['case_sensitive']:
                    text += UIConstants.RULE_SUFFIX_CASE_SENSITIVE
                if rule['trim_values']:
                    text += UIConstants.RULE_SUFFIX_TRIMMED
            elif rule['type'] == 'notetype':
                notetypes_text = ", ".join(rule['notetypes'][:3])  # Mostrar solo primeros 3
                if len(rule['notetypes']) > 3:
                    notetypes_text += UIConstants.RULE_MORE_ITEMS.format(count=len(rule['notetypes'])-3)
                text = f"{UIConstants.RULE_PREFIX_NOTE_TYPES}{notetypes_text}"
            
            item = QListWidgetItem(f"{i+1}. {text}")
            self.rules_list_widget.addItem(item)
    
    def _move_rule_up(self):
        """Mueve una regla hacia arriba en la lista"""
        current_row = self.rules_list_widget.currentRow()
        if current_row > 0:
            self.grouping_rules[current_row], self.grouping_rules[current_row - 1] = \
                self.grouping_rules[current_row - 1], self.grouping_rules[current_row]
            self._update_rules_list()
            self.rules_list_widget.setCurrentRow(current_row - 1)
    
    def _move_rule_down(self):
        """Mueve una regla hacia abajo en la lista"""
        current_row = self.rules_list_widget.currentRow()
        if current_row < len(self.grouping_rules) - 1:
            self.grouping_rules[current_row], self.grouping_rules[current_row + 1] = \
                self.grouping_rules[current_row + 1], self.grouping_rules[current_row]
            self._update_rules_list()
            self.rules_list_widget.setCurrentRow(current_row + 1)
    
    def _remove_rule(self):
        """Elimina una regla de la lista"""
        current_row = self.rules_list_widget.currentRow()
        if current_row >= 0:
            del self.grouping_rules[current_row]
            self._update_rules_list()
    
    def set_available_fields(self, field_names: List[str]):
        """Establece los campos disponibles para agrupamiento"""
        self.field_names = field_names
        self.field_selector.clear()
        self.field_selector.addItem(UIConstants.SELECT_FIELD_PLACEHOLDER)
        self.field_selector.addItems(field_names)
    
    def set_available_notetypes(self, notetypes: List[str]):
        """Establece los notetypes disponibles para agrupamiento"""
        self.notetypes = notetypes
        self.notetype_list_widget.clear()
        self.notetype_list_widget.addItems(notetypes)
    
    def get_data(self) -> Dict[str, Any]:
        """Retorna los datos de la sección"""
        if not self.grouping_enabled_checkbox.isChecked():
            return {
                'enabled': False,
                'rules': []
            }
        
        return {
            'enabled': True,
            'rules': self.grouping_rules.copy()
        }
    
    def set_data(self, data: Dict[str, Any]):
        """Establece los datos de la sección (para edición)"""
        self.grouping_enabled_checkbox.setChecked(data.get('enabled', False))
        self.grouping_rules = data.get('rules', []).copy()
        self._update_rules_list()
        self._update_grouping_ui_state()
    
    def clear_data(self):
        """Limpia los datos de la sección"""
        self.grouping_enabled_checkbox.setChecked(False)
        self.grouping_rules = []
        self._update_rules_list()
        self._update_grouping_ui_state()
    
    def validate(self) -> list:
        """Valida los datos de la sección"""
        errors = []
        
        if self.grouping_enabled_checkbox.isChecked():
            if not self.grouping_rules:
                errors.append(UIConstants.ERROR_NO_GROUPING_RULES)
            
            # Validar reglas de campo
            for rule in self.grouping_rules:
                if rule['type'] == 'field':
                    if not rule.get('field_name'):
                        errors.append(UIConstants.ERROR_EMPTY_FIELD_NAME)
                
                elif rule['type'] == 'notetype':
                    if not rule.get('notetypes'):
                        errors.append(UIConstants.ERROR_NO_NOTE_TYPES_SELECTED)
        
        return errors
