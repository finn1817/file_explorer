"""
Data Manager for File Explorer
Handles all CRUD operations for JSON data files
"""

import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class DataManager:
    """Manage all application data with CRUD operations"""
    # Instance attribute type hints
    _folder_sizes_cache: Dict[str, Any]
    _folder_sizes_loaded: bool
    
    def __init__(self, app_dir: Optional[Path] = None):
        """Initialize the data manager
        
        Args:
            app_dir: Application directory path. If None, uses parent of script directory
        """
        # Get the app-code directory (parent of python folder)
        if app_dir is None:
            app_dir = Path(__file__).parent.parent
        
        self.app_dir = app_dir
        self.data_dir = self.app_dir / 'data'
        
        # Ensure data directory exists
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Define all data files
        self.files = {
            'favorites': self.data_dir / 'favorites.json',
            'settings': self.data_dir / 'settings.json',
            'history': self.data_dir / 'history.json',
            'bookmarks': self.data_dir / 'bookmarks.json',
            'recent_files': self.data_dir / 'recent_files.json',
            'startup': self.data_dir / 'startup.json',  # Side Apps (apps/files to auto-run/open)
            'folder_sizes': self.data_dir / 'folder_sizes.json',  # Cache of computed folder sizes
        }
        
        logger.info(f"DataManager initialized with data directory: {self.data_dir}")
        
        # Initialize all data files
        self._initialize_files()

        # In-memory caches (loaded on first use)
        self._folder_sizes_cache = {}
        self._folder_sizes_loaded = False
    
    def _initialize_files(self):
        """Initialize all data files with default structures"""
        defaults = {
            'favorites': [],
            'settings': {},
            'history': [],
            'bookmarks': {},
            'recent_files': [],
            'startup': [],
            'folder_sizes': {},
        }
        
        for name, filepath in self.files.items():
            if not filepath.exists():
                logger.info(f"Creating new data file: {filepath}")
                self._write_json(filepath, defaults[name])
            else:
                logger.debug(f"Data file exists: {filepath}")
    
    def _read_json(self, filepath: Path, default: Any = None) -> Any:
        """Read JSON file with error handling
        
        Args:
            filepath: Path to JSON file
            default: Default value to return on error
            
        Returns:
            Parsed JSON data or default value
        """
        try:
            if filepath.exists():
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    logger.debug(f"Read {filepath.name}: {len(str(data))} chars")
                    return data
            else:
                logger.warning(f"File not found: {filepath}")
                return default if default is not None else []
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error in {filepath}: {e}")
            return default if default is not None else []
        except Exception as e:
            logger.error(f"Error reading {filepath}: {e}", exc_info=True)
            return default if default is not None else []
    
    def _write_json(self, filepath: Path, data: Any, backup: bool = True) -> bool:
        """Write JSON file with error handling and optional backup
        
        Args:
            filepath: Path to JSON file
            data: Data to write
            backup: Whether to create a backup before writing
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Create backup if requested and file exists
            if backup and filepath.exists():
                backup_path = filepath.with_suffix('.json.bak')
                import shutil
                shutil.copy2(filepath, backup_path)
                logger.debug(f"Created backup: {backup_path}")
            
            # Ensure directory exists
            filepath.parent.mkdir(parents=True, exist_ok=True)
            
            # Write data
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            # Verify write
            if filepath.exists():
                size = filepath.stat().st_size
                logger.info(f"✅ Wrote {filepath.name}: {size} bytes")
                return True
            else:
                logger.error(f"❌ File not created: {filepath}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Error writing {filepath}: {e}", exc_info=True)
            return False
    
    # ==================== FAVORITES CRUD ====================
    
    def get_favorites(self) -> List[str]:
        """Get all favorites"""
        favorites = self._read_json(self.files['favorites'], [])
        # Validate - ensure all items are strings
        return [f for f in favorites if isinstance(f, str)]
    
    def add_favorite(self, path: str) -> bool:
        """Add a path to favorites
        
        Args:
            path: Path to add
            
        Returns:
            True if added successfully, False if already exists or error
        """
        logger.info(f"Adding favorite: {path}")
        favorites = self.get_favorites()
        
        if path in favorites:
            logger.warning(f"Path already in favorites: {path}")
            return False
        
        favorites.append(path)
        success = self._write_json(self.files['favorites'], favorites)
        
        if success:
            logger.info(f"✅ Added favorite: {path}")
        return success
    
    def remove_favorite(self, path: str) -> bool:
        """Remove a path from favorites
        
        Args:
            path: Path to remove
            
        Returns:
            True if removed, False if not found or error
        """
        logger.info(f"Removing favorite: {path}")
        favorites = self.get_favorites()
        
        if path not in favorites:
            logger.warning(f"Path not in favorites: {path}")
            return False
        
        favorites.remove(path)
        success = self._write_json(self.files['favorites'], favorites)
        
        if success:
            logger.info(f"✅ Removed favorite: {path}")
        return success
    
    def clear_favorites(self) -> bool:
        """Clear all favorites"""
        logger.info("Clearing all favorites")
        return self._write_json(self.files['favorites'], [])
    
    def is_favorite(self, path: str) -> bool:
        """Check if path is in favorites"""
        return path in self.get_favorites()
    
    # ==================== SETTINGS CRUD ====================
    
    def get_settings(self) -> Dict[str, Any]:
        """Get all settings"""
        return self._read_json(self.files['settings'], {})
    
    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a specific setting
        
        Args:
            key: Setting key
            default: Default value if key doesn't exist
            
        Returns:
            Setting value or default
        """
        settings = self.get_settings()
        return settings.get(key, default)
    
    def set_setting(self, key: str, value: Any) -> bool:
        """Set a specific setting
        
        Args:
            key: Setting key
            value: Setting value
            
        Returns:
            True if successful
        """
        logger.info(f"Setting {key} = {value}")
        settings = self.get_settings()
        settings[key] = value
        return self._write_json(self.files['settings'], settings)
    
    def update_settings(self, new_settings: Dict[str, Any]) -> bool:
        """Update multiple settings
        
        Args:
            new_settings: Dictionary of settings to update
            
        Returns:
            True if successful
        """
        logger.info(f"Updating {len(new_settings)} settings")
        settings = self.get_settings()
        settings.update(new_settings)
        return self._write_json(self.files['settings'], settings)
    
    def clear_settings(self) -> bool:
        """Clear all settings"""
        logger.info("Clearing all settings")
        return self._write_json(self.files['settings'], {})
    
    # ==================== HISTORY CRUD ====================
    
    def get_history(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get navigation history
        
        Args:
            limit: Maximum number of items to return
            
        Returns:
            List of history entries
        """
        history = self._read_json(self.files['history'], [])
        if limit:
            return history[-limit:]
        return history
    
    def add_history(self, path: str) -> bool:
        """Add a path to history
        
        Args:
            path: Path to add
            
        Returns:
            True if successful
        """
        history = self.get_history()
        
        entry = {
            'path': path,
            'timestamp': datetime.now().isoformat(),
        }
        
        history.append(entry)
        
        # Keep only last 100 entries
        if len(history) > 100:
            history = history[-100:]
        
        return self._write_json(self.files['history'], history)
    
    def clear_history(self) -> bool:
        """Clear all history"""
        logger.info("Clearing history")
        return self._write_json(self.files['history'], [])
    
    # ==================== BOOKMARKS CRUD ====================
    
    def get_bookmarks(self) -> Dict[str, str]:
        """Get all bookmarks (name -> path mapping)"""
        return self._read_json(self.files['bookmarks'], {})
    
    def add_bookmark(self, name: str, path: str) -> bool:
        """Add a bookmark
        
        Args:
            name: Bookmark name
            path: Path to bookmark
            
        Returns:
            True if successful
        """
        logger.info(f"Adding bookmark: {name} -> {path}")
        bookmarks = self.get_bookmarks()
        bookmarks[name] = path
        return self._write_json(self.files['bookmarks'], bookmarks)
    
    def remove_bookmark(self, name: str) -> bool:
        """Remove a bookmark
        
        Args:
            name: Bookmark name to remove
            
        Returns:
            True if successful
        """
        logger.info(f"Removing bookmark: {name}")
        bookmarks = self.get_bookmarks()
        
        if name in bookmarks:
            del bookmarks[name]
            return self._write_json(self.files['bookmarks'], bookmarks)
        
        return False
    
    def clear_bookmarks(self) -> bool:
        """Clear all bookmarks"""
        logger.info("Clearing all bookmarks")
        return self._write_json(self.files['bookmarks'], {})
    
    # ==================== RECENT FILES CRUD ====================
    
    def get_recent_files(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get recent files
        
        Args:
            limit: Maximum number of items to return
            
        Returns:
            List of recent file entries
        """
        recent = self._read_json(self.files['recent_files'], [])
        if limit:
            return recent[-limit:]
        return recent
    
    def add_recent_file(self, path: str) -> bool:
        """Add a file to recent files
        
        Args:
            path: File path
            
        Returns:
            True if successful
        """
        recent = self.get_recent_files()
        
        # Remove if already exists (to move to end)
        recent = [r for r in recent if r.get('path') != path]
        
        entry = {
            'path': path,
            'timestamp': datetime.now().isoformat(),
        }
        
        recent.append(entry)
        
        # Keep only last 50 entries
        if len(recent) > 50:
            recent = recent[-50:]
        
        return self._write_json(self.files['recent_files'], recent)
    
    def clear_recent_files(self) -> bool:
        """Clear all recent files"""
        logger.info("Clearing recent files")
        return self._write_json(self.files['recent_files'], [])
    
    # ==================== UTILITY METHODS ====================
    
    def export_all_data(self, export_path: Path) -> bool:
        """Export all data to a single JSON file
        
        Args:
            export_path: Path to export file
            
        Returns:
            True if successful
        """
        try:
            all_data = {
                'favorites': self.get_favorites(),
                'settings': self.get_settings(),
                'history': self.get_history(),
                'bookmarks': self.get_bookmarks(),
                'recent_files': self.get_recent_files(),
                'export_date': datetime.now().isoformat(),
            }
            
            with open(export_path, 'w', encoding='utf-8') as f:
                json.dump(all_data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"✅ Exported all data to: {export_path}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error exporting data: {e}", exc_info=True)
            return False
    
    def import_all_data(self, import_path: Path, merge: bool = False) -> bool:
        """Import data from a JSON file
        
        Args:
            import_path: Path to import file
            merge: If True, merge with existing data; if False, replace
            
        Returns:
            True if successful
        """
        try:
            with open(import_path, 'r', encoding='utf-8') as f:
                imported = json.load(f)
            
            if merge:
                # Merge data
                current_favs = self.get_favorites()
                current_favs.extend(imported.get('favorites', []))
                self._write_json(self.files['favorites'], list(set(current_favs)))
                
                current_settings = self.get_settings()
                current_settings.update(imported.get('settings', {}))
                self._write_json(self.files['settings'], current_settings)
            else:
                # Replace data
                for key in ['favorites', 'settings', 'history', 'bookmarks', 'recent_files']:
                    if key in imported and key in self.files:
                        self._write_json(self.files[key], imported[key])
            
            logger.info(f"✅ Imported data from: {import_path}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error importing data: {e}", exc_info=True)
            return False
    
    def get_data_stats(self) -> Dict[str, Any]:
        """Get statistics about stored data"""
        stats = {}
        
        for name, filepath in self.files.items():
            if filepath.exists():
                size = filepath.stat().st_size
                stats[name] = {
                    'file': str(filepath),
                    'size_bytes': size,
                    'exists': True,
                }
            else:
                stats[name] = {
                    'file': str(filepath),
                    'exists': False,
                }
        
        return stats

    # ==================== STARTUP (SIDE APPS) ====================

    def get_startup_apps(self) -> List[str]:
        """Return list of app/file/folder paths to run/open on app start."""
        items = self._read_json(self.files['startup'], [])
        # ensure list of strings
        return [p for p in items if isinstance(p, str)]

    def add_startup_app(self, path: str) -> bool:
        """Add a path to startup list (idempotent)."""
        items = self.get_startup_apps()
        if path in items:
            return False
        items.append(path)
        return self._write_json(self.files['startup'], items)

    def remove_startup_app(self, path: str) -> bool:
        """Remove a path from startup list if present."""
        items = self.get_startup_apps()
        if path not in items:
            return False
        items = [p for p in items if p != path]
        return self._write_json(self.files['startup'], items)

    def clear_startup_apps(self) -> bool:
        """Clear the startup list."""
        return self._write_json(self.files['startup'], [])

    # ==================== FOLDER SIZE CACHE ====================

    def _folder_sizes_all(self) -> Dict[str, Any]:
        """Return the in-memory folder sizes cache, loading from disk once on first access."""
        if not getattr(self, '_folder_sizes_loaded', False):
            # Load once to avoid repeated disk reads during view painting
            self._folder_sizes_cache = self._read_json(self.files['folder_sizes'], {}) or {}
            self._folder_sizes_loaded = True
        return self._folder_sizes_cache

    def get_folder_size_cached(self, path: str) -> Optional[int]:
        """Return cached folder size in bytes if present and still valid.

        We treat cache as valid if the on-disk mtime of the folder matches
        what we stored. If mtime differs, the cache is considered stale.
        """
        try:
            data = self._folder_sizes_all()
            rec = data.get(path)
            if not isinstance(rec, dict):
                return None
            size = rec.get('size')
            mtime_recorded = rec.get('mtime')
            if size is None or mtime_recorded is None:
                return None
            # Validate against current mtime
            from os.path import getmtime, exists
            if not exists(path):
                return None
            mtime_now = getmtime(path)
            if abs(float(mtime_now) - float(mtime_recorded)) > 0.001:
                return None
            return int(size)
        except Exception:
            return None

    def set_folder_size_cached(self, path: str, size: int) -> bool:
        """Write folder size and current mtime to cache without re-reading from disk each time.

        Optimizations:
        - Uses in-memory cache to avoid frequent disk reads in hot paths (e.g., view painting).
        - Skips disk write if the cached value is already up to date.
        """
        try:
            data = self._folder_sizes_all()
            from os.path import getmtime, exists
            mtime_now = getmtime(path) if exists(path) else 0.0
            new_rec = {
                'size': int(size),
                'mtime': float(mtime_now),
                'updated': datetime.now().isoformat(),
            }

            # If unchanged, avoid disk write
            old = data.get(path)
            if (
                isinstance(old, dict)
                and int(old.get('size', -1)) == new_rec['size']
                and float(old.get('mtime', -1.0)) == new_rec['mtime']
            ):
                return True

            data[path] = new_rec
            # Persist current in-memory cache
            return self._write_json(self.files['folder_sizes'], data)
        except Exception:
            return False
