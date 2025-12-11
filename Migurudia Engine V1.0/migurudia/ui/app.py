"""main application file for Migurdia"""

import sys
import platform
import tkinter as tk
import customtkinter as ctk

from config import state
from .home_frame import HomeFrame
from .editor_frame import EditorFrame
from .tutorial_frame import TutorialFrame


class ConsoleRedirect:
    """console output redirector to Text widget"""

    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert("end", text)
        self.widget.see("end")

    def flush(self):
        pass


class MigurdiaApp(ctk.CTk):
    """Migurudia main application class"""

    def __init__(self):
        super().__init__()

        self.title("Migurudia V1.0")
        self.geometry("1280x720")
        self.minsize(854, 480)

        self._setup_icon()
        self._setup_dpi()
        self._create_frames()
        self._setup_console_redirect()

        # show home frame initially
        self.show_home()

    def _setup_icon(self):
        """setup application icon"""
        try:
            self.iconbitmap("assets/migurudia.ico")
        except:
            try:
                icon = tk.PhotoImage(file="assets/migurudia.png")
                self.iconphoto(True, icon)
            except:
                pass
    #cnmd microsoft
    def _setup_dpi(self):
        """setup DPI awareness for Windows"""
        if platform.system() == "Windows":
            try:
                from ctypes import windll
                windll.shcore.SetProcessDpiAwareness(1)
            except:
                pass

    def _create_frames(self):
        """create all main frames and their callbacks"""
        # home callbacks
        home_callbacks = {
            "on_create": self.show_editor,
            "on_load": self._load_and_open_editor,
            "on_import": self._import_and_open_editor,
            "on_tutorial": self.show_tutorial,
            "on_language_change": self._update_all_languages,
        }

        # editor callbacks
        editor_callbacks = {
            "on_exit": self.show_home,
        }

        # tutorial callbacks
        tutorial_callbacks = {
            "on_exit": self.show_home,
        }

        # Create Frame
        self.home_frame = HomeFrame(self, home_callbacks)
        self.editor_frame = EditorFrame(self, editor_callbacks)
        self.tutorial_frame = TutorialFrame(self, tutorial_callbacks)

    def _setup_console_redirect(self):
        """redirect stdout and stderr to console widget"""
        sys.stdout = ConsoleRedirect(self.editor_frame.console)
        sys.stderr = ConsoleRedirect(self.editor_frame.console)

    def show_home(self):
        """show home frame"""
        self.editor_frame.pack_forget()
        self.tutorial_frame.pack_forget()
        self.home_frame.pack(fill="both", expand=True)

    def show_editor(self):
        """show editor frame"""
        self.home_frame.pack_forget()
        self.tutorial_frame.pack_forget()
        self.editor_frame.pack(fill="both", expand=True)
        self.editor_frame.on_show()

    def show_tutorial(self):
        """show tutorial frame"""
        self.home_frame.pack_forget()
        self.editor_frame.pack_forget()
        self.tutorial_frame.pack(fill="both", expand=True)
        self.tutorial_frame.on_show()

    def _load_and_open_editor(self):
        """load code from file and open editor"""
        from tkinter import filedialog
        import os

        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Python Files", "*.py"),
                ("Migurudia Project", "*.migu"),
                ("All Files", "*.*")
            ],
            title="Open File"
        )

        if not file_path:
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()

            # change to editor frame
            self.show_editor()

            # load code into editor
            self.editor_frame.textbox.delete("1.0", "end")
            self.editor_frame.textbox.insert("1.0", code)
            state.current_file_path = file_path
            self.title(f"Migurudia V0.1 - {os.path.basename(file_path)}")
            self.editor_frame._update_editor()

            print(f"[Loaded] {file_path}")

        except Exception as e:
            print(f"[Error] Load failed: {e}")

    def _import_and_open_editor(self):
        """import assets and open editor"""
        from tkinter import filedialog
        from file_ops.asset_import import _insert_asset_code

        file_paths = filedialog.askopenfilenames(
            filetypes=[
                ("All Assets", "*.png *.jpg *.jpeg *.gif *.bmp *.wav *.mp3 *.ogg"),
                ("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp"),
                ("Audio Files", "*.wav *.mp3 *.ogg"),
                ("All Files", "*.*")
            ],
            title="Import Assets"
        )

        if not file_paths:
            return

        # change to editor frame
        self.show_editor()

        # insert asset code into editor
        _insert_asset_code(
            self.editor_frame.textbox,
            file_paths,
            self.editor_frame._update_editor
        )

    def _update_all_languages(self):
        """update language in all frames"""
        self.home_frame.update_language()
        self.editor_frame.update_language()
        self.tutorial_frame.update_language()
