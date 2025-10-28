# 🚀 Executable and script support

## ✨ What's New

You can open files easily as usual, and for executables and scripts we add a confirmation step before running them.

## 📋 Supported File Types

### ⚙️ Executables
- `.exe` – Windows executables
- `.msi` – Windows installers

### ⚡ Batch / command
- `.bat`, `.cmd`

### 💻 PowerShell
- `.ps1` (runs with ExecutionPolicy Bypass on Windows)

### 🐍 Python
- `.py`, `.pyw`

### 📜 Other
- `.vbs` (VBScript)
- `.sh` (Linux/Mac)

### 🔗 Shortcuts
- `.lnk` – Windows shortcuts (displayed with 🔗)

## 🎨 Icons

### All File Types Now Have Custom Icons:

**Documents:**
- 📄 `.txt`, `.doc`, `.docx`, `.rtf`, `.odt`
- 📝 `.md` (Markdown)
- 📕 `.pdf`

**Images:**
- 🖼️ `.jpg`, `.png`, `.gif`, `.bmp`, `.svg`, `.ico`, `.webp`

**Videos:**
- 🎥 `.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv`, `.flv`, `.webm`

**Audio:**
- 🎵 `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.wma`, `.m4a`

**Archives:**
- 📦 `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`, `.xz`

**Programming:**
- 🐍 Python (`.py`, `.pyw`, `.pyc`)
- 📜 JavaScript (`.js`)
- 📘 TypeScript (`.ts`)
- ⚛️ React (`.jsx`, `.tsx`)
- ☕ Java (`.java`, `.class`, `.jar`)
- ©️ C/C++ (`.c`, `.cpp`, `.h`, `.hpp`)
- #️⃣ C# (`.cs`)
- 🐹 Go (`.go`)
- 🦀 Rust (`.rs`)
- 💎 Ruby (`.rb`)
- 🐘 PHP (`.php`)

**Web:**
- 🌐 HTML (`.html`, `.htm`)
- 🎨 CSS (`.css`, `.scss`, `.sass`, `.less`)

**Data:**
- 📋 JSON, XML, YAML
- 📊 Excel (`.xlsx`, `.xls`, `.csv`)
- 🗄️ Database (`.sql`, `.db`, `.sqlite`)

**Configuration:**
- ⚙️ Config files (`.ini`, `.cfg`, `.conf`, `.toml`)
- 🔐 Environment (`.env`)
- 🔧 Registry (`.reg`)

**Other:**
- 💿 Disk images (`.iso`, `.img`)
- 🔌 Libraries (`.dll`, `.so`)

Note: by default the app does not create `.pyc` files when you run it from `run.bat`.

## 🎯 How to use

### Method 1: Right‑click menu
1. Right-click on any executable file (.exe, .bat, .py, etc.)
2. Click "▶️ Run"
3. Confirm you want to run it
4. The file executes!

### Method 2: From favorites
1. Add an executable to favorites (right-click → "⭐ Add to Favorites")
2. It appears in the sidebar with the correct icon (⚙️, ⚡, or 🐍)
3. Click the favorite
4. Confirm you want to run it
5. Done!

### Method 3: Double‑click
- Double-click any file
- If it's an executable, you'll be asked to confirm
- If it's a regular file, it opens with the default application

## 🔒 Safety

### Confirm before run
Every executable requires confirmation before running:
```
Are you sure you want to run this executable?

📄 shutdown.exe
📁 C:\Users\danny\Desktop\Power Options

⚠️ Only run files you trust!
```

### Logging
All executions are logged:
```
2025-10-27 21:30:00 - INFO - User confirmed - running: C:\path\to\file.exe
2025-10-27 21:30:01 - INFO - Successfully executed: file.exe
```

### Status bar feedback
- ✅ "Launched: shutdown.exe"
- ✅ "Running Python script: my_script.py"
- ❌ "Failed to run file.exe: Permission denied"

## 💡 Details per type (Windows)

### Python scripts
- Launched with `python` (or `python3` on non‑Windows).
- If you run from `run.bat`, `.pyc` won’t be created.

### PowerShell scripts
- Run with `-ExecutionPolicy Bypass`.
- You’ll always get a confirmation dialog first.

### Batch files
- Run in a new Command Prompt window.

### Shortcuts (.lnk)
- Shown with 🔗 icon and open the target.

## 🎪 Examples

### Example 1: Shutdown Shortcut
```
1. Find shutdown.exe in C:\Windows\System32
2. Create shortcut on Desktop
3. Favorite the shortcut in File Explorer
4. Click the favorite to run shutdown options
```

### Example 2: Python Script
```python
# my_script.py
print("Hello from Liquid Glass File Explorer!")
input("Press Enter to continue...")
```
1. Favorite `my_script.py`
2. Click the favorite
3. Confirm to run
4. See output in new window

### Example 3: Batch File
```batch
@echo off
echo This is running from File Explorer!
pause
```
1. Save as `test.bat`
2. Right-click → "▶️ Run"
3. See the output

## 🔍 Troubleshooting

### "Failed to run..."
**Solution**: Check if:
- File still exists
- You have permission to run it
- Python is installed (for .py files)
- File is not corrupted

### Python scripts don’t run
• Ensure Python is installed and on PATH. Try `python --version`.

### PowerShell scripts blocked
The app uses `-ExecutionPolicy Bypass`. If you still get a policy error, open PowerShell as Administrator and retry.

### Icons not showing correctly
- Restart the app and verify the file extension.

## 🎉 Summary
• Open files with their default apps.
• Run executables and scripts with a confirmation step.
• Shortcuts resolve to their targets.
• Logging records what happened if you need to debug.
