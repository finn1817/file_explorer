## 🎯 Quick start

### How to Run the App

1. Go to the project folder:
   ```powershell
   cd C:\Users\danny\Desktop\gitApps\files\file_explorer\app-code
   ```

2. Run with the launcher (easiest):
   - Double‑click `run.bat`
   
3. Or from a terminal:
   ```powershell
   cd python
   python -B main.py
   ```

The launcher sets `PYTHONDONTWRITEBYTECODE=1` and uses `-B` so Python doesn’t create `.pyc` files.

### Project structure at a glance

```
📁 app-code/
│
├── 🐍 python/           → All Python code
│   ├── main.py         → Start here!
│   ├── file_explorer.py
│   ├── file_operations.py
│   ├── data_manager.py
│   ├── theme.py
│   ├── settings_dialog.py
│   └── styles.py
│
├── 💾 data/            → Your data
│   ├── favorites.json
│   ├── settings.json
│   ├── history.json
│   ├── bookmarks.json
│   └── recent_files.json
│
├── 📋 log/             → Application logs
│   └── file_explorer.log
│
├── 📚 info/            → Documentation
│   ├── README.md
│   ├── PROJECT_STRUCTURE.md
│   ├── REORGANIZATION_COMPLETE.md
│   ├── TROUBLESHOOTING.md
│   ├── FIXES_APPLIED.md
│   ├── EXECUTABLE_SUPPORT.md
│   ├── EXECUTABLE_UPDATE.md
│   └── ICON_REFERENCE.md
│
└── ▶️ run.bat          → Click to launch (no .pyc)

### Requirements

- Windows + Python 3.11 or newer (developed on 3.13)
- Packages: `PyQt6`, `send2trash`
   - If needed:
      ```powershell
      py -m pip install PyQt6 send2trash
      ```
```

### Common tasks

• Edit code → open files in `python/`.

• Debug → check `log/file_explorer.log`.

• Backup → copy the `data/` folder (JSON files). Backups like `*.json.bak` are created automatically on save.

• Docs → see the `info/` folder.

• Run → double‑click `run.bat`.

### Features you’ll notice

- Scrollable favorites
- Run executables (.exe, .bat, .cmd, .ps1, .py, .lnk) with confirmation
- Dozens of file type icons
- JSON‑backed data (favorites, settings, history, bookmarks, recent files)
- Liquid glass theme

### Need help?

Check these docs in the `info/` folder:
- `README.md` - Overview and features
- `PROJECT_STRUCTURE.md` - Detailed structure info
- `TROUBLESHOOTING.md` - Common issues
- `EXECUTABLE_SUPPORT.md` - How to run files
- `ICON_REFERENCE.md` - All file icons

---

Happy exploring 👋
