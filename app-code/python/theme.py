import platform
from styles import LightStyle, DarkStyle, LiquidGlassStyle

# Windows imports for blur effects
if platform.system() == "Windows":
    try:
        import ctypes
        from ctypes import wintypes
    except ImportError:
        ctypes = None
else:
    ctypes = None


class Theme:
    """Base theme class with metadata and behavior"""
    
    def __init__(self, name, display_name, icon, style_class, has_blur=False):
        self.name = name
        self.display_name = display_name
        self.icon = icon
        self.style_class = style_class
        self.has_blur = has_blur  # Whether to enable Windows blur effect
        
    def get_stylesheet(self):
        """Get the stylesheet for this theme"""
        return self.style_class.get_stylesheet()


class ThemeManager:
    """Manages theme switching, window effects, and theme behaviors"""
    
    # Define all available themes
    THEMES = {
        'light': Theme(
            name='light',
            display_name='Light Theme',
            icon='☀️',
            style_class=LightStyle,
            has_blur=False
        ),
        'dark': Theme(
            name='dark',
            display_name='Dark Theme',
            icon='🌙',
            style_class=DarkStyle,
            has_blur=False
        ),
        'liquid_glass': Theme(
            name='liquid_glass',
            display_name='Liquid Glass Theme',
            icon='✨',
            style_class=LiquidGlassStyle,
            has_blur=True  # Enable blur effect for liquid glass
        )
    }
    
    def __init__(self, default_theme='liquid_glass'):
        """Initialize theme manager with default theme"""
        self.current_theme_name = default_theme
        self.is_windows = platform.system() == "Windows"
        self.window = None  # Will be set when applying theme
        
    @property
    def current_theme(self):
        """Get the current theme object"""
        return self.THEMES[self.current_theme_name]
        
    def get_current_stylesheet(self):
        """Get the current theme's stylesheet"""
        return self.current_theme.get_stylesheet()
        
    def set_theme(self, theme_name):
        """Set the active theme by name"""
        if theme_name in self.THEMES:
            self.current_theme_name = theme_name
            return True
        return False
        
    def get_available_themes(self):
        """Get list of available theme names"""
        return list(self.THEMES.keys())
        
    def get_theme_info(self, theme_name):
        """Get theme metadata"""
        if theme_name in self.THEMES:
            theme = self.THEMES[theme_name]
            return {
                'name': theme.name,
                'display_name': theme.display_name,
                'icon': theme.icon,
                'has_blur': theme.has_blur
            }
        return None
        
    def apply_theme(self, window, theme_name=None):
        """
        Apply theme to a window
        - Sets stylesheet
        - Applies window effects (blur, etc.)
        """
        if theme_name:
            self.set_theme(theme_name)
            
        self.window = window
        
        # Apply stylesheet
        window.setStyleSheet(self.get_current_stylesheet())
        
        # Apply window effects based on theme
        self._apply_window_effects(window)
        
    def _apply_window_effects(self, window):
        """Apply theme-specific window effects"""
        theme = self.current_theme
        
        if theme.has_blur and self.is_windows:
            # Enable Windows blur effect for themes that support it
            self._enable_windows_blur(window)
        else:
            # Disable blur effect
            self._disable_windows_blur(window)
            
    def _enable_windows_blur(self, window):
        """Enable Windows 11 Acrylic blur effect on title bar"""
        if not self.is_windows or not ctypes:
            return
            
        try:
            from PyQt6.QtCore import QTimer
            
            # Use QTimer to ensure window is fully initialized
            QTimer.singleShot(100, lambda: self._apply_blur_effect(window))
        except Exception as e:
            print(f"Could not schedule blur effect: {e}")
            
    def _apply_blur_effect(self, window):
        """Actually apply the blur effect (called after window is ready)"""
        if not self.is_windows or not ctypes:
            return
            
        try:
            hwnd = int(window.winId())
            
            # Windows 11 DWM attributes
            DWMWA_USE_IMMERSIVE_DARK_MODE = 20
            DWMWA_SYSTEMBACKDROP_TYPE = 38
            
            # Backdrop types
            DWMSBT_TRANSIENTWINDOW = 3  # Acrylic blur effect
            
            dwmapi = ctypes.windll.dwmapi
            
            # Enable dark mode for title bar
            use_dark = ctypes.c_int(1)
            dwmapi.DwmSetWindowAttribute(
                hwnd,
                DWMWA_USE_IMMERSIVE_DARK_MODE,
                ctypes.byref(use_dark),
                ctypes.sizeof(use_dark)
            )
            
            # Enable Acrylic blur effect on title bar
            backdrop_type = ctypes.c_int(DWMSBT_TRANSIENTWINDOW)
            dwmapi.DwmSetWindowAttribute(
                hwnd,
                DWMWA_SYSTEMBACKDROP_TYPE,
                ctypes.byref(backdrop_type),
                ctypes.sizeof(backdrop_type)
            )
            
            print(f"✨ Blur effect enabled for {self.current_theme.display_name}")
            
        except Exception as e:
            print(f"Could not enable blur effect: {e}")
            
    def _disable_windows_blur(self, window):
        """Disable Windows blur effect"""
        if not self.is_windows or not ctypes:
            return
            
        try:
            hwnd = int(window.winId())
            DWMWA_SYSTEMBACKDROP_TYPE = 38
            DWMSBT_NONE = 1
            
            dwmapi = ctypes.windll.dwmapi
            backdrop_type = ctypes.c_int(DWMSBT_NONE)
            dwmapi.DwmSetWindowAttribute(
                hwnd,
                DWMWA_SYSTEMBACKDROP_TYPE,
                ctypes.byref(backdrop_type),
                ctypes.sizeof(backdrop_type)
            )
            
        except Exception as e:
            print(f"Could not disable blur effect: {e}")
            
    def get_theme_display_info(self):
        """Get current theme display information"""
        theme = self.current_theme
        return f"{theme.icon} {theme.display_name}"