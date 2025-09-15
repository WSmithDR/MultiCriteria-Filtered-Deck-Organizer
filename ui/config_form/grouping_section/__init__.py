from typing import Dict, Any, List, Optional
from aqt.qt import (QCheckBox, QPushButton, QListWidget, 
                    QListWidgetItem, QVBoxLayout, QHBoxLayout, QFormLayout,
                    QGroupBox, QLabel, QSpinBox, QRadioButton, QButtonGroup,
                    QAbstractItemView)
from ..base_section_abs import BaseSection
from .field_grouping_section import FieldGroupingSection
from .notetype_grouping_section import NoteTypeGroupingSection
from .group_rules_order_section import GroupRulesOrderSection
from ....constants.ui import UIConstants
from ....styles import styles


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
        self.field_grouping_section = FieldGroupingSection()
        self.field_grouping_section.set_add_rule_callback(self._add_field_rule)
        
        # Sección de agrupamiento por notetype
        self.notetype_grouping_section = NoteTypeGroupingSection()
        self.notetype_grouping_section.set_add_rule_callback(self._add_notetype_rule)
        
        # Sección de ordenamiento de reglas
        self.group_rules_order_section = GroupRulesOrderSection()
        self.group_rules_order_section.set_rule_moved_callback(self._on_rule_moved)
        self.group_rules_order_section.set_rule_removed_callback(self._on_rule_removed)
        
        # Conectar eventos
        self.grouping_enabled_checkbox.stateChanged.connect(self._on_grouping_enabled_changed)
        
        # Actualizar estado inicial
        self._update_grouping_ui_state()
    
    
    
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
        
        # Sección de ordenamiento de reglas
        main_layout.addWidget(self.group_rules_order_section)
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
        self.group_rules_order_section.set_enabled(enabled)
    
    def _add_field_rule(self, rule: Dict[str, Any]):
        """Agrega una regla de agrupamiento por campo"""
        self.grouping_rules.append(rule)
        self.group_rules_order_section.set_grouping_rules(self.grouping_rules)
        self.field_grouping_section.clear_selection()
    
    def _add_notetype_rule(self, rule: Dict[str, Any]):
        """Agrega una regla de agrupamiento por notetype"""
        self.grouping_rules.append(rule)
        self.group_rules_order_section.set_grouping_rules(self.grouping_rules)
        self.notetype_grouping_section.clear_selection()
    
    def _on_rule_moved(self):
        """Callback para cuando se mueve una regla"""
        self.grouping_rules = self.group_rules_order_section.get_grouping_rules()
    
    def _on_rule_removed(self):
        """Callback para cuando se elimina una regla"""
        self.grouping_rules = self.group_rules_order_section.get_grouping_rules()
    
    
    def set_available_fields(self, field_names: List[str]):
        """Establece los campos disponibles para agrupamiento"""
        self.field_names = field_names
        self.field_grouping_section.set_available_fields(field_names)
    
    def set_available_notetypes(self, notetypes: List[str]):
        """Establece los notetypes disponibles para agrupamiento"""
        self.notetypes = notetypes
        self.notetype_grouping_section.set_available_notetypes(notetypes)
    
    def get_data(self) -> Dict[str, Any]:
        """Retorna los datos de la sección"""
        return {
            'enabled': self.grouping_enabled_checkbox.isChecked(),
            'grouping_rules': self.group_rules_order_section.get_grouping_rules()
        }
    
    def set_data(self, data: Dict[str, Any]):
        """Establece los datos de la sección (para edición)"""
        self.grouping_enabled_checkbox.setChecked(data.get('enabled', False))
        self.grouping_rules = data.get('grouping_rules', [])
        self.group_rules_order_section.set_grouping_rules(self.grouping_rules)
        self._update_grouping_ui_state()
    
    def clear_data(self):
        """Limpia los datos de la sección"""
        self.grouping_enabled_checkbox.setChecked(False)
        self.grouping_rules = []
        self.group_rules_order_section.clear_rules()
        self.field_grouping_section.clear_selection()
        self.notetype_grouping_section.clear_selection()
        self._update_grouping_ui_state()
    
    def validate(self) -> list:
        """Valida los datos de la sección"""
        errors = []
        
        if self.grouping_enabled_checkbox.isChecked():
            if not self.group_rules_order_section.get_grouping_rules():
                errors.append(UIConstants.ERROR_NO_GROUPING_RULES)
            
            # Validar reglas de campo
            for rule in self.group_rules_order_section.get_grouping_rules():
                if rule['type'] == 'field':
                    if not rule.get('field_name'):
                        errors.append(UIConstants.ERROR_EMPTY_FIELD_NAME)
                
                elif rule['type'] == 'notetype':
                    if not rule.get('notetypes'):
                        errors.append(UIConstants.ERROR_NO_NOTE_TYPES_SELECTED)
        
        return errors
