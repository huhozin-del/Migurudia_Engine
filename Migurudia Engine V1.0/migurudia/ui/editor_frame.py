"""code Editor Interface"""

import tkinter as tk
from tkinter import Menu
import customtkinter as ctk

from config import state, COLORS, LANGUAGES
from editor import (
    AutoCompletePopup, show_suggestions,
    highlight_code, setup_line_numbers, update_line_numbers
)
from file_ops import (
    save_file, save_file_as, load_file, new_file,
    import_images, import_sounds, import_all_assets,
    export_as_python, export_as_exe
)
from runtime import GameRunner, key_bridge, SPECIAL_KEYS


class EditorFrame(ctk.CTkFrame):
    """Editor Interface Frame"""

    def __init__(self, master, callbacks: dict):
        """
        Initialize the editor interface
        
        Args:
            master: Parent window
            callbacks: Dictionary of callback functions, including:
                - on_exit: Exit editor and return to home page
        """
        super().__init__(master)
        self.master = master
        self.callbacks = callbacks
        self.game_runner = None

        self._setup_ui()
        self._setup_key_bindings()

    def _setup_ui(self):
        """Setup UI layout"""
        # Navigation bar
        self.nav_frame = ctk.CTkFrame(
            self, height=40, fg_color=COLORS["primary"], corner_radius=0
        )
        self.nav_frame.pack(side="top", fill="x")
        self.nav_frame.pack_propagate(False)

        # Main editor area
        self.editor_main = ctk.CTkFrame(self)
        self.editor_main.pack(fill="both", expand=True, padx=5, pady=5)

        # Configure grid
        self.editor_main.grid_columnconfigure(0, weight=2)  # Code editor
        self.editor_main.grid_columnconfigure(1, weight=3)  # Preview + Console
        self.editor_main.grid_rowconfigure(0, weight=1)

        # Code editor area
        self.code_frame = ctk.CTkFrame(self.editor_main, corner_radius=0)
        self.code_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5), pady=0)

        # Right side area (Preview + Console)
        self.right_frame = ctk.CTkFrame(self.editor_main)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 0), pady=0)

        self.right_frame.grid_rowconfigure(0, weight=3)  # Preview
        self.right_frame.grid_rowconfigure(1, weight=1)  # Console
        self.right_frame.grid_columnconfigure(0, weight=1)

        # Preview area
        self._setup_preview()

        # Console
        self.console = ctk.CTkTextbox(self.right_frame)
        self.console.grid(row=1, column=0, sticky="nsew", pady=(5, 0))
        self.console.tag_config("error_tag", foreground=COLORS["error"])

        # Code editor components
        self._setup_code_editor()

        # Navigation bar buttons
        self._create_nav_buttons()

    def _setup_preview(self):
        """Setup preview area"""
        self.preview_container = ctk.CTkFrame(self.right_frame, fg_color="transparent")
        self.preview_container.grid(row=0, column=0, sticky="nsew", pady=(0, 5))

        self.preview_frame = tk.Frame(self.preview_container, background="black")
        self.preview_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Initial size
        self.preview_frame.configure(width=state.preview_width, height=state.preview_height)

        # Bind resize event
        self.preview_container.bind("<Configure>", self._update_preview_size)

    def _update_preview_size(self, event=None):
        """Update preview area size (keep 16:9 aspect ratio)"""
        self.preview_container.update_idletasks()
        container_w = self.preview_container.winfo_width()
        container_h = self.preview_container.winfo_height()

        if container_w < 100 or container_h < 100:
            return

        aspect = 16 / 9
        if container_w / aspect <= container_h:
            new_w = container_w - 20
            new_h = int(new_w / aspect)
        else:
            new_h = container_h - 20
            new_w = int(new_h * aspect)

        new_w = max(new_w, 320)
        new_h = max(new_h, 180)

        state.preview_width = new_w
        state.preview_height = new_h
        self.preview_frame.configure(width=new_w, height=new_h)
        state.pygame_embed_window_id = self.preview_frame.winfo_id()

    def _setup_code_editor(self):
        """Setup code editor"""
        self.code_area = ctk.CTkFrame(self.code_frame, fg_color="transparent")
        self.code_area.pack(fill="both", expand=True)

        # Line numbers
        self.line_numbers = ctk.CTkTextbox(
            self.code_area, width=50, corner_radius=0,
            text_color=("black", "white"), state="disabled", wrap="none"
        )
        self.line_numbers.pack(side="left", fill="y")

        # Code text box
        self.textbox = ctk.CTkTextbox(
            self.code_area, wrap="none", corner_radius=0,
            text_color=("black", "white"), undo=True
        )
        self.textbox.pack(side="left", fill="both", expand=True)

        # Setup line number synchronization
        setup_line_numbers(self.textbox, self.line_numbers)

        # Auto-completion
        self.autocomplete = AutoCompletePopup(self.master, self.textbox)

        # Tab handling
        self.textbox.bind("<Tab>", self._handle_tab)
        self.textbox.bind("<Shift-Tab>", lambda e: show_suggestions(self.textbox, self.autocomplete))

        # Syntax highlighting
        self.textbox.bind("<KeyRelease>", lambda e: highlight_code(self.textbox))
        highlight_code(self.textbox)

    def _handle_tab(self, event):
        """Handle Tab key"""
        if not state.is_running:
            self.textbox.insert("insert", "    ")
        return "break"

    def _create_nav_buttons(self):
        """Create navigation bar buttons"""
        lang = LANGUAGES[state.current_lang]

        self.btn_file = ctk.CTkButton(
            self.nav_frame, text=lang["File"],
            command=self._show_file_menu,
            width=80, height=25, fg_color="transparent",
            hover_color=COLORS["primary_hover"]
        )
        self.btn_file.pack(side="left", padx=5)

        self.btn_asset = ctk.CTkButton(
            self.nav_frame, text=lang["Asset"],
            command=self._show_asset_menu,
            width=80, height=25, fg_color="transparent",
            hover_color=COLORS["primary_hover"]
        )
        self.btn_asset.pack(side="left", padx=5)

        self.btn_export = ctk.CTkButton(
            self.nav_frame, text=lang["Export"],
            command=self._show_export_menu,
            width=80, height=25, fg_color="transparent",
            hover_color=COLORS["primary_hover"]
        )
        self.btn_export.pack(side="left", padx=5)

        self.btn_run = ctk.CTkButton(
            self.nav_frame, text=lang["Run"],
            command=self._run_code,
            width=80, height=25, fg_color="transparent",
            hover_color=COLORS["primary_hover"]
        )
        self.btn_run.pack(side="left", padx=5)

        self.btn_stop = ctk.CTkButton(
            self.nav_frame, text=lang["Stop"],
            command=self._stop_code,
            width=80, height=25, fg_color="transparent",
            hover_color=COLORS["primary_hover"]
        )
        self.btn_stop.pack(side="left", padx=5)

        self.btn_exit = ctk.CTkButton(
            self.nav_frame, text=lang["Exit"],
            command=self.callbacks.get("on_exit"),
            width=80, height=25, fg_color="transparent",
            hover_color=COLORS["primary_hover"]
        )
        self.btn_exit.pack(side="right", padx=5)

    def _show_file_menu(self):
        """Show file menu"""
        lang = LANGUAGES[state.current_lang]
        menu = Menu(self.master, tearoff=0)

        menu.add_command(
            label=lang["New"],
            command=lambda: new_file(self.textbox, self.master, self._update_editor),
            accelerator="Ctrl+N"
        )
        menu.add_command(
            label=lang["Open"],
            command=lambda: load_file(self.textbox, self.master, self._update_editor),
            accelerator="Ctrl+O"
        )
        menu.add_separator()
        menu.add_command(
            label=lang["Save"],
            command=lambda: save_file(self.textbox, self.master),
            accelerator="Ctrl+S"
        )
        menu.add_command(
            label=lang["SaveAs"],
            command=lambda: save_file_as(self.textbox, self.master),
            accelerator="Ctrl+Shift+S"
        )

        x = self.btn_file.winfo_rootx()
        y = self.btn_file.winfo_rooty() + self.btn_file.winfo_height()
        menu.post(x, y)

    def _show_asset_menu(self):
        """Show asset menu"""
        lang = LANGUAGES[state.current_lang]
        menu = Menu(self.master, tearoff=0)

        menu.add_command(
            label=lang["ImportImage"],
            command=lambda: import_images(self.textbox, self._update_editor)
        )
        menu.add_command(
            label=lang["ImportSound"],
            command=lambda: import_sounds(self.textbox, self._update_editor)
        )
        menu.add_separator()
        menu.add_command(
            label=lang["ImportAll"],
            command=lambda: import_all_assets(self.textbox, self._update_editor)
        )

        x = self.btn_asset.winfo_rootx()
        y = self.btn_asset.winfo_rooty() + self.btn_asset.winfo_height()
        menu.post(x, y)

    def _show_export_menu(self):
        """Show export menu"""
        lang = LANGUAGES[state.current_lang]
        menu = Menu(self.master, tearoff=0)

        menu.add_command(
            label=lang["ExportPy"],
            command=lambda: export_as_python(self.textbox)
        )
        menu.add_command(
            label=lang["ExportExe"],
            command=lambda: export_as_exe(self.textbox)
        )

        x = self.btn_export.winfo_rootx()
        y = self.btn_export.winfo_rooty() + self.btn_export.winfo_height()
        menu.post(x, y)

    def _update_editor(self):
        """Update editor (line numbers and highlighting)"""
        update_line_numbers(self.textbox, self.line_numbers)
        highlight_code(self.textbox)

    def _run_code(self):
        """Run code"""
        self._update_preview_size()
        if self.game_runner is None:
            self.game_runner = GameRunner(self.console, self.textbox, self.preview_frame)
        self.game_runner.run()

    def _stop_code(self):
        """Stop code"""
        if self.game_runner:
            self.game_runner.stop()

    def _setup_key_bindings(self):
        """Setup keyboard shortcuts"""
        # File operation shortcuts
        self.master.bind("<Control-s>", lambda e: save_file(self.textbox, self.master))
        self.master.bind("<Control-S>", lambda e: save_file(self.textbox, self.master))
        self.master.bind("<Control-Shift-s>", lambda e: save_file_as(self.textbox, self.master))
        self.master.bind("<Control-Shift-S>", lambda e: save_file_as(self.textbox, self.master))
        self.master.bind("<Control-o>", lambda e: load_file(self.textbox, self.master, self._update_editor))
        self.master.bind("<Control-O>", lambda e: load_file(self.textbox, self.master, self._update_editor))
        self.master.bind("<Control-n>", lambda e: new_file(self.textbox, self.master, self._update_editor))
        self.master.bind("<Control-N>", lambda e: new_file(self.textbox, self.master, self._update_editor))

        # Game keyboard input
        self.master.bind("<KeyPress>", self._on_key_press)
        self.master.bind("<KeyRelease>", self._on_key_release)
        self.preview_frame.bind("<KeyPress>", self._on_key_press)
        self.preview_frame.bind("<KeyRelease>", self._on_key_release)

        # Special key handling
        for shift_key in ['<Shift_L>', '<Shift_R>', '<KeyPress-Shift_L>', '<KeyPress-Shift_R>']:
            self.master.bind(shift_key, self._on_key_press)
            self.preview_frame.bind(shift_key, self._on_key_press)

        for shift_key in ['<KeyRelease-Shift_L>', '<KeyRelease-Shift_R>']:
            self.master.bind(shift_key, self._on_key_release)
            self.preview_frame.bind(shift_key, self._on_key_release)

    def _on_key_press(self, event):
        """Key press handling"""
        return self._handle_key(event, True)

    def _on_key_release(self, event):
        """Key release handling"""
        return self._handle_key(event, False)

    def _handle_key(self, event, is_press):
        """Unified key handling"""
        key_name = event.keysym

        if state.is_running:
            key_bridge.update(key_name, is_press)
            if key_name in SPECIAL_KEYS:
                return "break"

        return None

    def update_language(self):
        """Update interface language"""
        lang = LANGUAGES[state.current_lang]

        self.btn_file.configure(text=lang["File"])
        self.btn_asset.configure(text=lang["Asset"])
        self.btn_export.configure(text=lang["Export"])
        self.btn_run.configure(text=lang["Run"])
        self.btn_stop.configure(text=lang["Stop"])
        self.btn_exit.configure(text=lang["Exit"])

    def on_show(self):
        """Called when the interface is shown"""
        self.after(100, self._update_preview_size)