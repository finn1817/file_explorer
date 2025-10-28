"""
Stylesheet definitions for Liquid Glass File Explorer
All visual styling is centralized here
"""


class LightStyle:
    """Light theme stylesheet"""
    
    @staticmethod
    def get_stylesheet():
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #f5f5f5,
                    stop:1 #e8e8e8);
                color: #333333;
            }
            
            QWidget {
                background: transparent;
                color: #333333;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            
            QToolBar {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ffffff,
                    stop:1 #f0f0f0);
                border: none;
                border-bottom: 1px solid #d0d0d0;
                padding: 5px;
            }
            
            QToolBar QToolButton {
                background: #ffffff;
                border: 1px solid #c0c0c0;
                border-radius: 6px;
                padding: 8px 14px;
                margin: 2px;
                color: #333333;
                font-weight: 500;
            }
            
            QToolBar QToolButton:hover {
                background: #e8f4ff;
                border: 1px solid #0078d4;
                color: #0078d4;
            }
            
            QToolBar QToolButton:pressed {
                background: #d0e8ff;
            }
            
            QLineEdit {
                background: #ffffff;
                border: 1px solid #c0c0c0;
                border-radius: 6px;
                padding: 10px 14px;
                color: #333333;
                font-size: 11pt;
                selection-background-color: #0078d4;
            }
            
            QLineEdit:focus {
                border: 2px solid #0078d4;
            }
            
            QPushButton {
                background: #ffffff;
                border: 1px solid #c0c0c0;
                border-radius: 6px;
                padding: 8px 16px;
                color: #333333;
                font-weight: 500;
            }
            
            QPushButton:hover {
                background: #e8f4ff;
                border: 1px solid #0078d4;
                color: #0078d4;
            }
            
            QPushButton:pressed {
                background: #d0e8ff;
            }
            
            QListView {
                background: #ffffff;
                border: 1px solid #d0d0d0;
                border-radius: 8px;
                padding: 4px;
                alternate-background-color: #f9f9f9;
                selection-background-color: #0078d4;
                outline: none;
            }
            
            QListView::item {
                padding: 10px;
                border-radius: 4px;
                margin: 2px;
            }
            
            QListView::item:hover {
                background: #f0f0f0;
            }
            
            QListView::item:selected {
                background: #0078d4;
                color: white;
            }
            
            QTreeView {
                background: #ffffff;
                border: 1px solid #d0d0d0;
                border-radius: 8px;
                padding: 4px;
                selection-background-color: #0078d4;
                outline: none;
            }
            
            QTreeView::item {
                padding: 6px;
                border-radius: 4px;
            }
            
            QTreeView::item:hover {
                background: #f0f0f0;
            }
            
            QTreeView::item:selected {
                background: #0078d4;
                color: white;
            }
            
            QHeaderView::section {
                background: #f5f5f5;
                border: none;
                border-right: 1px solid #d0d0d0;
                border-bottom: 1px solid #d0d0d0;
                padding: 8px;
                color: #333333;
                font-weight: 600;
            }
            
            QHeaderView::section:hover {
                background: #e8e8e8;
            }
            
            QStatusBar {
                background: #f5f5f5;
                border-top: 1px solid #d0d0d0;
                color: #333333;
                padding: 5px;
            }
            
            QMenu {
                background: #ffffff;
                border: 1px solid #c0c0c0;
                border-radius: 8px;
                padding: 6px;
            }
            
            QMenu::item {
                background: transparent;
                padding: 10px 30px;
                margin: 2px 4px;
                border-radius: 6px;
                color: #333333;
            }
            
            QMenu::item:selected {
                background: #e8f4ff;
                color: #0078d4;
            }
            
            QMenu::separator {
                height: 1px;
                background: #d0d0d0;
                margin: 4px 8px;
            }
            
            QScrollBar:vertical {
                background: #f5f5f5;
                width: 12px;
                border-radius: 6px;
                margin: 0px;
            }
            
            QScrollBar::handle:vertical {
                background: #c0c0c0;
                border-radius: 6px;
                min-height: 30px;
            }
            
            QScrollBar::handle:vertical:hover {
                background: #a0a0a0;
            }
            
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            
            QScrollBar:horizontal {
                background: #f5f5f5;
                height: 12px;
                border-radius: 6px;
                margin: 0px;
            }
            
            QScrollBar::handle:horizontal {
                background: #c0c0c0;
                border-radius: 6px;
                min-width: 30px;
            }
            
            QScrollBar::handle:horizontal:hover {
                background: #a0a0a0;
            }
            
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                width: 0px;
            }
            
            QSplitter::handle {
                background: #d0d0d0;
                width: 2px;
            }
            
            QSplitter::handle:hover {
                background: #0078d4;
            }
            
            QLabel {
                color: #333333;
            }
            
            QCheckBox {
                color: #333333;
                spacing: 8px;
                padding: 4px;
            }
            
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #c0c0c0;
                border-radius: 4px;
                background: #ffffff;
            }
            
            QCheckBox::indicator:hover {
                border: 2px solid #0078d4;
                background: #e8f4ff;
            }
            
            QCheckBox::indicator:checked {
                background: #0078d4;
                border: 2px solid #0078d4;
                image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEzLjMzMzMgNEw2IDExLjMzMzNMMi42NjY2NyA4IiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPgo8L3N2Zz4K);
            }
            
            QCheckBox::indicator:checked:hover {
                background: #005a9e;
            }
            
            QCheckBox:disabled {
                color: #888888;
            }
            
            QCheckBox::indicator:disabled {
                border: 2px solid #d0d0d0;
                background: #f5f5f5;
            }
            
            QGroupBox {
                border: 1px solid #d0d0d0;
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 16px;
                font-weight: 500;
                color: #333333;
            }
            
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 12px;
                padding: 0 8px;
                background: #f5f5f5;
            }
            
            QComboBox {
                background: #ffffff;
                border: 1px solid #c0c0c0;
                border-radius: 6px;
                padding: 8px 12px;
                color: #333333;
                min-width: 120px;
            }
            
            QComboBox:hover {
                border: 1px solid #0078d4;
            }
            
            QComboBox::drop-down {
                border: none;
                width: 24px;
            }
            
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #666666;
                width: 0;
                height: 0;
            }
            
            QSpinBox {
                background: #ffffff;
                border: 1px solid #c0c0c0;
                border-radius: 6px;
                padding: 8px 12px;
                color: #333333;
            }
            
            QSpinBox:hover {
                border: 1px solid #0078d4;
            }
            
            QSpinBox::up-button, QSpinBox::down-button {
                background: #f0f0f0;
                border: none;
                width: 20px;
            }
            
            QSpinBox::up-button:hover, QSpinBox::down-button:hover {
                background: #e0e0e0;
            }
            
            QSlider::groove:horizontal {
                background: #d0d0d0;
                height: 6px;
                border-radius: 3px;
            }
            
            QSlider::handle:horizontal {
                background: #0078d4;
                width: 18px;
                height: 18px;
                margin: -6px 0;
                border-radius: 9px;
            }
            
            QSlider::handle:horizontal:hover {
                background: #005a9e;
            }
            
            QTabWidget::pane {
                border: 1px solid #d0d0d0;
                border-radius: 8px;
                background: #ffffff;
                padding: 8px;
            }
            
            QTabBar::tab {
                background: #f0f0f0;
                color: #666666;
                padding: 10px 20px;
                margin-right: 4px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
            }
            
            QTabBar::tab:selected {
                background: #ffffff;
                color: #0078d4;
                border-bottom: 2px solid #0078d4;
            }
            
            QTabBar::tab:hover:!selected {
                background: #e8e8e8;
            }
        """


class DarkStyle:
    """Dark theme stylesheet"""
    
    @staticmethod
    def get_stylesheet():
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1e1e1e,
                    stop:1 #2d2d2d);
                color: #e0e0e0;
            }
            
            QWidget {
                background: transparent;
                color: #e0e0e0;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            
            QToolBar {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2d2d2d,
                    stop:1 #252525);
                border: none;
                border-bottom: 1px solid #404040;
                padding: 5px;
            }
            
            QToolBar QToolButton {
                background: #3a3a3a;
                border: 1px solid #505050;
                border-radius: 6px;
                padding: 8px 14px;
                margin: 2px;
                color: #e0e0e0;
                font-weight: 500;
            }
            
            QToolBar QToolButton:hover {
                background: #4a4a4a;
                border: 1px solid #0078d4;
                color: #4cc2ff;
            }
            
            QToolBar QToolButton:pressed {
                background: #2a2a2a;
            }
            
            QLineEdit {
                background: #2d2d2d;
                border: 1px solid #505050;
                border-radius: 6px;
                padding: 10px 14px;
                color: #e0e0e0;
                font-size: 11pt;
                selection-background-color: #0078d4;
            }
            
            QLineEdit:focus {
                border: 2px solid #0078d4;
            }
            
            QPushButton {
                background: #3a3a3a;
                border: 1px solid #505050;
                border-radius: 6px;
                padding: 8px 16px;
                color: #e0e0e0;
                font-weight: 500;
            }
            
            QPushButton:hover {
                background: #4a4a4a;
                border: 1px solid #0078d4;
                color: #4cc2ff;
            }
            
            QPushButton:pressed {
                background: #2a2a2a;
            }
            
            QListView {
                background: #252525;
                border: 1px solid #404040;
                border-radius: 8px;
                padding: 4px;
                alternate-background-color: #2a2a2a;
                selection-background-color: #0078d4;
                outline: none;
            }
            
            QListView::item {
                padding: 10px;
                border-radius: 4px;
                margin: 2px;
            }
            
            QListView::item:hover {
                background: #3a3a3a;
            }
            
            QListView::item:selected {
                background: #0078d4;
                color: white;
            }
            
            QTreeView {
                background: #252525;
                border: 1px solid #404040;
                border-radius: 8px;
                padding: 4px;
                selection-background-color: #0078d4;
                outline: none;
            }
            
            QTreeView::item {
                padding: 6px;
                border-radius: 4px;
            }
            
            QTreeView::item:hover {
                background: #3a3a3a;
            }
            
            QTreeView::item:selected {
                background: #0078d4;
                color: white;
            }
            
            QHeaderView::section {
                background: #2d2d2d;
                border: none;
                border-right: 1px solid #404040;
                border-bottom: 1px solid #404040;
                padding: 8px;
                color: #e0e0e0;
                font-weight: 600;
            }
            
            QHeaderView::section:hover {
                background: #3a3a3a;
            }
            
            QStatusBar {
                background: #2d2d2d;
                border-top: 1px solid #404040;
                color: #e0e0e0;
                padding: 5px;
            }
            
            QMenu {
                background: #2d2d2d;
                border: 1px solid #505050;
                border-radius: 8px;
                padding: 6px;
            }
            
            QMenu::item {
                background: transparent;
                padding: 10px 30px;
                margin: 2px 4px;
                border-radius: 6px;
                color: #e0e0e0;
            }
            
            QMenu::item:selected {
                background: #0078d4;
                color: white;
            }
            
            QMenu::separator {
                height: 1px;
                background: #505050;
                margin: 4px 8px;
            }
            
            QScrollBar:vertical {
                background: #1e1e1e;
                width: 12px;
                border-radius: 6px;
                margin: 0px;
            }
            
            QScrollBar::handle:vertical {
                background: #505050;
                border-radius: 6px;
                min-height: 30px;
            }
            
            QScrollBar::handle:vertical:hover {
                background: #606060;
            }
            
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            
            QScrollBar:horizontal {
                background: #1e1e1e;
                height: 12px;
                border-radius: 6px;
                margin: 0px;
            }
            
            QScrollBar::handle:horizontal {
                background: #505050;
                border-radius: 6px;
                min-width: 30px;
            }
            
            QScrollBar::handle:horizontal:hover {
                background: #606060;
            }
            
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                width: 0px;
            }
            
            QSplitter::handle {
                background: #404040;
                width: 2px;
            }
            
            QSplitter::handle:hover {
                background: #0078d4;
            }
            
            QLabel {
                color: #e0e0e0;
            }
            
            QCheckBox {
                color: #e0e0e0;
                spacing: 8px;
                padding: 4px;
            }
            
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #505050;
                border-radius: 4px;
                background: #2a2a2a;
            }
            
            QCheckBox::indicator:hover {
                border: 2px solid #0078d4;
                background: #3a3a3a;
            }
            
            QCheckBox::indicator:checked {
                background: #0078d4;
                border: 2px solid #0078d4;
                image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEzLjMzMzMgNEw2IDExLjMzMzNMMi42NjY2NyA4IiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPgo8L3N2Zz4K);
            }
            
            QCheckBox::indicator:checked:hover {
                background: #005a9e;
            }
            
            QCheckBox:disabled {
                color: #666666;
            }
            
            QCheckBox::indicator:disabled {
                border: 2px solid #404040;
                background: #1e1e1e;
            }
            
            QGroupBox {
                border: 1px solid #404040;
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 16px;
                font-weight: 500;
                color: #e0e0e0;
            }
            
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 12px;
                padding: 0 8px;
                background: #1e1e1e;
            }
            
            QComboBox {
                background: #2a2a2a;
                border: 1px solid #505050;
                border-radius: 6px;
                padding: 8px 12px;
                color: #e0e0e0;
                min-width: 120px;
            }
            
            QComboBox:hover {
                border: 1px solid #0078d4;
            }
            
            QComboBox::drop-down {
                border: none;
                width: 24px;
            }
            
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #aaaaaa;
                width: 0;
                height: 0;
            }
            
            QSpinBox {
                background: #2a2a2a;
                border: 1px solid #505050;
                border-radius: 6px;
                padding: 8px 12px;
                color: #e0e0e0;
            }
            
            QSpinBox:hover {
                border: 1px solid #0078d4;
            }
            
            QSpinBox::up-button, QSpinBox::down-button {
                background: #3a3a3a;
                border: none;
                width: 20px;
            }
            
            QSpinBox::up-button:hover, QSpinBox::down-button:hover {
                background: #4a4a4a;
            }
            
            QSlider::groove:horizontal {
                background: #3a3a3a;
                height: 6px;
                border-radius: 3px;
            }
            
            QSlider::handle:horizontal {
                background: #0078d4;
                width: 18px;
                height: 18px;
                margin: -6px 0;
                border-radius: 9px;
            }
            
            QSlider::handle:horizontal:hover {
                background: #005a9e;
            }
            
            QTabWidget::pane {
                border: 1px solid #404040;
                border-radius: 8px;
                background: #2a2a2a;
                padding: 8px;
            }
            
            QTabBar::tab {
                background: #3a3a3a;
                color: #aaaaaa;
                padding: 10px 20px;
                margin-right: 4px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
            }
            
            QTabBar::tab:selected {
                background: #2a2a2a;
                color: #4cc2ff;
                border-bottom: 2px solid #0078d4;
            }
            
            QTabBar::tab:hover:!selected {
                background: #454545;
            }
        """


class LiquidGlassStyle:
    """Liquid Glass theme stylesheet with glassmorphism effects"""
    
    @staticmethod
    def get_stylesheet():
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(20, 25, 45, 0.98),
                    stop:0.3 rgba(35, 45, 75, 0.98),
                    stop:0.6 rgba(45, 35, 70, 0.98),
                    stop:1 rgba(25, 30, 50, 0.98));
                color: white;
            }
            
            QWidget {
                background: transparent;
                color: rgba(255, 255, 255, 0.95);
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            
            QToolBar {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.15),
                    stop:1 rgba(255, 255, 255, 0.08));
                border: none;
                border-bottom: 1px solid rgba(255, 255, 255, 0.25);
                border-top: 1px solid rgba(255, 255, 255, 0.1);
                padding: 5px;
            }
            
            QToolBar QToolButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.12),
                    stop:1 rgba(255, 255, 255, 0.06));
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 8px;
                padding: 8px 14px;
                margin: 2px;
                color: rgba(255, 255, 255, 0.95);
                font-weight: 500;
            }
            
            QToolBar QToolButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.25),
                    stop:1 rgba(255, 255, 255, 0.15));
                border: 1px solid rgba(255, 255, 255, 0.4);
                color: white;
            }
            
            QToolBar QToolButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.18),
                    stop:1 rgba(255, 255, 255, 0.28));
            }
            
            QLineEdit {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.15),
                    stop:1 rgba(255, 255, 255, 0.08));
                border: 1px solid rgba(255, 255, 255, 0.25);
                border-radius: 8px;
                padding: 10px 14px;
                color: white;
                font-size: 11pt;
                selection-background-color: rgba(120, 170, 255, 0.5);
            }
            
            QLineEdit:focus {
                border: 1px solid rgba(120, 170, 255, 0.8);
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.2),
                    stop:1 rgba(255, 255, 255, 0.12));
            }
            
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.12),
                    stop:1 rgba(255, 255, 255, 0.06));
                border: 1px solid rgba(255, 255, 255, 0.25);
                border-radius: 8px;
                padding: 8px 16px;
                color: rgba(255, 255, 255, 0.95);
                font-weight: 500;
            }
            
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.22),
                    stop:1 rgba(255, 255, 255, 0.14));
                border: 1px solid rgba(255, 255, 255, 0.45);
                color: white;
            }
            
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.15),
                    stop:1 rgba(255, 255, 255, 0.25));
            }
            
            QListView {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.08),
                    stop:1 rgba(255, 255, 255, 0.03));
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 10px;
                padding: 4px;
                alternate-background-color: rgba(255, 255, 255, 0.03);
                selection-background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(100, 150, 255, 0.4),
                    stop:1 rgba(120, 170, 255, 0.35));
                outline: none;
            }
            
            QListView::item {
                padding: 10px;
                border-radius: 6px;
                margin: 2px;
            }
            
            QListView::item:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(255, 255, 255, 0.12),
                    stop:1 rgba(255, 255, 255, 0.08));
                border: 1px solid rgba(255, 255, 255, 0.2);
            }
            
            QListView::item:selected {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(100, 150, 255, 0.5),
                    stop:1 rgba(120, 170, 255, 0.4));
                border: 1px solid rgba(120, 170, 255, 0.7);
                color: white;
            }
            
            QTreeView {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.08),
                    stop:1 rgba(255, 255, 255, 0.03));
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 10px;
                padding: 4px;
                selection-background-color: rgba(100, 150, 255, 0.4);
                outline: none;
            }
            
            QTreeView::item {
                padding: 6px;
                border-radius: 4px;
            }
            
            QTreeView::item:hover {
                background: rgba(255, 255, 255, 0.1);
            }
            
            QTreeView::item:selected {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(100, 150, 255, 0.5),
                    stop:1 rgba(120, 170, 255, 0.4));
                border: 1px solid rgba(120, 170, 255, 0.6);
            }
            
            QHeaderView::section {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.15),
                    stop:1 rgba(255, 255, 255, 0.08));
                border: none;
                border-right: 1px solid rgba(255, 255, 255, 0.1);
                border-bottom: 1px solid rgba(255, 255, 255, 0.2);
                padding: 8px;
                color: rgba(255, 255, 255, 0.9);
                font-weight: 600;
            }
            
            QHeaderView::section:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.22),
                    stop:1 rgba(255, 255, 255, 0.14));
            }
            
            QStatusBar {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.08),
                    stop:1 rgba(255, 255, 255, 0.15));
                border-top: 1px solid rgba(255, 255, 255, 0.25);
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                color: rgba(255, 255, 255, 0.9);
                padding: 5px;
            }
            
            QMenu {
                background: rgba(30, 35, 55, 0.97);
                border: 1px solid rgba(255, 255, 255, 0.25);
                border-radius: 10px;
                padding: 6px;
            }
            
            QMenu::item {
                background: transparent;
                padding: 10px 30px;
                margin: 2px 4px;
                border-radius: 6px;
                color: rgba(255, 255, 255, 0.95);
            }
            
            QMenu::item:selected {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(100, 150, 255, 0.4),
                    stop:1 rgba(120, 170, 255, 0.3));
                color: white;
            }
            
            QMenu::separator {
                height: 1px;
                background: rgba(255, 255, 255, 0.15);
                margin: 4px 8px;
            }
            
            QScrollBar:vertical {
                background: rgba(255, 255, 255, 0.05);
                width: 12px;
                border-radius: 6px;
                margin: 0px;
            }
            
            QScrollBar::handle:vertical {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(255, 255, 255, 0.25),
                    stop:1 rgba(255, 255, 255, 0.15));
                border-radius: 6px;
                min-height: 30px;
            }
            
            QScrollBar::handle:vertical:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(255, 255, 255, 0.35),
                    stop:1 rgba(255, 255, 255, 0.25));
            }
            
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            
            QScrollBar:horizontal {
                background: rgba(255, 255, 255, 0.05);
                height: 12px;
                border-radius: 6px;
                margin: 0px;
            }
            
            QScrollBar::handle:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.25),
                    stop:1 rgba(255, 255, 255, 0.15));
                border-radius: 6px;
                min-width: 30px;
            }
            
            QScrollBar::handle:horizontal:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.35),
                    stop:1 rgba(255, 255, 255, 0.25));
            }
            
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                width: 0px;
            }
            
            QSplitter::handle {
                background: rgba(255, 255, 255, 0.15);
                width: 2px;
            }
            
            QSplitter::handle:hover {
                background: rgba(255, 255, 255, 0.3);
            }
            
            QLabel {
                color: rgba(255, 255, 255, 0.95);
            }
            
            QMessageBox {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(30, 35, 55, 0.98),
                    stop:1 rgba(40, 45, 65, 0.98));
            }
            
            QInputDialog {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(30, 35, 55, 0.98),
                    stop:1 rgba(40, 45, 65, 0.98));
            }
            
            QCheckBox {
                color: rgba(255, 255, 255, 0.95);
                spacing: 8px;
                padding: 4px;
            }
            
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid rgba(255, 255, 255, 0.3);
                border-radius: 6px;
                background: rgba(255, 255, 255, 0.08);
            }
            
            QCheckBox::indicator:hover {
                border: 2px solid rgba(100, 200, 255, 0.8);
                background: rgba(100, 200, 255, 0.15);
            }
            
            QCheckBox::indicator:checked {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(100, 200, 255, 0.8),
                    stop:1 rgba(50, 150, 255, 0.9));
                border: 2px solid rgba(100, 200, 255, 0.9);
                image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEzLjMzMzMgNEw2IDExLjMzMzNMMi42NjY2NyA4IiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPgo8L3N2Zz4K);
            }
            
            QCheckBox::indicator:checked:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(120, 210, 255, 0.9),
                    stop:1 rgba(70, 170, 255, 1.0));
            }
            
            QCheckBox:disabled {
                color: rgba(255, 255, 255, 0.3);
            }
            
            QCheckBox::indicator:disabled {
                border: 2px solid rgba(255, 255, 255, 0.15);
                background: rgba(255, 255, 255, 0.05);
            }
            
            QGroupBox {
                border: 2px solid rgba(255, 255, 255, 0.2);
                border-radius: 12px;
                margin-top: 14px;
                padding-top: 18px;
                font-weight: 600;
                color: rgba(255, 255, 255, 0.95);
                background: rgba(255, 255, 255, 0.03);
            }
            
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 16px;
                padding: 0 10px;
                background: rgba(30, 35, 55, 0.8);
                border-radius: 4px;
            }
            
            QComboBox {
                background: rgba(255, 255, 255, 0.08);
                border: 2px solid rgba(255, 255, 255, 0.2);
                border-radius: 8px;
                padding: 8px 12px;
                color: rgba(255, 255, 255, 0.95);
                min-width: 120px;
            }
            
            QComboBox:hover {
                border: 2px solid rgba(100, 200, 255, 0.6);
                background: rgba(100, 200, 255, 0.12);
            }
            
            QComboBox::drop-down {
                border: none;
                width: 28px;
            }
            
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 6px solid rgba(255, 255, 255, 0.7);
                width: 0;
                height: 0;
            }
            
            QComboBox QAbstractItemView {
                background: rgba(30, 35, 55, 0.95);
                border: 2px solid rgba(100, 200, 255, 0.4);
                border-radius: 8px;
                selection-background-color: rgba(100, 200, 255, 0.3);
                color: rgba(255, 255, 255, 0.95);
                padding: 4px;
            }
            
            QSpinBox {
                background: rgba(255, 255, 255, 0.08);
                border: 2px solid rgba(255, 255, 255, 0.2);
                border-radius: 8px;
                padding: 8px 12px;
                color: rgba(255, 255, 255, 0.95);
            }
            
            QSpinBox:hover {
                border: 2px solid rgba(100, 200, 255, 0.6);
                background: rgba(100, 200, 255, 0.12);
            }
            
            QSpinBox::up-button, QSpinBox::down-button {
                background: rgba(255, 255, 255, 0.1);
                border: none;
                width: 24px;
                border-radius: 4px;
            }
            
            QSpinBox::up-button:hover, QSpinBox::down-button:hover {
                background: rgba(100, 200, 255, 0.3);
            }
            
            QSlider::groove:horizontal {
                background: rgba(255, 255, 255, 0.15);
                height: 8px;
                border-radius: 4px;
            }
            
            QSlider::handle:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(100, 200, 255, 0.9),
                    stop:1 rgba(50, 150, 255, 1.0));
                width: 20px;
                height: 20px;
                margin: -6px 0;
                border-radius: 10px;
                border: 2px solid rgba(255, 255, 255, 0.3);
            }
            
            QSlider::handle:horizontal:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(120, 210, 255, 1.0),
                    stop:1 rgba(70, 170, 255, 1.0));
                border: 2px solid rgba(255, 255, 255, 0.5);
            }
            
            QTabWidget::pane {
                border: 2px solid rgba(255, 255, 255, 0.15);
                border-radius: 12px;
                background: rgba(255, 255, 255, 0.03);
                padding: 12px;
            }
            
            QTabBar::tab {
                background: rgba(255, 255, 255, 0.05);
                color: rgba(255, 255, 255, 0.6);
                padding: 12px 24px;
                margin-right: 4px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                border: 2px solid transparent;
            }
            
            QTabBar::tab:selected {
                background: rgba(100, 200, 255, 0.15);
                color: rgba(255, 255, 255, 0.95);
                border: 2px solid rgba(100, 200, 255, 0.4);
                border-bottom: none;
            }
            
            QTabBar::tab:hover:!selected {
                background: rgba(255, 255, 255, 0.08);
                color: rgba(255, 255, 255, 0.8);
            }
            
            QDialog {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(30, 35, 55, 0.97),
                    stop:1 rgba(40, 45, 65, 0.97));
            }
        """
