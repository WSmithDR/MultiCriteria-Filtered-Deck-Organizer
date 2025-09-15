from typing import Dict, Any, List, Optional, Callable
from aqt.qt import (QPushButton, QListWidget, QListWidgetItem, QVBoxLayout, 
                    QHBoxLayout, QGroupBox, QLabel)
from ....constants.ui import UIConstants
from ....styles import styles


class GroupRulesOrderSection(QGroupBox):
    """Sección para configurar el ordenamiento de reglas de agrupamiento"""
    
    def __init__(self, parent=None):
        super().__init__(UIConstants.GROUPING_RULES_ORDER, parent)
        self.grouping_rules = []
        self.on_rule_moved_callback: Optional[Callable] = None
        self.on_rule_removed_callback: Optional[Callable] = None
        self._create_widgets()
        self._setup_layout()
    
    def _create_widgets(self):
        """Crea los widgets para la sección de ordenamiento de reglas"""
        # Lista de reglas de agrupamiento (para ordenamiento)
        self.rules_list_widget = QListWidget()
        self.rules_list_widget.setMaximumHeight(150)
        self.rules_list_widget.setStyleSheet(styles.INPUT)
        
        # Botones para manejar el orden de las reglas
        self.move_up_button = self._create_styled_button(UIConstants.BUTTON_MOVE_UP)
        self.move_down_button = self._create_styled_button(UIConstants.BUTTON_MOVE_DOWN)
        self.remove_rule_button = self._create_styled_button(UIConstants.BUTTON_REMOVE_RULE)
        
        # Conectar eventos
        self.move_up_button.clicked.connect(self._move_rule_up)
        self.move_down_button.clicked.connect(self._move_rule_down)
        self.remove_rule_button.clicked.connect(self._remove_rule)
    
    def _setup_layout(self):
        """Configura el layout de la sección"""
        layout = QVBoxLayout()
        
        # Lista de reglas
        layout.addWidget(QLabel(UIConstants.RULES_ORDER_DESCRIPTION))
        layout.addWidget(self.rules_list_widget)
        
        # Botones de control
        buttons_layout = self._create_horizontal_layout()
        buttons_layout.addWidget(self.move_up_button)
        buttons_layout.addWidget(self.move_down_button)
        buttons_layout.addWidget(self.remove_rule_button)
        buttons_layout.addStretch()
        
        layout.addLayout(buttons_layout)
        self.setLayout(layout)
    
    def _create_styled_button(self, text: str) -> QPushButton:
        """Crea un botón con estilo estándar"""
        button = QPushButton(text)
        button.setStyleSheet(styles.BUTTON)
        return button
    
    def _create_horizontal_layout(self) -> QHBoxLayout:
        """Crea un layout horizontal estándar"""
        return QHBoxLayout()
    
    def _move_rule_up(self):
        """Mueve una regla hacia arriba en la lista"""
        current_row = self.rules_list_widget.currentRow()
        if current_row > 0:
            self.grouping_rules[current_row], self.grouping_rules[current_row - 1] = \
                self.grouping_rules[current_row - 1], self.grouping_rules[current_row]
            self._update_rules_list()
            self.rules_list_widget.setCurrentRow(current_row - 1)
            
            if self.on_rule_moved_callback:
                self.on_rule_moved_callback()
    
    def _move_rule_down(self):
        """Mueve una regla hacia abajo en la lista"""
        current_row = self.rules_list_widget.currentRow()
        if current_row < len(self.grouping_rules) - 1:
            self.grouping_rules[current_row], self.grouping_rules[current_row + 1] = \
                self.grouping_rules[current_row + 1], self.grouping_rules[current_row]
            self._update_rules_list()
            self.rules_list_widget.setCurrentRow(current_row + 1)
            
            if self.on_rule_moved_callback:
                self.on_rule_moved_callback()
    
    def _remove_rule(self):
        """Elimina una regla de la lista"""
        current_row = self.rules_list_widget.currentRow()
        if current_row >= 0:
            del self.grouping_rules[current_row]
            self._update_rules_list()
            
            if self.on_rule_removed_callback:
                self.on_rule_removed_callback()
    
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
    
    def set_grouping_rules(self, rules: List[Dict[str, Any]]):
        """Establece las reglas de agrupamiento"""
        self.grouping_rules = rules.copy()
        self._update_rules_list()
    
    def get_grouping_rules(self) -> List[Dict[str, Any]]:
        """Retorna las reglas de agrupamiento actuales"""
        return self.grouping_rules.copy()
    
    def set_rule_moved_callback(self, callback: Callable):
        """Establece el callback para cuando se mueve una regla"""
        self.on_rule_moved_callback = callback
    
    def set_rule_removed_callback(self, callback: Callable):
        """Establece el callback para cuando se elimina una regla"""
        self.on_rule_removed_callback = callback
    
    def set_enabled(self, enabled: bool):
        """Habilita o deshabilita la sección"""
        self.setEnabled(enabled)
        self.rules_list_widget.setEnabled(enabled)
        self.move_up_button.setEnabled(enabled)
        self.move_down_button.setEnabled(enabled)
        self.remove_rule_button.setEnabled(enabled)
    
    def clear_rules(self):
        """Limpia todas las reglas"""
        self.grouping_rules = []
        self._update_rules_list()
