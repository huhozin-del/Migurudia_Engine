"""home Frame Interface"""

import customtkinter as ctk
from PIL import Image

from config import state, COLORS, LANGUAGES


class HomeFrame(ctk.CTkFrame):
    """Home Frame Class"""

    def __init__(self, master, callbacks: dict):
        """
        initialize Home Frame
        
        Args:
            master: parent widget
            callbacks: callback functions dictionary:
                - on_create: create new project
                - on_load: load existing project
                - on_import: import asset
                - on_tutorial: open tutorials
        """
        super().__init__(master)
        self.callbacks = callbacks

        self._setup_ui()

    def _setup_ui(self):
        """setup user interface"""
        # title frame
        self.title_frame = ctk.CTkFrame(
            self, height=60, fg_color=COLORS["primary"], corner_radius=0
        )
        self.title_frame.pack(side="top", fill="x")
        self.title_frame.pack_propagate(False)

        # Logo and Title
        try:
            self.logo_image = ctk.CTkImage(
                light_image=Image.open("assets/migurudia.png"),
                size=(50, 50)
            )
        except FileNotFoundError:
            self.logo_image = None

        self.title_label = ctk.CTkLabel(
            self.title_frame,
            text=LANGUAGES[state.current_lang]["title"],
            font=("Arial", 22, "bold"),
            image=self.logo_image,
            compound="right",
            text_color="white"
        )
        self.title_label.place(relx=0.02, rely=0.02, anchor="nw")

        # main content frame
        self.main_content = ctk.CTkFrame(self)
        self.main_content.pack(fill="both", expand=True)

        # navigation frame
        self.nav_frame = ctk.CTkFrame(self.main_content, corner_radius=0)
        self.nav_frame.pack(side="left", fill="y", ipadx=50)

        # settings frame
        self.settings_frame = ctk.CTkFrame(self.main_content)
        self.settings_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        # create navigation buttons and settings
        self._create_nav_buttons()
        self._create_settings()

    def _create_nav_buttons(self):
        """Create navigation buttons"""
        lang = LANGUAGES[state.current_lang]

        self.btn_create = ctk.CTkButton(
            self.nav_frame,
            text=lang["create"],
            fg_color="transparent",
            hover_color=COLORS["primary"],
            command=self.callbacks.get("on_create"),
            text_color=("black", "white")
        )
        self.btn_create.pack(pady=10, padx=20)

        self.btn_load = ctk.CTkButton(
            self.nav_frame,
            text=lang["load"],
            fg_color="transparent",
            hover_color=COLORS["primary"],
            command=self.callbacks.get("on_load"),
            text_color=("black", "white")
        )
        self.btn_load.pack(pady=10, padx=20)

        self.btn_import = ctk.CTkButton(
            self.nav_frame,
            text=lang["import"],
            fg_color="transparent",
            hover_color=COLORS["primary"],
            command=self.callbacks.get("on_import"),
            text_color=("black", "white")
        )
        self.btn_import.pack(pady=10, padx=20)

        self.btn_tutorial = ctk.CTkButton(
            self.nav_frame,
            text=lang["tutorials"],
            fg_color="transparent",
            hover_color=COLORS["primary"],
            command=self.callbacks.get("on_tutorial"),
            text_color=("black", "white")
        )
        self.btn_tutorial.pack(pady=10, padx=20)

    def _create_settings(self):
        """Create settings area"""
        lang = LANGUAGES[state.current_lang]

        # Theme switch
        self.theme_switch = ctk.CTkSwitch(
            self.settings_frame,
            text=lang["theme"],
            command=self._switch_theme,
            fg_color=COLORS["primary_hover"],
            button_color="white",
            progress_color=COLORS["primary_hover"]
        )
        self.theme_switch.pack(pady=10, padx=20)

        # Language selection
        self.lang_var = ctk.StringVar(value=lang["language"])
        self.lang_combobox = ctk.CTkComboBox(
            self.settings_frame,
            values=['English', '中文'],
            width=140,
            height=28,
            command=self._change_language,
            variable=self.lang_var
        )
        self.lang_combobox.place(x=10, y=10)

    def _switch_theme(self):
        """Switch theme"""
        if self.theme_switch.get() == 1:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    def _change_language(self, choice):
        """Switch language"""
        if choice == "English":
            state.current_lang = "en"
        elif choice == "中文":
            state.current_lang = "zh"

        # Notify main application to update language
        if "on_language_change" in self.callbacks:
            self.callbacks["on_language_change"]()

    def update_language(self):
        """Update interface language"""
        lang = LANGUAGES[state.current_lang]

        self.title_label.configure(text=lang["title"])
        self.theme_switch.configure(text=lang["theme"])
        self.lang_var.set(lang["language"])
        self.btn_create.configure(text=lang["create"])
        self.btn_load.configure(text=lang["load"])
        self.btn_import.configure(text=lang["import"])
        self.btn_tutorial.configure(text=lang["tutorials"])