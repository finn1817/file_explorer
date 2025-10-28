import os
import shutil
import subprocess
import platform
import json
import logging
from datetime import datetime
from pathlib import Path
from PyQt6.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, 
                            QTreeView, QListView, QLineEdit, QPushButton, 
                            QSplitter, QLabel, QMessageBox, QInputDialog,
                            QMenu, QToolBar, QStatusBar,
                            QAbstractItemView, QHeaderView, QScrollArea)
from PyQt6.QtCore import (Qt, QDir, QModelIndex, QTimer, pyqtSignal, 
                         QSortFilterProxyModel, QThread, pyqtSlot, QSize)
from PyQt6.QtGui import (QAction, QKeySequence, QFont, QPixmap, QPalette, 
                        QBrush, QColor, QIcon, QFileSystemModel)
from PyQt6.QtWidgets import QGraphicsBlurEffect, QGraphicsDropShadowEffect
from send2trash import send2trash
from file_operations import FileOperations
from theme import ThemeManager
from settings_dialog import SettingsDialog
from data_manager import DataManager

# Setup logging - save to log directory
log_dir = Path(__file__).parent.parent / 'log'
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / 'file_explorer.log'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class LiquidGlassFileExplorer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file_ops = FileOperations()
        self.theme_manager = ThemeManager()
        self.data_manager = DataManager()  # New data manager
        
        self.current_path = str(Path.home())
        self.clipboard_path = None
        self.clipboard_operation = None  # 'cut' or 'copy'
        
        # Favorites list - now managed by data_manager
        self.favorites = []
        self.load_favorites()
        
        # User settings with defaults
        self.settings = {
            'theme': 'liquid_glass',
            'font_size': 11,
            'font_family': 'Segoe UI',
            'view_mode': 'list',
            'show_hidden': False,
            'confirm_delete': True,
            'blur_enabled': True,
            'shadow_enabled': True,
            'use_trash': True,
            'double_click_open': True,
            'remember_location': True,
            'auto_refresh': True,
            'refresh_interval': 5,
            'icon_size': 32,
            'alternating_rows': True,
            'show_sidebar': True,
            'sidebar_width': 250,
            'show_toolbar': True,
            'toolbar_style': 'text_beside_icon'
        }
        
        self.init_ui()
        self.apply_current_theme()
        self.connect_signals()
        self.navigate_to_path(self.current_path)

    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("✨ Liquid Glass File Explorer")
        self.setGeometry(100, 100, 1200, 800)
        
        # Enable translucent background for better glass effect (optional)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Add subtle shadow effect to central widget
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setColor(QColor(0, 0, 0, 80))
        shadow.setOffset(0, 0)
        central_widget.setGraphicsEffect(shadow)
        
        # Create main layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(8, 8, 8, 8)
        main_layout.setSpacing(8)
        
        # Create splitter for sidebar and main area
        splitter = QSplitter(Qt.Orientation.Horizontal)
        main_layout.addWidget(splitter)
        
        # Create sidebar
        self.create_sidebar(splitter)
        
        # Create main content area
        self.create_main_area(splitter)
        
        # Set splitter proportions
        splitter.setSizes([250, 950])
        
        # Create toolbar
        self.create_toolbar()
        
        # Create status bar
        self.create_status_bar()
        
        # Setup file system model
        self.setup_file_model()

    def create_sidebar(self, parent):
        """Create the sidebar with quick access"""
        sidebar = QWidget()
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(10, 10, 10, 10)
        
        # Quick Access label
        quick_label = QLabel("✨ Quick Access")
        quick_label.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        quick_label.setStyleSheet("""
            QLabel {
                padding: 10px;
                border-radius: 8px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(255, 255, 255, 0.12),
                    stop:1 rgba(255, 255, 255, 0.06));
                border: 1px solid rgba(255, 255, 255, 0.15);
                color: white;
            }
        """)
        sidebar_layout.addWidget(quick_label)
        
        # Add spacing after label
        sidebar_layout.addSpacing(10)
        
        # Quick access buttons
        quick_folders = [
            ("🖥️ Desktop", str(Path.home() / "Desktop")),
            ("📄 Documents", str(Path.home() / "Documents")),
            ("⬇️ Downloads", str(Path.home() / "Downloads")),
            ("🖼️ Pictures", str(Path.home() / "Pictures")),
            ("🎥 Videos", str(Path.home() / "Videos")),
            ("🎵 Music", str(Path.home() / "Music")),
        ]
        
        for name, path in quick_folders:
            if os.path.exists(path):
                btn = QPushButton(name)
                btn.setStyleSheet("""
                    QPushButton {
                        text-align: left;
                        padding: 10px 14px;
                        border: 1px solid rgba(255, 255, 255, 0.12);
                        border-radius: 8px;
                        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                            stop:0 rgba(255, 255, 255, 0.08),
                            stop:1 rgba(255, 255, 255, 0.04));
                        color: rgba(255, 255, 255, 0.95);
                        font-size: 10pt;
                        font-weight: 500;
                    }
                    QPushButton:hover {
                        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                            stop:0 rgba(255, 255, 255, 0.18),
                            stop:1 rgba(255, 255, 255, 0.12));
                        border: 1px solid rgba(255, 255, 255, 0.25);
                        color: white;
                    }
                    QPushButton:pressed {
                        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                            stop:0 rgba(255, 255, 255, 0.12),
                            stop:1 rgba(255, 255, 255, 0.20));
                    }
                """)
                btn.clicked.connect(lambda checked, p=path: self.navigate_to_path(p))
                sidebar_layout.addWidget(btn)
        
        # Add spacing before favorites
        sidebar_layout.addSpacing(20)
        
        # Favorites section
        favorites_label = QLabel("⭐ Favorites")
        favorites_label.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        favorites_label.setStyleSheet("""
            QLabel {
                padding: 10px;
                border-radius: 8px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(255, 200, 100, 0.15),
                    stop:1 rgba(255, 150, 50, 0.10));
                border: 1px solid rgba(255, 200, 100, 0.25);
                color: white;
            }
        """)
        sidebar_layout.addWidget(favorites_label)
        
        # Create scrollable area for favorites with custom styling
        self.favorites_scroll = QScrollArea()
        self.favorites_scroll.setWidgetResizable(True)
        self.favorites_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.favorites_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.favorites_scroll.setFrameShape(QScrollArea.Shape.NoFrame)
        
        # Style the scroll area with liquid glass theme
        self.favorites_scroll.setStyleSheet("""
            QScrollArea {
                background: transparent;
                border: none;
            }
            QScrollBar:vertical {
                background: rgba(255, 255, 255, 0.08);
                width: 12px;
                border-radius: 6px;
                margin: 2px;
            }
            QScrollBar::handle:vertical {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(255, 200, 100, 0.5),
                    stop:1 rgba(255, 150, 50, 0.4));
                border-radius: 6px;
                min-height: 30px;
                border: 1px solid rgba(255, 200, 100, 0.2);
            }
            QScrollBar::handle:vertical:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(255, 200, 100, 0.7),
                    stop:1 rgba(255, 150, 50, 0.6));
                border: 1px solid rgba(255, 200, 100, 0.4);
            }
            QScrollBar::handle:vertical:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(255, 200, 100, 0.9),
                    stop:1 rgba(255, 150, 50, 0.8));
                border: 1px solid rgba(255, 200, 100, 0.6);
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        
        # Favorites container widget (goes inside scroll area)
        self.favorites_container = QWidget()
        self.favorites_container.setStyleSheet("background: transparent;")
        self.favorites_layout = QVBoxLayout(self.favorites_container)
        self.favorites_layout.setContentsMargins(0, 5, 5, 5)  # Add margins for scrollbar
        self.favorites_layout.setSpacing(5)
        self.favorites_layout.addStretch()  # Add stretch at the bottom to push items to top
        
        # Set the container as the scroll area's widget
        self.favorites_scroll.setWidget(self.favorites_container)
        
        # Set minimum and maximum height for scroll area
        self.favorites_scroll.setMinimumHeight(100)  # Minimum height
        # No maximum height - let it expand with stretch factor
        
        # Add scroll area to sidebar (with stretch factor to allow it to grow)
        sidebar_layout.addWidget(self.favorites_scroll, 1)  # Stretch factor = 1 means it will expand
        
        # Populate favorites
        self.update_favorites_list()
        parent.addWidget(sidebar)

    def create_main_area(self, parent):
        """Create the main file viewing area"""
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Address bar
        address_layout = QHBoxLayout()
        address_layout.setContentsMargins(10, 5, 10, 5)
        
        self.back_btn = QPushButton("← Back")
        self.back_btn.setToolTip("Go back to parent directory (Alt+Left)")
        self.back_btn.setShortcut("Alt+Left")
        
        self.forward_btn = QPushButton("→ Forward")
        self.forward_btn.setToolTip("Go forward (Alt+Right)")
        self.forward_btn.setShortcut("Alt+Right")
        
        self.up_btn = QPushButton("↑ Up")
        self.up_btn.setToolTip("Go to parent folder (Alt+Up)")
        self.up_btn.setShortcut("Alt+Up")
        
        self.refresh_btn = QPushButton("🔄 Refresh")
        self.refresh_btn.setToolTip("Refresh current folder (F5)")
        self.refresh_btn.setShortcut("F5")
        
        self.address_bar = QLineEdit()
        self.address_bar.setPlaceholderText("Enter path...")
        self.address_bar.setToolTip("Enter a path and press Enter to navigate")
        
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search files...")
        self.search_bar.setMaximumWidth(250)
        self.search_bar.setToolTip("Search for files in the current folder")
        
        address_layout.addWidget(self.back_btn)
        address_layout.addWidget(self.forward_btn)
        address_layout.addWidget(self.up_btn)
        address_layout.addWidget(self.refresh_btn)
        address_layout.addWidget(QLabel("📁"))
        address_layout.addWidget(self.address_bar)
        address_layout.addWidget(QLabel("🔍"))
        address_layout.addWidget(self.search_bar)
        
        main_layout.addLayout(address_layout)
        
        # File list view
        self.file_list = QListView()
        self.file_list.setViewMode(QListView.ViewMode.ListMode)
        self.file_list.setAlternatingRowColors(True)
        self.file_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        main_layout.addWidget(self.file_list)
        
        parent.addWidget(main_widget)

    def create_toolbar(self):
        """Create the toolbar with file operations"""
        toolbar = QToolBar()
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.addToolBar(toolbar)
        
        # File operations
        new_folder_action = QAction("📁 New Folder", self)
        new_folder_action.setShortcut(QKeySequence("Ctrl+Shift+N"))
        new_folder_action.setToolTip("Create a new folder (Ctrl+Shift+N)")
        new_folder_action.triggered.connect(self.create_new_folder)
        toolbar.addAction(new_folder_action)
        
        toolbar.addSeparator()
        
        copy_action = QAction("📋 Copy", self)
        copy_action.setShortcut(QKeySequence.StandardKey.Copy)
        copy_action.setToolTip("Copy selected items (Ctrl+C)")
        copy_action.triggered.connect(self.copy_selected)
        toolbar.addAction(copy_action)
        
        cut_action = QAction("✂️ Cut", self)
        cut_action.setShortcut(QKeySequence.StandardKey.Cut)
        cut_action.setToolTip("Cut selected items (Ctrl+X)")
        cut_action.triggered.connect(self.cut_selected)
        toolbar.addAction(cut_action)
        
        paste_action = QAction("📌 Paste", self)
        paste_action.setShortcut(QKeySequence.StandardKey.Paste)
        paste_action.setToolTip("Paste items (Ctrl+V)")
        paste_action.triggered.connect(self.paste_items)
        toolbar.addAction(paste_action)
        
        toolbar.addSeparator()
        
        rename_action = QAction("✏️ Rename", self)
        rename_action.setShortcut(QKeySequence("F2"))
        rename_action.setToolTip("Rename selected item (F2)")
        rename_action.triggered.connect(self.rename_selected)
        toolbar.addAction(rename_action)
        
        delete_action = QAction("🗑️ Delete", self)
        delete_action.setShortcut(QKeySequence.StandardKey.Delete)
        delete_action.setToolTip("Delete selected items (Delete)")
        delete_action.triggered.connect(self.delete_selected)
        toolbar.addAction(delete_action)
        
        toolbar.addSeparator()
        
        # Add to favorites button
        add_fav_action = QAction("⭐ Add to Favorites", self)
        add_fav_action.setShortcut(QKeySequence("Ctrl+D"))
        add_fav_action.setToolTip("Add selected item to favorites (Ctrl+D)")
        add_fav_action.triggered.connect(lambda: self.add_to_favorites())
        toolbar.addAction(add_fav_action)
        
        toolbar.addSeparator()
        
        # Open in CMD button
        cmd_action = QAction("💻 Open in CMD", self)
        cmd_action.setShortcut(QKeySequence("Ctrl+Shift+C"))
        cmd_action.setToolTip("Open Command Prompt in current location (Ctrl+Shift+C)")
        cmd_action.triggered.connect(self.open_in_cmd)
        toolbar.addAction(cmd_action)
        
        # Open in VS Code button
        vscode_action = QAction("📝 Open in VS Code", self)
        vscode_action.setShortcut(QKeySequence("Ctrl+Shift+V"))
        vscode_action.setToolTip("Open current folder in VS Code (Ctrl+Shift+V)")
        vscode_action.triggered.connect(self.open_in_vscode)
        toolbar.addAction(vscode_action)
        
        toolbar.addSeparator()
        
        # Settings button
        settings_action = QAction("⚙️ Settings", self)
        settings_action.setShortcut(QKeySequence("Ctrl+,"))
        settings_action.setToolTip("Open settings (Ctrl+,)")
        settings_action.triggered.connect(self.show_settings_dialog)
        toolbar.addAction(settings_action)

    def create_status_bar(self):
        """Create the status bar"""
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")

    def setup_file_model(self):
        """Setup the file system model"""
        self.file_model = QFileSystemModel()
        self.file_model.setRootPath("")
        
        # Create proxy model for filtering
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.file_model)
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        
        self.file_list.setModel(self.proxy_model)

    def connect_signals(self):
        """Connect all signals"""
        self.back_btn.clicked.connect(self.go_back)
        self.forward_btn.clicked.connect(self.go_forward)
        self.up_btn.clicked.connect(self.go_up)
        self.refresh_btn.clicked.connect(self.refresh_current)
        self.address_bar.returnPressed.connect(self.navigate_from_address_bar)
        self.search_bar.textChanged.connect(self.filter_files)
        self.file_list.doubleClicked.connect(self.open_item)
        self.file_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.file_list.customContextMenuRequested.connect(self.show_context_menu)

    def apply_current_theme(self):
        """Apply the current theme from theme manager"""
        # ThemeManager now handles everything: stylesheet + window effects
        self.theme_manager.apply_theme(self)
    
    def switch_theme(self, theme_name):
        """Switch to a different theme"""
        if self.theme_manager.set_theme(theme_name):
            self.apply_current_theme()
            theme_info = self.theme_manager.get_theme_display_info()
            self.status_bar.showMessage(f"Theme changed to: {theme_info}", 3000)
            # Update settings
            self.settings['theme'] = theme_name
    
    def open_in_cmd(self):
        """Open Command Prompt in the current directory"""
        try:
            # Get the current path
            current_dir = self.current_path
            
            # Verify the path exists
            if not os.path.exists(current_dir):
                self.status_bar.showMessage("❌ Current path does not exist", 3000)
                return
            
            # Open CMD in the current directory
            if platform.system() == 'Windows':
                # Use the simpler approach: just set cwd and open cmd
                subprocess.Popen('cmd.exe', cwd=current_dir, creationflags=subprocess.CREATE_NEW_CONSOLE)
                self.status_bar.showMessage(f"💻 Opened CMD in: {current_dir}", 3000)
            else:
                # For non-Windows systems, open terminal (fallback)
                subprocess.Popen(['x-terminal-emulator'], cwd=current_dir)
                self.status_bar.showMessage(f"💻 Opened terminal in: {current_dir}", 3000)
                
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to open Command Prompt:\n{str(e)}")
            self.status_bar.showMessage("❌ Failed to open CMD", 3000)
    
    def open_in_vscode(self):
        """Open current directory in VS Code"""
        try:
            # Get the current path
            current_dir = self.current_path
            
            # Verify the path exists
            if not os.path.exists(current_dir):
                self.status_bar.showMessage("❌ Current path does not exist", 3000)
                return
            
            # Try multiple methods to find and open VS Code
            vscode_opened = False
            
            # Method 1: Try 'code' command in PATH
            try:
                subprocess.Popen(['code', current_dir], 
                               stdout=subprocess.DEVNULL, 
                               stderr=subprocess.DEVNULL)
                vscode_opened = True
                self.status_bar.showMessage(f"📝 Opened in VS Code: {current_dir}", 3000)
            except FileNotFoundError:
                pass
            
            # Method 2: Try common installation paths on Windows
            if not vscode_opened and platform.system() == 'Windows':
                possible_paths = [
                    os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Programs', 'Microsoft VS Code', 'Code.exe'),
                    os.path.join(os.environ.get('PROGRAMFILES', ''), 'Microsoft VS Code', 'Code.exe'),
                    os.path.join(os.environ.get('PROGRAMFILES(X86)', ''), 'Microsoft VS Code', 'Code.exe'),
                ]
                
                for vscode_path in possible_paths:
                    if os.path.exists(vscode_path):
                        subprocess.Popen([vscode_path, current_dir])
                        vscode_opened = True
                        self.status_bar.showMessage(f"📝 Opened in VS Code: {current_dir}", 3000)
                        break
            
            # If still not opened, show error
            if not vscode_opened:
                QMessageBox.information(
                    self, 
                    "VS Code Not Found", 
                    "VS Code could not be found.\n\n"
                    "Please make sure VS Code is installed.\n"
                    "You can download it from: https://code.visualstudio.com/\n\n"
                    "Or add the 'code' command to your PATH by opening VS Code,\n"
                    "pressing Ctrl+Shift+P and running:\n"
                    "'Shell Command: Install 'code' command in PATH'"
                )
                self.status_bar.showMessage("❌ VS Code not found", 3000)
                
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to open VS Code:\n{str(e)}")
            self.status_bar.showMessage("❌ Failed to open VS Code", 3000)
    
    def show_settings_dialog(self):
        """Show the settings dialog"""
        dialog = SettingsDialog(self, self.settings)
        
        # Connect the signal
        dialog.settings_changed.connect(self.apply_settings)
        
        # Show the dialog
        dialog.exec()
    
    def apply_settings(self, new_settings):
        """Apply new settings from the settings dialog"""
        # Update internal settings
        self.settings.update(new_settings)
        
        # Apply theme change
        theme = new_settings.get('theme', 'liquid_glass')
        if theme != self.theme_manager.current_theme:
            self.switch_theme(theme)
        
        # Apply font size and family
        font_size = new_settings.get('font_size', 11)
        font_family = new_settings.get('font_family', 'Segoe UI')
        self.apply_font(font_size, font_family)
        
        # Apply view mode
        view_mode = new_settings.get('view_mode', 'list')
        self.apply_view_mode(view_mode)
        
        # Apply icon size
        icon_size = new_settings.get('icon_size', 32)
        if view_mode == 'icon':
            self.file_list.setIconSize(QSize(icon_size, icon_size))
        
        # Apply hidden files visibility
        show_hidden = new_settings.get('show_hidden', False)
        self.toggle_hidden_files(show_hidden)
        
        # Apply alternating rows
        self.file_list.setAlternatingRowColors(new_settings.get('alternating_rows', True))
        
        self.status_bar.showMessage("✅ Settings applied successfully", 3000)
    
    def apply_font(self, size, family='Segoe UI'):
        """Apply font size and family to all text elements"""
        font = QFont(family, size)
        
        # Apply to main widgets
        self.address_bar.setFont(font)
        self.search_bar.setFont(font)
        self.file_list.setFont(font)
        self.status_bar.setFont(font)
        
        # Update settings
        self.settings['font_size'] = size
        self.settings['font_family'] = family
    
    def apply_view_mode(self, mode):
        """Change the file list view mode"""
        if mode == 'list':
            self.file_list.setViewMode(QListView.ViewMode.ListMode)
        elif mode == 'icon':
            self.file_list.setViewMode(QListView.ViewMode.IconMode)
            icon_size = self.settings.get('icon_size', 32)
            self.file_list.setIconSize(QSize(icon_size, icon_size))
        
        self.settings['view_mode'] = mode
    
    def toggle_hidden_files(self, show):
        """Toggle visibility of hidden files"""
        if show:
            self.file_model.setFilter(QDir.Filter.AllEntries | QDir.Filter.NoDotAndDotDot | QDir.Filter.Hidden)
        else:
            self.file_model.setFilter(QDir.Filter.AllEntries | QDir.Filter.NoDotAndDotDot)
        
        self.settings['show_hidden_files'] = show

    # Navigation methods
    def navigate_to_path(self, path):
        """Navigate to a specific path"""
        if os.path.exists(path):
            self.current_path = os.path.abspath(path)
            self.address_bar.setText(self.current_path)
            
            root_index = self.file_model.setRootPath(self.current_path)
            proxy_root = self.proxy_model.mapFromSource(root_index)
            self.file_list.setRootIndex(proxy_root)
            
            self.status_bar.showMessage(f"📁 {self.current_path}")
            self.update_file_count()
            
            # Add to navigation history
            self.data_manager.add_history(self.current_path)
            logger.debug(f"Navigated to: {self.current_path}")

    def navigate_from_address_bar(self):
        """Navigate using the address bar"""
        path = self.address_bar.text().strip()
        if path:
            self.navigate_to_path(path)

    def go_back(self):
        """Go to parent directory"""
        parent = os.path.dirname(self.current_path)
        if parent != self.current_path:
            self.navigate_to_path(parent)

    def go_forward(self):
        """Go forward (placeholder for history)"""
        pass

    def go_up(self):
        """Go up one directory level"""
        self.go_back()

    def refresh_current(self):
        """Refresh current directory"""
        self.navigate_to_path(self.current_path)

    def filter_files(self):
        """Filter files based on search text"""
        text = self.search_bar.text()
        if text:
            self.proxy_model.setFilterWildcard(f"*{text}*")
        else:
            self.proxy_model.setFilterWildcard("")

    def open_item(self, index):
        """Open file or folder on double click"""
        source_index = self.proxy_model.mapToSource(index)
        path = self.file_model.filePath(source_index)
        
        if self.file_model.isDir(source_index):
            self.navigate_to_path(path)
        else:
            # Add to recent files
            self.data_manager.add_recent_file(path)
            self.file_ops.open_file(path)

    # File operations
    def get_selected_paths(self):
        """Get paths of selected items"""
        selected_indexes = self.file_list.selectionModel().selectedIndexes()
        paths = []
        for index in selected_indexes:
            source_index = self.proxy_model.mapToSource(index)
            path = self.file_model.filePath(source_index)
            paths.append(path)
        return paths

    def create_new_folder(self):
        """Create a new folder"""
        name, ok = QInputDialog.getText(self, "New Folder", "Folder name:")
        if ok and name:
            new_path = os.path.join(self.current_path, name)
            if self.file_ops.create_folder(new_path):
                self.refresh_current()
            else:
                QMessageBox.warning(self, "Error", f"Could not create folder '{name}'")

    def copy_selected(self):
        """Copy selected items"""
        paths = self.get_selected_paths()
        if paths:
            self.clipboard_path = paths
            self.clipboard_operation = 'copy'
            self.status_bar.showMessage(f"📋 Copied {len(paths)} item(s)")

    def cut_selected(self):
        """Cut selected items"""
        paths = self.get_selected_paths()
        if paths:
            self.clipboard_path = paths
            self.clipboard_operation = 'cut'
            self.status_bar.showMessage(f"✂️ Cut {len(paths)} item(s)")

    def paste_items(self):
        """Paste items from clipboard"""
        if not self.clipboard_path:
            return
            
        success_count = 0
        for source_path in self.clipboard_path:
            dest_path = os.path.join(self.current_path, os.path.basename(source_path))
            
            if self.clipboard_operation == 'copy':
                if self.file_ops.copy_item(source_path, dest_path):
                    success_count += 1
            elif self.clipboard_operation == 'cut':
                if self.file_ops.move_item(source_path, dest_path):
                    success_count += 1
        
        if self.clipboard_operation == 'cut':
            self.clipboard_path = None
            self.clipboard_operation = None
            
        self.refresh_current()
        self.status_bar.showMessage(f"📌 Pasted {success_count} item(s)")

    def rename_selected(self):
        """Rename selected item"""
        paths = self.get_selected_paths()
        if len(paths) == 1:
            old_path = paths[0]
            old_name = os.path.basename(old_path)
            new_name, ok = QInputDialog.getText(self, "Rename", "New name:", text=old_name)
            
            if ok and new_name and new_name != old_name:
                new_path = os.path.join(os.path.dirname(old_path), new_name)
                if self.file_ops.rename_item(old_path, new_path):
                    self.refresh_current()
                else:
                    QMessageBox.warning(self, "Error", f"Could not rename '{old_name}'")

    def delete_selected(self):
        """Delete selected items"""
        paths = self.get_selected_paths()
        if not paths:
            return
        
        # Check if confirmation is required
        if self.settings.get('confirm_delete', True):
            reply = QMessageBox.question(
                self, "Delete", 
                f"Are you sure you want to delete {len(paths)} item(s)?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            
            if reply != QMessageBox.StandardButton.Yes:
                return
        
        success_count = 0
        for path in paths:
            if self.file_ops.delete_item(path):
                success_count += 1
        
        self.refresh_current()
        self.status_bar.showMessage(f"🗑️ Deleted {success_count} item(s)")

    def show_context_menu(self, position):
        """Show context menu"""
        logger.info("=== Context menu requested ===")
        index = self.file_list.indexAt(position)
        logger.info(f"Index valid: {index.isValid()}")
        
        menu = QMenu(self)
        
        if index.isValid():
            # Get the path for this item
            source_index = self.proxy_model.mapToSource(index)
            selected_path = self.file_model.filePath(source_index)
            logger.info(f"Context menu for path: {selected_path}")
            
            open_action = menu.addAction("📂 Open")
            open_action.triggered.connect(lambda: self.open_item(index))
            
            # Add "Run" option for executables
            if self.file_ops.is_executable(selected_path):
                run_action = menu.addAction("▶️ Run")
                run_action.triggered.connect(lambda checked=False, p=selected_path: self.run_file(p))
                logger.info(f"Added 'Run' action for executable: {selected_path}")
            
            menu.addSeparator()
            
            copy_action = menu.addAction("📋 Copy")
            copy_action.triggered.connect(self.copy_selected)
            
            cut_action = menu.addAction("✂️ Cut")
            cut_action.triggered.connect(self.cut_selected)
            
            rename_action = menu.addAction("✏️ Rename")
            rename_action.triggered.connect(self.rename_selected)
            
            delete_action = menu.addAction("🗑️ Delete")
            delete_action.triggered.connect(self.delete_selected)
            
            menu.addSeparator()
            
            # Add to favorites option - use lambda to pass the path
            favorite_action = menu.addAction("⭐ Add to Favorites")
            favorite_action.triggered.connect(lambda checked=False, p=selected_path: self.add_to_favorites(p))
            logger.info(f"Added 'Add to Favorites' action for: {selected_path}")
        
        menu.addSeparator()
        paste_action = menu.addAction("📌 Paste")
        paste_action.triggered.connect(self.paste_items)
        paste_action.setEnabled(bool(self.clipboard_path))
        
        new_folder_action = menu.addAction("📁 New Folder")
        new_folder_action.triggered.connect(self.create_new_folder)
        
        menu.addSeparator()
        cmd_action = menu.addAction("💻 Open in CMD")
        cmd_action.triggered.connect(self.open_in_cmd)
        
        vscode_action = menu.addAction("📝 Open in VS Code")
        vscode_action.triggered.connect(self.open_in_vscode)
        
        logger.info("Showing context menu")
        menu.exec(self.file_list.mapToGlobal(position))

    def update_file_count(self):
        """Update file count in status bar"""
        try:
            items = os.listdir(self.current_path)
            files = sum(1 for item in items if os.path.isfile(os.path.join(self.current_path, item)))
            folders = sum(1 for item in items if os.path.isdir(os.path.join(self.current_path, item)))
            self.status_bar.showMessage(f"📁 {self.current_path} | 📄 {files} files | 📁 {folders} folders")
        except:
            pass
    
    def load_favorites(self):
        """Load favorites from data manager"""
        try:
            logger.info("Loading favorites from DataManager")
            self.favorites = self.data_manager.get_favorites()
            logger.info(f"Loaded {len(self.favorites)} favorites: {self.favorites}")
        except Exception as e:
            logger.error(f"Error loading favorites: {e}", exc_info=True)
            self.favorites = []
    
    def save_favorites(self):
        """Save favorites using data manager"""
        # Note: DataManager handles saving automatically in add/remove methods
        # This method kept for compatibility
        logger.info("Favorites are automatically saved by DataManager")
    
    def add_to_favorites(self, path=None):
        """Add a path to favorites"""
        logger.info("=== add_to_favorites called ===")
        logger.info(f"Input path parameter: {path}")
        
        if path is None:
            # Get selected items
            paths = self.get_selected_paths()
            logger.info(f"Selected paths: {paths}")
            if not paths:
                logger.warning("No paths selected")
                self.status_bar.showMessage("⚠️ No item selected", 3000)
                return
            path = paths[0]  # Take first selected item
            logger.info(f"Using first selected path: {path}")
        
        # Validate path is a string
        if not isinstance(path, str):
            logger.error(f"Path is not a string: {type(path)} - {path}")
            return
        
        # Normalize the path
        path = os.path.abspath(path)
        logger.info(f"Normalized path: {path}")
        
        # Check if path exists
        if not os.path.exists(path):
            logger.warning(f"Path does not exist: {path}")
            self.status_bar.showMessage(f"⚠️ Path does not exist: {os.path.basename(path)}", 3000)
            return
        
        # Use data manager to add favorite
        if self.data_manager.add_favorite(path):
            # Reload favorites list
            self.load_favorites()
            
            # Update UI
            self.update_favorites_list()
            
            # Show success message
            message = f"⭐ Added to favorites: {os.path.basename(path)}"
            logger.info(message)
            self.status_bar.showMessage(message, 3000)
            
            # Also show a message box for confirmation
            QMessageBox.information(self, "Favorites", f"Added to favorites:\n{path}")
        else:
            logger.info(f"Path already in favorites: {path}")
            self.status_bar.showMessage(f"⭐ Already in favorites: {os.path.basename(path)}", 3000)
    
    def remove_from_favorites(self, path):
        """Remove a path from favorites"""
        logger.info(f"=== remove_from_favorites called ===")
        logger.info(f"Removing path: {path}")
        
        if self.data_manager.remove_favorite(path):
            # Reload favorites list
            self.load_favorites()
            
            # Update UI
            self.update_favorites_list()
            
            message = f"❌ Removed from favorites: {os.path.basename(path)}"
            logger.info(message)
            self.status_bar.showMessage(message, 3000)
        else:
            logger.warning(f"Path not found in favorites: {path}")
    
    def open_favorite(self, path):
        """Open a favorite - navigate if folder, execute/open if file"""
        logger.info(f"=== open_favorite called for: {path} ===")
        
        if not os.path.exists(path):
            logger.warning(f"Favorite path no longer exists: {path}")
            QMessageBox.warning(self, "Path Not Found", 
                              f"This path no longer exists:\n{path}\n\nWould you like to remove it from favorites?")
            return
        
        if os.path.isdir(path):
            # Navigate to folder
            logger.info(f"Navigating to folder: {path}")
            self.navigate_to_path(path)
        else:
            # It's a file - check if executable
            if self.file_ops.is_executable(path):
                # Ask for confirmation before running
                reply = QMessageBox.question(
                    self,
                    "Run Executable",
                    f"Do you want to run this executable?\n\n{os.path.basename(path)}\n\nPath: {path}",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No
                )
                
                if reply == QMessageBox.StandardButton.Yes:
                    logger.info(f"User confirmed - running executable: {path}")
                    success, message = self.file_ops.run_executable(path)
                    if success:
                        self.status_bar.showMessage(f"✅ {message}", 5000)
                        logger.info(f"Successfully launched: {path}")
                    else:
                        QMessageBox.warning(self, "Execution Failed", message)
                        logger.error(f"Failed to launch: {path} - {message}")
                else:
                    logger.info("User cancelled execution")
            else:
                # Regular file - just open it
                logger.info(f"Opening file: {path}")
                if self.file_ops.open_file(path):
                    self.status_bar.showMessage(f"📂 Opened: {os.path.basename(path)}", 3000)
                    # Add to recent files
                    self.data_manager.add_recent_file(path)
                else:
                    QMessageBox.warning(self, "Error", f"Could not open file:\n{path}")
    
    def run_file(self, path):
        """Run an executable file with confirmation"""
        logger.info(f"=== run_file called for: {path} ===")
        
        if not os.path.exists(path):
            QMessageBox.warning(self, "File Not Found", f"File not found:\n{path}")
            return
        
        # Confirm execution
        reply = QMessageBox.question(
            self,
            "Run Executable",
            f"Are you sure you want to run this executable?\n\n📄 {os.path.basename(path)}\n📁 {os.path.dirname(path)}\n\n⚠️ Only run files you trust!",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            logger.info(f"User confirmed - running: {path}")
            success, message = self.file_ops.run_executable(path)
            
            if success:
                self.status_bar.showMessage(f"✅ {message}", 5000)
                logger.info(f"Successfully executed: {path}")
                QMessageBox.information(self, "Success", message)
            else:
                self.status_bar.showMessage(f"❌ {message}", 5000)
                logger.error(f"Execution failed: {path} - {message}")
                QMessageBox.warning(self, "Execution Failed", message)
        else:
            logger.info("User cancelled execution")
            self.status_bar.showMessage("Execution cancelled", 2000)
    
    def update_favorites_list(self):
        """Update the favorites list in the sidebar"""
        logger.info("=== Updating favorites list UI ===")
        logger.info(f"Current favorites: {self.favorites}")
        
        # Clear existing favorites buttons (but keep the stretch at the end)
        while self.favorites_layout.count() > 1:  # Keep the stretch item
            child = self.favorites_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        # Clean and validate favorites - remove any non-string items
        self.favorites = [f for f in self.favorites if isinstance(f, str)]
        logger.info(f"After validation: {len(self.favorites)} favorites")
        
        # Sort favorites alphabetically
        sorted_favorites = sorted(self.favorites, key=lambda p: os.path.basename(p).lower())
        logger.info(f"Sorted favorites: {sorted_favorites}")
        
        if not sorted_favorites:
            # Show "Nothing Favorited" message
            empty_label = QLabel("Nothing Favorited Yet")
            empty_label.setStyleSheet("""
                QLabel {
                    padding: 20px 10px;
                    color: rgba(255, 255, 255, 0.4);
                    font-style: italic;
                    text-align: center;
                    font-size: 9pt;
                }
            """)
            empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.favorites_layout.insertWidget(0, empty_label)
        else:
            # Add each favorite as a widget
            for fav_path in sorted_favorites:
                if os.path.exists(fav_path):
                    # Get proper icon using file_ops icon system
                    icon = self.file_ops.get_file_icon(fav_path)
                    
                    # Create horizontal layout for button and remove button
                    fav_widget = QWidget()
                    fav_widget.setStyleSheet("background: transparent;")
                    fav_layout = QHBoxLayout(fav_widget)
                    fav_layout.setContentsMargins(0, 0, 0, 0)
                    fav_layout.setSpacing(5)
                    
                    # Main favorite button
                    btn = QPushButton(f"{icon} {os.path.basename(fav_path)}")
                    btn.setToolTip(fav_path)
                    btn.setStyleSheet("""
                        QPushButton {
                            text-align: left;
                            padding: 8px 12px;
                            border: 1px solid rgba(255, 200, 100, 0.2);
                            border-radius: 6px;
                            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 rgba(255, 200, 100, 0.1),
                                stop:1 rgba(255, 150, 50, 0.08));
                            color: rgba(255, 255, 255, 0.95);
                            font-size: 9pt;
                        }
                        QPushButton:hover {
                            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 rgba(255, 200, 100, 0.25),
                                stop:1 rgba(255, 150, 50, 0.18));
                            border: 1px solid rgba(255, 200, 100, 0.35);
                            color: white;
                        }
                        QPushButton:pressed {
                            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 rgba(255, 150, 50, 0.2),
                                stop:1 rgba(255, 200, 100, 0.25));
                        }
                    """)
                    btn.clicked.connect(lambda checked, p=fav_path: self.open_favorite(p))
                    
                    # Remove button
                    remove_btn = QPushButton("×")
                    remove_btn.setToolTip("Remove from favorites")
                    remove_btn.setFixedSize(24, 24)
                    remove_btn.setStyleSheet("""
                        QPushButton {
                            border: 1px solid rgba(255, 100, 100, 0.3);
                            border-radius: 12px;
                            background: rgba(255, 100, 100, 0.15);
                            color: rgba(255, 150, 150, 0.9);
                            font-size: 14pt;
                            font-weight: bold;
                            padding: 0px;
                        }
                        QPushButton:hover {
                            background: rgba(255, 100, 100, 0.3);
                            border: 1px solid rgba(255, 100, 100, 0.5);
                            color: white;
                        }
                        QPushButton:pressed {
                            background: rgba(255, 100, 100, 0.5);
                        }
                    """)
                    remove_btn.clicked.connect(lambda checked, p=fav_path: self.remove_from_favorites(p))
                    
                    fav_layout.addWidget(btn, 1)
                    fav_layout.addWidget(remove_btn, 0)
                    
                    # Insert before the stretch item
                    self.favorites_layout.insertWidget(self.favorites_layout.count() - 1, fav_widget)
                else:
                    # Path no longer exists, remove it
                    logger.warning(f"Favorite path no longer exists, removing: {fav_path}")
                    if fav_path in self.favorites:
                        self.favorites.remove(fav_path)
                        self.data_manager.remove_favorite(fav_path)
        
        logger.info(f"Favorites UI updated with {len(sorted_favorites)} items")

# Alias for easier import
FileExplorer = LiquidGlassFileExplorer