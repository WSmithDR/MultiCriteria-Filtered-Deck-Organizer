from typing import Dict, Any, List, Optional, Callable
from aqt.qt import (QCheckBox, QPushButton, QListWidget, 
                    QListWidgetItem, QVBoxLayout, QGroupBox, QLabel,
                    QAbstractItemView)
from ....constants.ui import UIConstants
from ....styles import styles


class NoteTypeGroupingSection(QGroupBox):
    """Sección para configurar el agrupamiento por notetype"""
    
    def __init__(self, parent=None):
        super().__init__(UIConstants.GROUP_BY_NOTE_TYPE, parent)
        self.notetypes = []  # Lista de notetypes disponibles
        self.on_add_rule_callback: Optional[Callable] = None
        self._create_widgets()
        self._setup_layout()
    
    def _create_widgets(self):
        """Crea los widgets para la sección de agrupamiento por notetype"""
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
        self.add_notetype_rule_button.clicked.connect(self._on_add_rule)
    
    def _setup_layout(self):
        """Configura el layout de la sección"""
        layout = QVBoxLayout()
        
        # Agregar widgets al layout
        layout.addWidget(self.notetype_grouping_enabled)
        layout.addWidget(QLabel(UIConstants.LABEL_SELECT_NOTE_TYPES))
        layout.addWidget(self.notetype_list_widget)
        layout.addWidget(self.add_notetype_rule_button)
        
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
        """Maneja el evento de agregar regla de notetype"""
        selected_items = self.notetype_list_widget.selectedItems()
        if not selected_items:
            return
        
        selected_notetypes = [item.text() for item in selected_items]
        
        rule = {
            'type': 'notetype',
            'notetypes': selected_notetypes
        }
        
        if self.on_add_rule_callback:
            self.on_add_rule_callback(rule)
    
    def set_available_notetypes(self, notetypes: List[str]):
        """Establece los notetypes disponibles para agrupamiento"""
        self.notetypes = notetypes
        self.notetype_list_widget.clear()
        self.notetype_list_widget.addItems(notetypes)
    
    def set_add_rule_callback(self, callback: Callable):
        """Establece el callback para cuando se agrega una regla"""
        self.on_add_rule_callback = callback
    
    def get_notetype_rule_data(self) -> Optional[Dict[str, Any]]:
        """Retorna los datos de la regla de notetype actual, o None si no es válida"""
        selected_items = self.notetype_list_widget.selectedItems()
        if not selected_items:
            return None
        
        selected_notetypes = [item.text() for item in selected_items]
        
        return {
            'type': 'notetype',
            'notetypes': selected_notetypes
        }
    
    def clear_selection(self):
        """Limpia la selección actual"""
        self.notetype_list_widget.clearSelection()
