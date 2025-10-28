# 📁 Project structure

## Directory Organization

```
.
├── .gitignore                 ← Keeps __pycache__/ and *.pyc out of git
└── app-code/
	├── python/               ← All Python source code
	│   ├── main.py          ← Application entry point
	│   ├── file_explorer.py
	│   ├── file_operations.py
	│   ├── data_manager.py
	│   ├── theme.py
	│   ├── settings_dialog.py
	│   └── styles.py
	│
	├── data/                 ← All application data (JSON files)
	│   ├── favorites.json
	│   ├── settings.json (+ settings.json.bak backups)
	│   ├── history.json (+ history.json.bak backups)
	│   ├── bookmarks.json
	│   └── recent_files.json
	│
	├── log/                  ← Application logs
	│   └── file_explorer.log
	│
	├── info/                 ← Documentation (this folder)
	│   ├── PROJECT_STRUCTURE.md
	│   ├── QUICK_START.md
	│   ├── REORGANIZATION_COMPLETE.md
	│   ├── TROUBLESHOOTING.md
	│   ├── EXECUTABLE_SUPPORT.md
	│   ├── EXECUTABLE_UPDATE.md
	│   └── ICON_REFERENCE.md
	│
	└── run.bat               ← One-click launcher (disables .pyc)
```

## 🚀 How to run

### Method 1: Using the Launcher (Recommended)
Double-click `app-code\run.bat`.

Notes:
- The launcher sets PYTHONDONTWRITEBYTECODE and uses `python -B` so Python won’t create `.pyc` files.
- The GUI starts from `python/main.py` and writes data only under `app-code/data`.

### Method 2: From Terminal
```powershell
cd app-code\python
python -B main.py
```

### Method 3: From PowerShell
Same as above; PowerShell is the default on Windows.

## 📂 Why this structure?

### ✅ Benefits:
- **Clean separation**: Code, data, logs, and docs are separate
- **Easy to find**: Everything has its own folder
- **Professional**: Industry-standard project organization
- **Maintainable**: Easy to add new files in the right place
- **Portable**: Data folder can be backed up separately
- **Debugging**: Logs in dedicated folder

### 📁 Folder Purposes:

**`python/`** – All source code
- Easy to find all Python files
- Can be version controlled separately
- Clear entry point (main.py)

**`data/`** – User data & settings
- All JSON files in one place
- Easy to backup/restore
- Can be gitignored if needed

**`log/`** – Application logs
- Centralized logging
- Easy to clear old logs
- Won't clutter code directory

**`info/`** – Documentation
- All docs in one place
- Easy to reference
- Professional organization

## 🔧 How it works

### Path Resolution:
```python
# From python/file_explorer.py
log_dir = Path(__file__).parent.parent / 'log'   # app-code/log
data_dir = Path(__file__).parent.parent / 'data' # app-code/data
```

### Relative paths
- Code locates the `app-code` directory with `Path(__file__).parent.parent`.
- Works regardless of where the folder lives on disk.
- Data and logs always resolve to `app-code/data` and `app-code/log`.

## 📝 Adding new files

• New Python module → put it in `python/`.

• New data file → put it in `data/`.

• New documentation → put it in `info/`.

• Logs live in `log/`.

## 🔍 Troubleshooting

### “Can’t find data files”
- Check that `data/` folder exists in `app-code/`
- Verify you're running from the correct directory

### “Logs not appearing”
- Check `log/` folder for `file_explorer.log`
- Log folder is created automatically

### “Import errors”
- Make sure you're in the `python/` directory when running
- All Python files must be in `python/` folder

## ✅ Migration complete

**Old Structure:**
```
app-code/
├── main.py
├── file_explorer.py
├── file_operations.py
├── data_manager.py
├── theme.py
├── settings_dialog.py
├── styles.py
├── file_explorer.log
├── favorites.json
└── ...
```

**New Structure:**
```
app-code/
├── python/         ← Code
├── data/           ← Data
├── log/            ← Logs
├── info/           ← Docs
└── run.bat         ← Launcher
```

Cleaner, simpler, and easier to maintain.

---

Updated: October 27, 2025
Status: ✅ Current
