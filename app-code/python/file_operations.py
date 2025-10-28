import os
import shutil
import subprocess
import platform
from send2trash import send2trash
from pathlib import Path
from typing import Optional, Tuple

class FileOperations:
    """Handle all file system operations"""
    
    def __init__(self):
        self.system = platform.system()
    
    def open_file(self, path):
        """Open file with default application"""
        try:
            if self.system == "Windows":
                os.startfile(path)
            elif self.system == "Darwin":  # macOS
                subprocess.run(["open", path])
            else:  # Linux
                subprocess.run(["xdg-open", path])
            return True
        except Exception as e:
            print(f"Error opening file: {e}")
            return False
    
    def create_folder(self, path):
        """Create a new folder"""
        try:
            os.makedirs(path, exist_ok=False)
            return True
        except Exception as e:
            print(f"Error creating folder: {e}")
            return False
    
    def copy_item(self, source, destination):
        """Copy file or folder"""
        try:
            if os.path.isfile(source):
                # Handle file name conflicts
                if os.path.exists(destination):
                    base, ext = os.path.splitext(destination)
                    counter = 1
                    while os.path.exists(f"{base} - Copy{f' ({counter})' if counter > 1 else ''}{ext}"):
                        counter += 1
                    destination = f"{base} - Copy{f' ({counter})' if counter > 1 else ''}{ext}"
                
                shutil.copy2(source, destination)
            elif os.path.isdir(source):
                # Handle folder name conflicts
                if os.path.exists(destination):
                    counter = 1
                    base_dest = destination
                    while os.path.exists(f"{base_dest} - Copy{f' ({counter})' if counter > 1 else ''}"):
                        counter += 1
                    destination = f"{base_dest} - Copy{f' ({counter})' if counter > 1 else ''}"
                
                shutil.copytree(source, destination)
            return True
        except Exception as e:
            print(f"Error copying item: {e}")
            return False
    
    def move_item(self, source, destination):
        """Move file or folder"""
        try:
            # Handle name conflicts
            if os.path.exists(destination):
                base, ext = os.path.splitext(destination)
                counter = 1
                while os.path.exists(f"{base} ({counter}){ext}"):
                    counter += 1
                destination = f"{base} ({counter}){ext}"
            
            shutil.move(source, destination)
            return True
        except Exception as e:
            print(f"Error moving item: {e}")
            return False
    
    def rename_item(self, old_path, new_path):
        """Rename file or folder"""
        try:
            os.rename(old_path, new_path)
            return True
        except Exception as e:
            print(f"Error renaming item: {e}")
            return False
    
    def delete_item(self, path):
        """Delete file or folder (send to trash)"""
        try:
            send2trash(path)
            return True
        except Exception as e:
            print(f"Error deleting item: {e}")
            # Fallback to permanent deletion
            try:
                if os.path.isfile(path):
                    os.remove(path)
                elif os.path.isdir(path):
                    shutil.rmtree(path)
                return True
            except Exception as e2:
                print(f"Error with permanent deletion: {e2}")
                return False
    
    def get_file_size(self, path):
        """Get file size in bytes"""
        try:
            if os.path.isfile(path):
                return os.path.getsize(path)
            elif os.path.isdir(path):
                total_size = 0
                for dirpath, dirnames, filenames in os.walk(path):
                    for filename in filenames:
                        filepath = os.path.join(dirpath, filename)
                        try:
                            total_size += os.path.getsize(filepath)
                        except:
                            pass
                return total_size
        except:
            return 0
    
    def format_file_size(self, size_bytes):
        """Format file size in human readable format"""
        if size_bytes == 0:
            return "0 B"
        
        size_names = ["B", "KB", "MB", "GB", "TB"]
        import math
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return f"{s} {size_names[i]}"
    
    def get_file_icon(self, path):
        """Get appropriate icon for file type"""
        if os.path.isdir(path):
            return "📁"
        
        ext = os.path.splitext(path)[1].lower()
        
        icon_map = {
            # Documents
            '.txt': '📄', '.doc': '📄', '.docx': '📄', '.pdf': '📕',
            '.rtf': '📄', '.odt': '📄', '.md': '📝',
            
            # Images
            '.jpg': '🖼️', '.jpeg': '🖼️', '.png': '🖼️', '.gif': '🖼️', 
            '.bmp': '🖼️', '.svg': '🖼️', '.ico': '🖼️', '.webp': '🖼️',
            
            # Videos
            '.mp4': '🎥', '.avi': '🎥', '.mov': '🎥', '.mkv': '🎥',
            '.wmv': '🎥', '.flv': '🎥', '.webm': '🎥',
            
            # Audio
            '.mp3': '🎵', '.wav': '🎵', '.flac': '🎵', '.aac': '🎵',
            '.ogg': '🎵', '.wma': '🎵', '.m4a': '🎵',
            
            # Archives
            '.zip': '📦', '.rar': '📦', '.7z': '📦', '.tar': '📦',
            '.gz': '📦', '.bz2': '📦', '.xz': '📦',
            
            # Executables & Scripts
            '.exe': '⚙️', '.msi': '⚙️', '.app': '⚙️',
            '.bat': '⚡', '.cmd': '⚡', '.sh': '⚡',
            '.ps1': '💻', '.vbs': '📜', '.reg': '🔧',
            '.lnk': '🔗',  # Shortcuts
            
            # Programming
            '.py': '🐍', '.pyc': '🐍', '.pyw': '🐍',
            '.js': '📜', '.ts': '📘', '.jsx': '⚛️', '.tsx': '⚛️',
            '.java': '☕', '.class': '☕', '.jar': '☕',
            '.c': '©️', '.cpp': '©️', '.h': '©️', '.hpp': '©️',
            '.cs': '#️⃣', '.go': '🐹', '.rs': '🦀', '.rb': '💎',
            '.php': '🐘', '.swift': '🦅', '.kt': '🅺',
            
            # Web
            '.html': '🌐', '.htm': '🌐', '.css': '🎨', 
            '.scss': '🎨', '.sass': '🎨', '.less': '🎨',
            
            # Data
            '.json': '📋', '.xml': '📋', '.yaml': '📋', '.yml': '📋',
            '.csv': '📊', '.xlsx': '📊', '.xls': '📊',
            '.sql': '🗄️', '.db': '🗄️', '.sqlite': '🗄️',
            
            # Config
            '.ini': '⚙️', '.cfg': '⚙️', '.conf': '⚙️',
            '.toml': '⚙️', '.env': '🔐',
            
            # Others
            '.iso': '💿', '.img': '💿',
            '.dll': '🔌', '.so': '🔌',
        }
        
        return icon_map.get(ext, '📄')
    
    def is_executable(self, path):
        """Check if a file is executable (exe, bat, cmd, ps1, py, lnk)"""
        if os.path.isdir(path):
            return False
        
        ext = os.path.splitext(path)[1].lower()
        executable_extensions = ['.exe', '.bat', '.cmd', '.ps1', '.vbs', '.py', '.pyw', '.lnk', '.msi']
        return ext in executable_extensions
    
    def run_executable(self, path):
        """Run an executable file with proper handling"""
        try:
            ext = os.path.splitext(path)[1].lower()
            
            if self.system == "Windows":
                if ext in ['.exe', '.bat', '.cmd', '.lnk', '.msi']:
                    # Run directly with startfile (opens in default way)
                    os.startfile(path)
                    return True, f"Launched: {os.path.basename(path)}"
                
                elif ext == '.ps1':
                    # PowerShell script
                    subprocess.Popen(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', path])
                    return True, f"Running PowerShell script: {os.path.basename(path)}"
                
                elif ext == '.vbs':
                    # VBScript
                    subprocess.Popen(['wscript.exe', path])
                    return True, f"Running VBScript: {os.path.basename(path)}"
                
                elif ext in ['.py', '.pyw']:
                    # Python script
                    subprocess.Popen(['python', path])
                    return True, f"Running Python script: {os.path.basename(path)}"
                
                else:
                    # Fallback to startfile
                    os.startfile(path)
                    return True, f"Opened: {os.path.basename(path)}"
            
            else:
                # Linux/Mac
                if ext == '.py':
                    subprocess.Popen(['python3', path])
                    return True, f"Running Python script: {os.path.basename(path)}"
                elif ext == '.sh':
                    subprocess.Popen(['bash', path])
                    return True, f"Running shell script: {os.path.basename(path)}"
                else:
                    subprocess.Popen([path])
                    return True, f"Launched: {os.path.basename(path)}"
                    
        except Exception as e:
            return False, f"Failed to run {os.path.basename(path)}: {str(e)}"
    
    def get_shortcut_target(self, lnk_path):
        """Get the target path of a .lnk shortcut file (Windows only)"""
        try:
            if self.system == "Windows" and lnk_path.endswith('.lnk'):
                import winshell
                return winshell.shortcut(lnk_path).path
        except Exception as e:
            # If winshell not available, return original path
            pass
        return lnk_path

    # -------------------- Shortcuts (Windows) --------------------
    def create_shortcut(self, target_path: str, shortcut_path: str, icon_path: Optional[str] = None) -> Tuple[bool, str]:
        """Create a shortcut pointing to target_path.

        On Windows, tries to create a .lnk via COM. If COM libs are missing,
        falls back to a simple .url file that points to the target.

        Returns (success, message).
        """
        try:
            if self.system != "Windows":
                return False, "Shortcuts are only supported on Windows."

            # Prefer .lnk via COM if available
            try:
                import win32com.client  # type: ignore
                shell = win32com.client.Dispatch('WScript.Shell')
                shortcut = shell.CreateShortcut(shortcut_path)
                shortcut.TargetPath = target_path
                shortcut.WorkingDirectory = os.path.dirname(target_path)
                if icon_path and os.path.exists(icon_path):
                    shortcut.IconLocation = icon_path
                shortcut.Save()
                return True, f"Created shortcut: {os.path.basename(shortcut_path)}"
            except Exception:
                # Fallback: create a .url internet shortcut
                # Works for files/folders using file:/// URI
                uri = Path(target_path).resolve().as_uri()
                content = f"[InternetShortcut]\nURL={uri}\nIconIndex=0\n"
                try:
                    with open(shortcut_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    return True, f"Created URL shortcut: {os.path.basename(shortcut_path)}"
                except Exception as e2:
                    return False, f"Failed to create URL shortcut: {e2}"
        except Exception as e:
            return False, f"Failed to create shortcut: {e}"