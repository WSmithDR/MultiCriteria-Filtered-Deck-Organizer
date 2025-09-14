from typing import Dict, Any, List
from aqt.qt import (
    QCheckBox, QListWidget, QListWidgetItem, Qt, QComboBox, QLineEdit
)
from .base_section import BaseSection
from ...constants import GroupingType, GroupingCombination
from ...constants.ui import UIConstants

class GroupingSection(BaseSection):
    """Sección para configurar el agrupamiento de mazos filtrados"""
    
    def __init__(self, parent=None):
        super().__init__(UIConstants.SECTION_GROUPING, parent)
        self.grouping_type_combo = None
        self.combination_type_combo = None
        self.field_name_input = None
        self.enable_multiple_check = None
        self.grouping_list = None
        self.add_group_button = None
        self.remove_group_button = None
        self.create_widgets()
        self.setup_layout()
    
    def create_widgets(self):
        """Crea los widgets para la sección de agrupamiento"""
        # Tipo de agrupamiento principal
        self.grouping_type_combo = self._create_styled_input(QComboBox)
        for group_type in GroupingType:
            self.grouping_type_combo.addItem(group_type.value.replace('_', ' ').title(), group_type)
        
        # Tipo de combinación
        self.combination_type_combo = self._create_styled_input(QComboBox)
        for combo_type in GroupingCombination:
            self.combination_type_combo.addItem(combo_type.value.replace('_', ' ').title(), combo_type)
        
        # Campo para nombre de campo (cuando se selecciona FIELD_CONTENT)
        self.field_name_input = self._create_styled_input(
            QLineEdit,
            UIConstants.PLACEHOLDER_FIELD_NAME
        )
        
        # Habilitar múltiples grupos
        self.enable_multiple_check = QCheckBox(UIConstants.CHECKBOX_ENABLE_MULTIPLE)
        
        # Lista de grupos actuales
        self.grouping_list = self._create_styled_input(QListWidget)
        self.grouping_list.setMaximumHeight(UIConstants.LIST_MAX_HEIGHT)
        
        # Botones para gestionar grupos
        self.add_group_button = self._create_styled_button(
            UIConstants.BUTTON_ADD_GROUP
        )
        
        self.remove_group_button = self._create_styled_button(
            UIConstants.BUTTON_REMOVE_GROUP
        )
        
        # Conectar señales
        self.grouping_type_combo.currentTextChanged.connect(self._on_grouping_type_changed)
        self.add_group_button.clicked.connect(self._add_group)
        self.remove_group_button.clicked.connect(self._remove_group)
    
    def setup_layout(self):
        """Configura el layout de la sección"""
        # Layout principal
        main_layout = self._create_vertical_layout()
        
        # Form layout para configuración básica
        form_layout = self._create_form_layout()
        form_layout.addRow("Tipo de agrupamiento:", self.grouping_type_combo)
        form_layout.addRow("Combinación:", self.combination_type_combo)
        form_layout.addRow("Campo (si aplica):", self.field_name_input)
        
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.enable_multiple_check)
        main_layout.addWidget(self.grouping_list)
        
        # Layout horizontal para botones
        button_layout = self._create_horizontal_layout()
        button_layout.addWidget(self.add_group_button)
        button_layout.addWidget(self.remove_group_button)
        button_layout.addStretch()
        
        main_layout.addLayout(button_layout)
        
        # Agregar al layout de la sección
        self.layout.addLayout(main_layout)
        
        # Estado inicial
        self._on_grouping_type_changed(self.grouping_type_combo.currentText())
    
    def _on_grouping_type_changed(self, value):
        """Maneja el cambio de tipo de agrupamiento"""
        # Mostrar/ocultar campo de nombre de campo según el tipo
        if value == GroupingType.FIELD_CONTENT.value:
            self.field_name_input.setEnabled(True)
            self.field_name_input.setPlaceholderText(UIConstants.PLACEHOLDER_FIELD_NAME_ACTIVE)
        else:
            self.field_name_input.setEnabled(False)
            self.field_name_input.setPlaceholderText(UIConstants.PLACEHOLDER_FIELD_NAME_INACTIVE)
            self.field_name_input.clear()
    
    def _add_group(self):
        """Agrega un nuevo grupo a la lista"""
        current_type = self.grouping_type_combo.currentData()
        field_value = self.field_name_input.text() if current_type == GroupingType.FIELD_CONTENT else ""
        
        group_text = f"{current_type.value}"
        if field_value:
            group_text += f" ({field_value})"
        
        item = QListWidgetItem(group_text)
        item.setData(Qt.ItemDataRole.UserRole, {
            'type': current_type,
            'field': field_value
        })
        self.grouping_list.addItem(item)
    
    def _remove_group(self):
        """Elimina el grupo seleccionado"""
        current_item = self.grouping_list.currentItem()
        if current_item:
            self.grouping_list.takeItem(self.grouping_list.row(current_item))
    
    def get_data(self) -> Dict[str, Any]:
        """Retorna los datos de la sección"""
        groups = []
        for i in range(self.grouping_list.count()):
            item = self.grouping_list.item(i)
            group_data = item.data(Qt.ItemDataRole.UserRole)
            groups.append(group_data)
        
        return {
            "grouping_type": self.grouping_type_combo.currentData(),
            "combination_type": self.combination_type_combo.currentData(),
            "enable_multiple": self.enable_multiple_check.isChecked(),
            "groups": groups
        }
    
    def set_data(self, data: Dict[str, Any]):
        """Establece los datos de la sección (para edición)"""
        if "grouping_type" in data:
            index = self.grouping_type_combo.findData(data["grouping_type"])
            if index >= 0:
                self.grouping_type_combo.setCurrentIndex(index)
        
        if "combination_type" in data:
            index = self.combination_type_combo.findData(data["combination_type"])
            if index >= 0:
                self.combination_type_combo.setCurrentIndex(index)
        
        if "enable_multiple" in data:
            self.enable_multiple_check.setChecked(data["enable_multiple"])
        
        if "groups" in data:
            self.grouping_list.clear()
            for group_data in data["groups"]:
                item = QListWidgetItem(f"{group_data['type'].value}")
                if group_data.get('field'):
                    item.setText(f"{group_data['type'].value} ({group_data['field']})")
                item.setData(Qt.ItemDataRole.UserRole, group_data)
                self.grouping_list.addItem(item)
    
    def clear_data(self):
        """Limpia los datos de la sección"""
        self.grouping_type_combo.setCurrentIndex(0)
        self.combination_type_combo.setCurrentIndex(0)
        self.field_name_input.clear()
        self.enable_multiple_check.setChecked(False)
        self.grouping_list.clear()
    
    def validate(self) -> list:
        """Valida los datos de la sección"""
        errors = []
        if self.grouping_list.count() == 0:
            errors.append(UIConstants.ERROR_NO_GROUPS)
        
        current_type = self.grouping_type_combo.currentData()
        if current_type == GroupingType.FIELD_CONTENT and not self.field_name_input.text().strip():
            errors.append(UIConstants.ERROR_NO_FIELD_NAME)
        
        return errors
