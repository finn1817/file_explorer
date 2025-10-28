# 🌊 Liquid Glass File Explorer

A modern, beautiful file explorer built with PyQt6 featuring a stunning liquid glass UI and comprehensive file management capabilities.

## ✨ Features

### 🎨 Beautiful UI
- Liquid glass theme with blur effects
- Multiple theme options
- Customizable fonts and icon sizes
- Smooth animations and transitions

### 📁 File Management (Full CRUD)
- **Create**: New folders
- **Read**: Browse files and folders
- **Update**: Rename, move, copy files
- **Delete**: Delete to trash or permanent deletion

### ⭐ Favorites System (Full CRUD)
- **Add** items to favorites (Right-click → Add to Favorites or Ctrl+D)
- **View** all favorites in the sidebar
- **Remove** favorites with one click
- **Persistent** storage in JSON files

### 📊 Data Management
All app data is stored in JSON files in the `data/` directory:

#### `data/favorites.json`
Stores your favorite files and folders:
```json
[
  "C:\\Users\\YourName\\Documents\\Important",
  "C:\\Users\\YourName\\Desktop\\Projects"
]
```

#### `data/settings.json`
Stores all user preferences:
```json
{
  "theme": "liquid_glass",
  "font_size": 11,
  "font_family": "Segoe UI",
  "view_mode": "list",
  "show_hidden": false,
  "confirm_delete": true
}
```

#### `data/history.json`
Tracks navigation history:
```json
[
  {
    "path": "C:\\Users\\YourName\\Documents",
    "timestamp": "2025-10-27T10:30:45.123456"
  }
]
```

#### `data/bookmarks.json`
Named bookmarks for quick access:
```json
{
  "Work Projects": "C:\\Work\\Projects",
  "Personal Docs": "C:\\Users\\YourName\\Personal"
}
```

#### `data/recent_files.json`
Recently opened files:
```json
[
  {
    "path": "C:\\Users\\YourName\\Documents\\report.pdf",
    "timestamp": "2025-10-27T10:35:12.654321"
  }
]
```

### 🔧 CRUD Operations

#### Favorites CRUD
- **Create**: `Ctrl+D` or right-click → "Add to Favorites"
- **Read**: View in sidebar under "⭐ Favorites"
- **Update**: Remove and re-add (rename coming soon)
- **Delete**: Click the `×` button next to any favorite

#### Files CRUD
- **Create**: `Ctrl+Shift+N` to create new folder
- **Read**: Browse and search files
- **Update**: `F2` to rename, `Ctrl+C/X/V` to copy/cut/paste
- **Delete**: `Delete` key or right-click → Delete

#### Settings CRUD
- **Create/Update**: `Ctrl+,` to open settings dialog
- **Read**: Settings automatically loaded on startup
- **Delete**: Clear settings from settings dialog

### ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+D` | Add to Favorites |
| `Ctrl+Shift+N` | New Folder |
| `Ctrl+C` | Copy |
| `Ctrl+X` | Cut |
| `Ctrl+V` | Paste |
| `F2` | Rename |
| `Delete` | Delete |
| `F5` | Refresh |
| `Alt+Left` | Back |
| `Alt+Right` | Forward |
| `Alt+Up` | Go Up |
| `Ctrl+,` | Settings |
| `Ctrl+Shift+C` | Open in CMD |
| `Ctrl+Shift+V` | Open in VS Code |

### 🖱️ Context Menu
Right-click on any file or folder to access:
- 📂 Open
- 📋 Copy
- ✂️ Cut
- ✏️ Rename
- 🗑️ Delete
- ⭐ Add to Favorites
- 💻 Open in CMD
- 📝 Open in VS Code

### 🛠️ Advanced Features

#### Data Manager
The `DataManager` class provides a robust API for all data operations:

```python
from data_manager import DataManager

dm = DataManager()

# Favorites
dm.add_favorite("C:\\path\\to\\folder")
dm.remove_favorite("C:\\path\\to\\folder")
favorites = dm.get_favorites()
is_fav = dm.is_favorite("C:\\path\\to\\folder")

# Settings
dm.set_setting("theme", "dark_mode")
value = dm.get_setting("theme", default="liquid_glass")
dm.update_settings({"font_size": 12, "view_mode": "icon"})

# History
dm.add_history("C:\\visited\\path")
history = dm.get_history(limit=10)

# Export/Import
dm.export_all_data(Path("backup.json"))
dm.import_all_data(Path("backup.json"), merge=True)
```

#### Logging
All operations are logged to `file_explorer.log`:
- DEBUG: Detailed information
- INFO: General information
- WARNING: Warning messages
- ERROR: Error messages with stack traces

Check the log file to troubleshoot any issues.

## 🚀 Installation

1. Install required packages:
```bash
pip install PyQt6 send2trash
```

2. Run the application:
```bash
python main.py
```

## 📝 Debugging

If favorites aren't working:

1. **Check the log file**: `file_explorer.log`
2. **Verify data directory exists**: `data/` folder should be created automatically
3. **Check file permissions**: Ensure the app can write to the `data/` directory
4. **View data files**: All JSON files in `data/` should be readable

### Log File Example
```
2025-10-27 10:30:00 - INFO - Loading favorites from DataManager
2025-10-27 10:30:00 - INFO - Loaded 3 favorites: ['C:\\path1', 'C:\\path2', 'C:\\path3']
2025-10-27 10:30:15 - INFO - === add_to_favorites called ===
2025-10-27 10:30:15 - INFO - Adding favorite: C:\\path\\to\\folder
2025-10-27 10:30:15 - INFO - ✅ Wrote favorites.json: 256 bytes
```

## 🔍 Troubleshooting

### Favorites Not Saving
1. Check if `data/favorites.json` is being created
2. Look for errors in `file_explorer.log`
3. Verify write permissions in the app directory
4. Try running as administrator (Windows)

### No Console Output
- Console output is now saved to `file_explorer.log`
- Use a text editor to view the log in real-time

### File Permissions
On Windows, if you get permission errors:
1. Right-click the app folder
2. Properties → Security
3. Ensure your user has "Full Control"

## 🎯 Future Enhancements
- [ ] Drag and drop support
- [ ] File preview panel
- [ ] Zip/extract operations
- [ ] Bookmark folders with custom names
- [ ] Export/import settings
- [ ] Cloud storage integration

## 📄 License
MIT License - Feel free to modify and distribute!

## 🤝 Contributing
Contributions welcome! Please feel free to submit issues and pull requests.

---

Made with ❤️ and PyQt6
