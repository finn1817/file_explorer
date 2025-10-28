import os
import sys

# Prevent creation of .pyc files as early as possible (applies to subsequent imports)
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
sys.dont_write_bytecode = True

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from file_explorer import FileExplorer

def main():
    # Enable high DPI scaling
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    app = QApplication(sys.argv)
    app.setApplicationName("Liquid Glass File Explorer")
    app.setOrganizationName("LiquidGlass")
    
    # Set application icon if available
    if os.path.exists("icon.ico"):
        app.setWindowIcon(QIcon("icon.ico"))
    
    # Create and show the main window
    explorer = FileExplorer()
    explorer.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()