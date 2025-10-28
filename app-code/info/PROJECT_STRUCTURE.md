# 📁 Project Structure

## Directory Organization

```
app-code/
├── python/              ← All Python source code
│   ├── main.py         ← Application entry point
│   ├── file_explorer.py
│   ├── file_operations.py
│   ├── data_manager.py
│   ├── theme.py
│   ├── settings_dialog.py
│   └── styles.py
│
├── data/               ← All application data (JSON files)
│   ├── favorites.json
│   ├── settings.json
│   ├── history.json
│   ├── bookmarks.json
│   └── recent_files.json
│
├── log/                ← Application logs
│   └── file_explorer.log
│
├── info/               ← Documentation
│   ├── README.md
│   ├── TROUBLESHOOTING.md
│   ├── FIXES_APPLIED.md
│   ├── EXECUTABLE_SUPPORT.md
│   ├── EXECUTABLE_UPDATE.md
│   └── ICON_REFERENCE.md
│
└── run.bat             ← Quick launcher script
```

## 🚀 How to Run

### Method 1: Using the Launcher (Recommended)
Double-click `run.bat` in the `app-code` folder

### Method 2: From Terminal
```bash
cd app-code/python
python main.py
```

### Method 3: From PowerShell
```powershell
cd app-code\python
python main.py
```

## 📂 Why This Structure?

### ✅ Benefits:
- **Clean separation**: Code, data, logs, and docs are separate
- **Easy to find**: Everything has its own folder
- **Professional**: Industry-standard project organization
- **Maintainable**: Easy to add new files in the right place
- **Portable**: Data folder can be backed up separately
- **Debugging**: Logs in dedicated folder

### 📁 Folder Purposes:

**`python/`** - All source code
- Easy to find all Python files
- Can be version controlled separately
- Clear entry point (main.py)

**`data/`** - User data & settings
- All JSON files in one place
- Easy to backup/restore
- Can be gitignored if needed

**`log/`** - Application logs
- Centralized logging
- Easy to clear old logs
- Won't clutter code directory

**`info/`** - Documentation
- All docs in one place
- Easy to reference
- Professional organization

## 🔧 How It Works

### Path Resolution:
```python
# From python/file_explorer.py
log_dir = Path(__file__).parent.parent / 'log'  # Goes up to app-code, then into log
data_dir = Path(__file__).parent.parent / 'data'  # Goes up to app-code, then into data
```

### Relative Paths:
- Python scripts use `Path(__file__).parent.parent` to find app-code directory
- This works regardless of where the app is installed
- Data and logs always resolve correctly

## 📝 Adding New Files

**New Python module?**
→ Add to `python/` folder

**New data file?**
→ Add to `data/` folder

**New documentation?**
→ Add to `info/` folder

**Want to check logs?**
→ Look in `log/` folder

## 🔍 Troubleshooting

### "Can't find data files"
- Check that `data/` folder exists in `app-code/`
- Verify you're running from the correct directory

### "Logs not appearing"
- Check `log/` folder for `file_explorer.log`
- Log folder is created automatically

### "Import errors"
- Make sure you're in the `python/` directory when running
- All Python files must be in `python/` folder

## ✅ Migration Complete

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

**Cleaner, more professional, easier to maintain!** ✨

---

**Last Updated**: October 27, 2025
**Status**: ✅ Fully Migrated & Working
