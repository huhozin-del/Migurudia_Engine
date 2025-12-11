"""Global settings and application state management"""

import customtkinter as ctk

# CustomTkinter initial settingh
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# colour constant
COLORS = {
    "primary": "#648CFF",
    "primary_hover": "#466EDC",
    "error": "#FF5555",
}

# preveiw window defult size
DEFAULT_PREVIEW_WIDTH = 640
DEFAULT_PREVIEW_HEIGHT = 360


class AppState:
    """Global application state management"""
    
    def __init__(self):
        self.current_lang = "en"
        self.current_file_path = None
        self.is_running = False
        self.current_process = None
        self.preview_width = DEFAULT_PREVIEW_WIDTH
        self.preview_height = DEFAULT_PREVIEW_HEIGHT
        self.pygame_embed_window_id = None
        
        # UI asset call back
        self._ui_callbacks = {}
    
    def register_callback(self, name: str, callback):
        """register UI callback"""
        self._ui_callbacks[name] = callback
    
    def call(self, name: str, *args, **kwargs):
        """use registered callback"""
        if name in self._ui_callbacks:
            return self._ui_callbacks[name](*args, **kwargs)
    
    def reset_runtime_state(self):
        """reset runtime state"""
        self.is_running = False
        self.current_process = None


# global state instance
state = AppState()
