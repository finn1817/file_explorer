"""
Settings Dialog for Liquid Glass File Explorer
Provides in-app configuration options
"""

from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                            QPushButton, QComboBox, QSpinBox, QCheckBox,
                            QGroupBox, QSlider, QTabWidget, QWidget,
                            QColorDialog, QFontDialog)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont


class SettingsDialog(QDialog):
    """Settings dialog with multiple configuration tabs"""
    
    settings_changed = pyqtSignal(dict)  # Signal to notify of setting changes
    
    def __init__(self, parent=None, current_settings=None):
        super().__init__(parent)
        self.current_settings = current_settings or {}
        self.init_ui()
        self.load_current_settings()
    
    def init_ui(self):
        """Initialize the settings UI"""
        self.setWindowTitle("⚙️ Settings")
        self.setModal(True)
        self.setMinimumSize(600, 500)
        
        layout = QVBoxLayout(self)
        
        # Create tab widget
        self.tabs = QTabWidget()
        
        # Add tabs
        self.tabs.addTab(self.create_appearance_tab(), "🎨 Appearance")
        self.tabs.addTab(self.create_behavior_tab(), "⚡ Behavior")
        self.tabs.addTab(self.create_view_tab(), "👁️ View")
        self.tabs.addTab(self.create_advanced_tab(), "🔧 Advanced")
        
        layout.addWidget(self.tabs)
        
        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        self.reset_btn = QPushButton("🔄 Reset to Defaults")
        self.reset_btn.clicked.connect(self.reset_to_defaults)
        button_layout.addWidget(self.reset_btn)
        
        self.cancel_btn = QPushButton("❌ Cancel")
        self.cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(self.cancel_btn)
        
        self.apply_btn = QPushButton("✅ Apply")
        self.apply_btn.clicked.connect(self.apply_settings)
        button_layout.addWidget(self.apply_btn)
        
        layout.addLayout(button_layout)
    
    def create_appearance_tab(self):
        """Create appearance settings tab"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Theme selection
        theme_group = QGroupBox("Theme")
        theme_layout = QVBoxLayout()
        
        theme_label = QLabel("Select Theme:")
        theme_layout.addWidget(theme_label)
        
        self.theme_combo = QComboBox()
        self.theme_combo.addItem("✨ Liquid Glass", "liquid_glass")
        self.theme_combo.addItem("🌙 Dark", "dark")
        self.theme_combo.addItem("☀️ Light", "light")
        theme_layout.addWidget(self.theme_combo)
        
        theme_group.setLayout(theme_layout)
        layout.addWidget(theme_group)
        
        # Font settings
        font_group = QGroupBox("Font")
        font_layout = QVBoxLayout()
        
        # Font size
        font_size_layout = QHBoxLayout()
        font_size_label = QLabel("Font Size:")
        self.font_size_spin = QSpinBox()
        self.font_size_spin.setRange(8, 24)
        self.font_size_spin.setValue(11)
        self.font_size_spin.setSuffix(" pt")
        font_size_layout.addWidget(font_size_label)
        font_size_layout.addWidget(self.font_size_spin)
        font_size_layout.addStretch()
        font_layout.addLayout(font_size_layout)
        
        # Font family
        font_family_layout = QHBoxLayout()
        font_family_label = QLabel("Font Family:")
        self.font_family_combo = QComboBox()
        self.font_family_combo.addItems([
            "Segoe UI", "Arial", "Helvetica", "Calibri", 
            "Consolas", "Courier New", "Times New Roman"
        ])
        font_family_layout.addWidget(font_family_label)
        font_family_layout.addWidget(self.font_family_combo)
        font_layout.addLayout(font_family_layout)
        
        font_group.setLayout(font_layout)
        layout.addWidget(font_group)
        
        # Window effects
        effects_group = QGroupBox("Window Effects")
        effects_layout = QVBoxLayout()
        
        self.blur_checkbox = QCheckBox("Enable blur effect (Liquid Glass only)")
        self.blur_checkbox.setChecked(True)
        effects_layout.addWidget(self.blur_checkbox)
        
        self.shadow_checkbox = QCheckBox("Enable shadow effects")
        self.shadow_checkbox.setChecked(True)
        effects_layout.addWidget(self.shadow_checkbox)
        
        effects_group.setLayout(effects_layout)
        layout.addWidget(effects_group)
        
        layout.addStretch()
        return tab
    
    def create_behavior_tab(self):
        """Create behavior settings tab"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # File operations
        file_ops_group = QGroupBox("File Operations")
        file_ops_layout = QVBoxLayout()
        
        self.confirm_delete_checkbox = QCheckBox("Confirm before deleting")
        self.confirm_delete_checkbox.setChecked(True)
        file_ops_layout.addWidget(self.confirm_delete_checkbox)
        
        self.use_trash_checkbox = QCheckBox("Move to trash instead of permanent delete")
        self.use_trash_checkbox.setChecked(True)
        file_ops_layout.addWidget(self.use_trash_checkbox)
        
        self.double_click_checkbox = QCheckBox("Double-click to open files")
        self.double_click_checkbox.setChecked(True)
        file_ops_layout.addWidget(self.double_click_checkbox)
        
        file_ops_group.setLayout(file_ops_layout)
        layout.addWidget(file_ops_group)
        
        # Navigation
        nav_group = QGroupBox("Navigation")
        nav_layout = QVBoxLayout()
        
        self.show_hidden_checkbox = QCheckBox("Show hidden files")
        self.show_hidden_checkbox.setChecked(False)
        nav_layout.addWidget(self.show_hidden_checkbox)
        
        self.remember_location_checkbox = QCheckBox("Remember last location on startup")
        self.remember_location_checkbox.setChecked(True)
        nav_layout.addWidget(self.remember_location_checkbox)
        
        nav_group.setLayout(nav_layout)
        layout.addWidget(nav_group)
        
        # Performance
        perf_group = QGroupBox("Performance")
        perf_layout = QVBoxLayout()
        
        self.auto_refresh_checkbox = QCheckBox("Auto-refresh file list")
        self.auto_refresh_checkbox.setChecked(True)
        perf_layout.addWidget(self.auto_refresh_checkbox)
        
        refresh_interval_layout = QHBoxLayout()
        refresh_label = QLabel("Refresh interval:")
        self.refresh_interval_spin = QSpinBox()
        self.refresh_interval_spin.setRange(1, 60)
        self.refresh_interval_spin.setValue(5)
        self.refresh_interval_spin.setSuffix(" sec")
        refresh_interval_layout.addWidget(refresh_label)
        refresh_interval_layout.addWidget(self.refresh_interval_spin)
        refresh_interval_layout.addStretch()
        perf_layout.addLayout(refresh_interval_layout)
        
        perf_group.setLayout(perf_layout)
        layout.addWidget(perf_group)
        
        layout.addStretch()
        return tab
    
    def create_view_tab(self):
        """Create view settings tab"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # List view options
        view_group = QGroupBox("List View")
        view_layout = QVBoxLayout()
        
        # View mode
        view_mode_layout = QHBoxLayout()
        view_mode_label = QLabel("View Mode:")
        self.view_mode_combo = QComboBox()
        self.view_mode_combo.addItem("📋 List", "list")
        self.view_mode_combo.addItem("🔲 Icon", "icon")
        view_mode_layout.addWidget(view_mode_label)
        view_mode_layout.addWidget(self.view_mode_combo)
        view_mode_layout.addStretch()
        view_layout.addLayout(view_mode_layout)
        
        # Icon size
        icon_size_layout = QHBoxLayout()
        icon_size_label = QLabel("Icon Size:")
        self.icon_size_slider = QSlider(Qt.Orientation.Horizontal)
        self.icon_size_slider.setRange(16, 128)
        self.icon_size_slider.setValue(32)
        self.icon_size_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.icon_size_slider.setTickInterval(16)
        self.icon_size_value = QLabel("32px")
        self.icon_size_slider.valueChanged.connect(
            lambda v: self.icon_size_value.setText(f"{v}px")
        )
        icon_size_layout.addWidget(icon_size_label)
        icon_size_layout.addWidget(self.icon_size_slider)
        icon_size_layout.addWidget(self.icon_size_value)
        view_layout.addLayout(icon_size_layout)
        
        self.alternating_rows_checkbox = QCheckBox("Alternating row colors")
        self.alternating_rows_checkbox.setChecked(True)
        view_layout.addWidget(self.alternating_rows_checkbox)
        
        view_group.setLayout(view_layout)
        layout.addWidget(view_group)
        
        # Sidebar
        sidebar_group = QGroupBox("Sidebar")
        sidebar_layout = QVBoxLayout()
        
        self.show_sidebar_checkbox = QCheckBox("Show sidebar")
        self.show_sidebar_checkbox.setChecked(True)
        sidebar_layout.addWidget(self.show_sidebar_checkbox)
        
        sidebar_width_layout = QHBoxLayout()
        sidebar_width_label = QLabel("Sidebar Width:")
        self.sidebar_width_spin = QSpinBox()
        self.sidebar_width_spin.setRange(150, 400)
        self.sidebar_width_spin.setValue(250)
        self.sidebar_width_spin.setSuffix(" px")
        sidebar_width_layout.addWidget(sidebar_width_label)
        sidebar_width_layout.addWidget(self.sidebar_width_spin)
        sidebar_width_layout.addStretch()
        sidebar_layout.addLayout(sidebar_width_layout)
        
        sidebar_group.setLayout(sidebar_layout)
        layout.addWidget(sidebar_group)
        
        # Toolbar
        toolbar_group = QGroupBox("Toolbar")
        toolbar_layout = QVBoxLayout()
        
        self.show_toolbar_checkbox = QCheckBox("Show toolbar")
        self.show_toolbar_checkbox.setChecked(True)
        toolbar_layout.addWidget(self.show_toolbar_checkbox)
        
        toolbar_style_layout = QHBoxLayout()
        toolbar_style_label = QLabel("Button Style:")
        self.toolbar_style_combo = QComboBox()
        self.toolbar_style_combo.addItem("Icon + Text", "text_beside_icon")
        self.toolbar_style_combo.addItem("Icon Only", "icon_only")
        self.toolbar_style_combo.addItem("Text Only", "text_only")
        toolbar_style_layout.addWidget(toolbar_style_label)
        toolbar_style_layout.addWidget(self.toolbar_style_combo)
        toolbar_style_layout.addStretch()
        toolbar_layout.addLayout(toolbar_style_layout)
        
        toolbar_group.setLayout(toolbar_layout)
        layout.addWidget(toolbar_group)
        
        layout.addStretch()
        return tab
    
    def create_advanced_tab(self):
        """Create advanced settings tab"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Developer options
        dev_group = QGroupBox("Developer Options")
        dev_layout = QVBoxLayout()
        
        self.debug_mode_checkbox = QCheckBox("Enable debug mode")
        self.debug_mode_checkbox.setChecked(False)
        dev_layout.addWidget(self.debug_mode_checkbox)
        
        self.show_file_extensions_checkbox = QCheckBox("Always show file extensions")
        self.show_file_extensions_checkbox.setChecked(True)
        dev_layout.addWidget(self.show_file_extensions_checkbox)
        
        dev_group.setLayout(dev_layout)
        layout.addWidget(dev_group)
        
        # Experimental
        exp_group = QGroupBox("Experimental Features")
        exp_layout = QVBoxLayout()
        
        self.preview_pane_checkbox = QCheckBox("Enable preview pane (Coming Soon)")
        self.preview_pane_checkbox.setChecked(False)
        self.preview_pane_checkbox.setEnabled(False)
        exp_layout.addWidget(self.preview_pane_checkbox)
        
        self.tabs_checkbox = QCheckBox("Enable tabs (Coming Soon)")
        self.tabs_checkbox.setChecked(False)
        self.tabs_checkbox.setEnabled(False)
        exp_layout.addWidget(self.tabs_checkbox)
        
        exp_group.setLayout(exp_layout)
        layout.addWidget(exp_group)
        
        # About
        about_group = QGroupBox("About")
        about_layout = QVBoxLayout()
        
        about_label = QLabel(
            "✨ <b>Liquid Glass File Explorer</b><br>"
            "Version 1.0.0<br><br>"
            "A modern, beautiful file explorer<br>"
            "with glassmorphism design.<br><br>"
            "Built with PyQt6"
        )
        about_label.setWordWrap(True)
        about_layout.addWidget(about_label)
        
        about_group.setLayout(about_layout)
        layout.addWidget(about_group)
        
        layout.addStretch()
        return tab
    
    def load_current_settings(self):
        """Load current settings into UI"""
        # Theme
        theme = self.current_settings.get('theme', 'liquid_glass')
        index = self.theme_combo.findData(theme)
        if index >= 0:
            self.theme_combo.setCurrentIndex(index)
        
        # Font
        self.font_size_spin.setValue(self.current_settings.get('font_size', 11))
        self.font_family_combo.setCurrentText(self.current_settings.get('font_family', 'Segoe UI'))
        
        # Checkboxes
        self.blur_checkbox.setChecked(self.current_settings.get('blur_enabled', True))
        self.shadow_checkbox.setChecked(self.current_settings.get('shadow_enabled', True))
        self.confirm_delete_checkbox.setChecked(self.current_settings.get('confirm_delete', True))
        self.use_trash_checkbox.setChecked(self.current_settings.get('use_trash', True))
        self.double_click_checkbox.setChecked(self.current_settings.get('double_click_open', True))
        self.show_hidden_checkbox.setChecked(self.current_settings.get('show_hidden', False))
        self.remember_location_checkbox.setChecked(self.current_settings.get('remember_location', True))
        self.auto_refresh_checkbox.setChecked(self.current_settings.get('auto_refresh', True))
        self.alternating_rows_checkbox.setChecked(self.current_settings.get('alternating_rows', True))
        self.show_sidebar_checkbox.setChecked(self.current_settings.get('show_sidebar', True))
        self.show_toolbar_checkbox.setChecked(self.current_settings.get('show_toolbar', True))
        
        # Spinners and sliders
        self.refresh_interval_spin.setValue(self.current_settings.get('refresh_interval', 5))
        self.icon_size_slider.setValue(self.current_settings.get('icon_size', 32))
        self.sidebar_width_spin.setValue(self.current_settings.get('sidebar_width', 250))
        
        # View mode
        view_mode = self.current_settings.get('view_mode', 'list')
        index = self.view_mode_combo.findData(view_mode)
        if index >= 0:
            self.view_mode_combo.setCurrentIndex(index)
        
        # Toolbar style
        toolbar_style = self.current_settings.get('toolbar_style', 'text_beside_icon')
        index = self.toolbar_style_combo.findData(toolbar_style)
        if index >= 0:
            self.toolbar_style_combo.setCurrentIndex(index)
    
    def get_settings(self):
        """Get current settings from UI"""
        return {
            # Appearance
            'theme': self.theme_combo.currentData(),
            'font_size': self.font_size_spin.value(),
            'font_family': self.font_family_combo.currentText(),
            'blur_enabled': self.blur_checkbox.isChecked(),
            'shadow_enabled': self.shadow_checkbox.isChecked(),
            
            # Behavior
            'confirm_delete': self.confirm_delete_checkbox.isChecked(),
            'use_trash': self.use_trash_checkbox.isChecked(),
            'double_click_open': self.double_click_checkbox.isChecked(),
            'show_hidden': self.show_hidden_checkbox.isChecked(),
            'remember_location': self.remember_location_checkbox.isChecked(),
            'auto_refresh': self.auto_refresh_checkbox.isChecked(),
            'refresh_interval': self.refresh_interval_spin.value(),
            
            # View
            'view_mode': self.view_mode_combo.currentData(),
            'icon_size': self.icon_size_slider.value(),
            'alternating_rows': self.alternating_rows_checkbox.isChecked(),
            'show_sidebar': self.show_sidebar_checkbox.isChecked(),
            'sidebar_width': self.sidebar_width_spin.value(),
            'show_toolbar': self.show_toolbar_checkbox.isChecked(),
            'toolbar_style': self.toolbar_style_combo.currentData(),
            
            # Advanced
            'debug_mode': self.debug_mode_checkbox.isChecked(),
            'show_file_extensions': self.show_file_extensions_checkbox.isChecked(),
        }
    
    def apply_settings(self):
        """Apply settings and close dialog"""
        settings = self.get_settings()
        self.settings_changed.emit(settings)
        self.accept()
    
    def reset_to_defaults(self):
        """Reset all settings to defaults"""
        self.current_settings = {}
        self.load_current_settings()
