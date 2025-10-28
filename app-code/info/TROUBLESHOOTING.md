# 🔧 Liquid Glass File Explorer - Quick Troubleshooting Guide

## ✅ Favorites System is NOW WORKING!

### How to Add Favorites
1. **Right-click** on any file or folder
2. Click **"⭐ Add to Favorites"**
3. You should see a popup confirmation
4. The item appears in the left sidebar under "⭐ Favorites"

**OR use keyboard shortcut:**
- Select a file/folder
- Press **Ctrl+D**

### How to Remove Favorites
- Click the **×** button next to any favorite in the sidebar

### Where is the Data Stored?
All app data is now in the `data/` directory:

```
app-code/
├── data/
│   ├── favorites.json       ← Your favorites
│   ├── settings.json        ← Your settings
│   ├── history.json         ← Navigation history
│   ├── bookmarks.json       ← Named bookmarks
│   └── recent_files.json    ← Recently opened files
├── file_explorer.log        ← Detailed logs of everything
└── ... (other app files)
```

## 🐛 Debugging Tips

### Check if Favorites are Being Saved
1. Open `data/favorites.json` in a text editor
2. Should look like:
   ```json
   [
     "C:\\Users\\YourName\\Documents\\Folder1",
     "C:\\Users\\YourName\\Desktop\\Folder2"
   ]
   ```

### View Detailed Logs
Open `file_explorer.log` in a text editor to see:
- When favorites are added/removed
- File paths being accessed
- Any errors that occur

Example log entries when adding a favorite:
```
2025-10-27 21:11:00 - INFO - === add_to_favorites called ===
2025-10-27 21:11:00 - INFO - Input path parameter: C:/Users/danny/Desktop/gitApps
2025-10-27 21:11:00 - INFO - Normalized path: C:\Users\danny\Desktop\gitApps
2025-10-27 21:11:00 - INFO - Adding favorite: C:\Users\danny\Desktop\gitApps
2025-10-27 21:11:00 - INFO - ✅ Wrote favorites.json: 38 bytes
2025-10-27 21:11:00 - INFO - Loaded 1 favorites: ['C:\\Users\\danny\\Desktop\\gitApps']
```

### Console Emoji Warning
You might see "Logging error" messages about Unicode characters in the console. **This is normal on Windows** and doesn't affect functionality. The emojis just can't display in the PowerShell console, but they work fine in the log file.

## 📋 Full CRUD Operations

### Favorites CRUD
- ✅ **Create**: Right-click → "Add to Favorites" or Ctrl+D
- ✅ **Read**: View in sidebar
- ✅ **Update**: Remove and re-add
- ✅ **Delete**: Click × button

### Files CRUD
- ✅ **Create**: Ctrl+Shift+N (new folder)
- ✅ **Read**: Browse files
- ✅ **Update**: F2 to rename, Ctrl+C/X/V to copy/cut/paste
- ✅ **Delete**: Delete key

### Settings CRUD
- ✅ **Create/Update**: Ctrl+, to open settings
- ✅ **Read**: Settings auto-load
- ✅ **Delete**: Clear from settings dialog

## 🔍 Common Issues & Solutions

### Issue: "Nothing shows up when I favorite something"
**Solution**: 
1. Check the log file for errors
2. Verify `data/favorites.json` exists and has content
3. Try restarting the app

### Issue: "Favorites disappear after restarting"
**Solution**:
1. Check if `data/favorites.json` has content
2. Verify file permissions (should be readable/writable)
3. Check the log for "Loading favorites from DataManager"

### Issue: "Can't write to data files"
**Solution**:
1. Run the app as Administrator (right-click → Run as Administrator)
2. Check folder permissions
3. Ensure antivirus isn't blocking file writes

### Issue: "No console output"
**Solution**:
All output is in `file_explorer.log` - this is intentional for better debugging!

## 📊 Data File Structure

### favorites.json
```json
[
  "C:\\Path\\To\\Folder1",
  "C:\\Path\\To\\Folder2"
]
```

### settings.json
```json
{
  "theme": "liquid_glass",
  "font_size": 11,
  "view_mode": "list"
}
```

### history.json
```json
[
  {
    "path": "C:\\Users\\Name\\Documents",
    "timestamp": "2025-10-27T10:30:45.123456"
  }
]
```

## 🎯 Testing Checklist

- [ ] Add a favorite (right-click or Ctrl+D)
- [ ] See popup confirmation
- [ ] Favorite appears in sidebar
- [ ] Favorite persists after restart
- [ ] Can click favorite to navigate
- [ ] Can remove favorite with × button
- [ ] Check `data/favorites.json` has content
- [ ] Check `file_explorer.log` for activity

## 📞 Still Having Issues?

1. **Delete the `data/` folder** and restart the app (it will recreate)
2. **Check the log file** for specific error messages
3. **Verify Python version** (should be Python 3.7+)
4. **Check dependencies**: `pip install PyQt6 send2trash`

## 🎉 Everything Working?

Great! Here's what you can do:
- Favorite your most-used folders
- Use Ctrl+D for quick favoriting
- Navigation history is tracked automatically
- All your settings are saved
- Enjoy the beautiful liquid glass UI!

---

**Last Updated**: October 27, 2025
**Status**: ✅ Favorites Fully Functional
