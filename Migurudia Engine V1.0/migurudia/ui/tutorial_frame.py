"""Tutorial Interface with Rich Text Support"""

import re
import customtkinter as ctk

from config import state, COLORS, LANGUAGES
from data import get_tutorial_titles, get_tutorial_content


class TutorialFrame(ctk.CTkFrame):
    """Tutorial Interface Frame with Rich Text Support｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡(Finally, to be fair I was to lazy to add this thing but I did it now)"""

    def __init__(self, master, callbacks: dict):
        """
        Initialize tutorial interface
        
        Args:
            master: Parent window
            callbacks: Dictionary of callback functions, including:
                - on_exit: Exit tutorial and return to home page
        """
        super().__init__(master)
        self.callbacks = callbacks
        self.tutorial_buttons = []
        self.current_tutorial = None

        self._setup_ui()
        self._setup_text_tags()

    def _setup_ui(self):
        """Setup UI layout"""
        # Navigation bar
        self.nav_frame = ctk.CTkFrame(
            self, height=40, fg_color=COLORS["primary"], corner_radius=0
        )
        self.nav_frame.pack(side="top", fill="x")
        self.nav_frame.pack_propagate(False)

        # Exit button
        self.btn_exit = ctk.CTkButton(
            self.nav_frame,
            text=LANGUAGES[state.current_lang]["Exit"],
            command=self.callbacks.get("on_exit"),
            width=80, height=25, fg_color="transparent",
            hover_color=COLORS["primary_hover"]
        )
        self.btn_exit.pack(side="right", padx=10)

        # Title
        self.title_label = ctk.CTkLabel(
            self.nav_frame,
            text="Tutorials",
            font=("Arial", 16, "bold"),
            text_color="white"
        )
        self.title_label.pack(side="left", padx=15)

        # Main content area
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # Left sidebar
        self.sidebar = ctk.CTkFrame(self.content_frame, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y", padx=(0, 5))
        self.sidebar.pack_propagate(False)

        # Right content display area
        self.display_frame = ctk.CTkFrame(self.content_frame)
        self.display_frame.pack(side="left", fill="both", expand=True)

        # Content text widget - using larger base font
        self.text_widget = ctk.CTkTextbox(
            self.display_frame, 
            wrap="word", 
            font=("Consolas", 13),  # Monospace for better alignment
            spacing2=2,  # Line spacing
            spacing3=4,  # Paragraph spacing
        )
        self.text_widget.pack(fill="both", expand=True, padx=10, pady=10)

    def _get_text_widget(self):
        """Get the underlying Tk Text widget"""
        # CTkTextbox has an internal textbox attribute
        for attr in ("_textbox", "textbox", "_text"):
            if hasattr(self.text_widget, attr):
                return getattr(self.text_widget, attr)
        return self.text_widget

    def _setup_text_tags(self):
        """Setup text styling tags"""
        text = self._get_text_widget()
        
        # Main title - big, bold, colored
        text.tag_config(
            "h1",
            font=("Arial", 24, "bold"),
            foreground="#648CFF",
            spacing1=10,
            spacing3=10
        )
        
        # Section header - medium, bold
        text.tag_config(
            "h2",
            font=("Arial", 18, "bold"),
            foreground="#4A90D9",
            spacing1=15,
            spacing3=5
        )
        
        # Subsection - smaller bold
        text.tag_config(
            "h3",
            font=("Arial", 15, "bold"),
            foreground="#5BA0D0",
            spacing1=10,
            spacing3=3
        )
        
        # Bold text
        text.tag_config(
            "bold",
            font=("Arial", 13, "bold")
        )
        
        # Code/monospace - with background
        text.tag_config(
            "code",
            font=("Consolas", 12),
            foreground="#E06C75",
            background="#2D2D2D"
        )
        
        # Code block
        text.tag_config(
            "codeblock",
            font=("Consolas", 12),
            foreground="#ABB2BF",
            background="#282C34",
            spacing1=5,
            spacing3=5,
            lmargin1=20,
            lmargin2=20
        )
        
        # Highlight/important
        text.tag_config(
            "highlight",
            foreground="#FFD700",
            font=("Arial", 13, "bold")
        )
        
        # Success/green
        text.tag_config(
            "success",
            foreground="#98C379",
            font=("Arial", 13, "bold")
        )
        
        # Error/warning red
        text.tag_config(
            "error",
            foreground="#E06C75",
            font=("Arial", 13, "bold")
        )
        
        # Tip/info blue
        text.tag_config(
            "tip",
            foreground="#61AFEF",
            font=("Arial", 13)
        )
        
        # Divider line
        text.tag_config(
            "divider",
            foreground="#555555",
            font=("Arial", 10)
        )
        
        # Emoji - slightly larger
        text.tag_config(
            "emoji",
            font=("Segoe UI Emoji", 14)
        )

    def _render_rich_text(self, content: str):
        """
        Parse and render rich text with styling
        
        Supported syntax:
            # Title          → h1 (big blue title)
            ## Section       → h2 (medium bold)
            ### Subsection   → h3 (small bold)
            **bold**         → bold text
            `code`           → inline code
            ```code block``` → code block
            !!warning!!      → red warning
            ??tip??          → blue tip
            $$highlight$$    → yellow highlight
            ++success++      → green success
            ---              → divider line
        """
        text = self._get_text_widget()
        
        lines = content.split('\n')
        in_code_block = False
        code_block_content = []
        
        for line in lines:
            # Code block handling
            if line.strip().startswith('```'):
                if in_code_block:
                    # End of code block
                    code_text = '\n'.join(code_block_content) + '\n'
                    text.insert("end", code_text, "codeblock")
                    code_block_content = []
                    in_code_block = False
                else:
                    # Start of code block
                    in_code_block = True
                continue
            
            if in_code_block:
                code_block_content.append(line)
                continue
            
            # Divider line
            if line.strip().startswith('━') or line.strip() == '---':
                text.insert("end", line + '\n', "divider")
                continue
            
            # H1 Title: # Title
            if line.startswith('# ') and not line.startswith('##'):
                text.insert("end", line[2:] + '\n', "h1")
                continue
            
            # H2 Section: ## Section
            if line.startswith('## '):
                text.insert("end", line[3:] + '\n', "h2")
                continue
            
            # H3 Subsection: ### Subsection
            if line.startswith('### '):
                text.insert("end", line[4:] + '\n', "h3")
                continue
            
            # Process inline formatting
            self._insert_formatted_line(text, line + '\n')
        
        # Handle unclosed code block
        if code_block_content:
            code_text = '\n'.join(code_block_content) + '\n'
            text.insert("end", code_text, "codeblock")

    def _insert_formatted_line(self, text, line: str):
        """Insert a line with inline formatting"""
        # Pattern for inline styles
        patterns = [
            (r'\*\*(.+?)\*\*', 'bold'),      # **bold**
            (r'`([^`]+)`', 'code'),           # `code`
            (r'!!(.+?)!!', 'error'),          # !!warning!!
            (r'\?\?(.+?)\?\?', 'tip'),        # ??tip??
            (r'\$\$(.+?)\$\$', 'highlight'),  # $$highlight$$
            (r'\+\+(.+?)\+\+', 'success'),    # ++success++
        ]
        
        # Find all matches and their positions
        segments = []
        last_end = 0
        
        # Combine all patterns
        combined_pattern = '|'.join(f'({p[0]})' for p in patterns)
        
        for match in re.finditer(combined_pattern, line):
            start, end = match.span()
            
            # Add plain text before this match
            if start > last_end:
                segments.append((line[last_end:start], None))
            
            # Find which pattern matched
            matched_text = match.group()
            for pattern, tag in patterns:
                m = re.match(pattern, matched_text)
                if m:
                    # Extract the content (group 1)
                    content = m.group(1)
                    segments.append((content, tag))
                    break
            
            last_end = end
        
        # Add remaining text
        if last_end < len(line):
            segments.append((line[last_end:], None))
        
        # Insert all segments
        for content, tag in segments:
            if tag:
                text.insert("end", content, tag)
            else:
                text.insert("end", content)

    def _create_tutorial_buttons(self):
        """Create tutorial navigation buttons"""
        # Clear existing buttons
        for btn, _ in self.tutorial_buttons:
            btn.destroy()
        self.tutorial_buttons = []

        # Get tutorial list for current language
        titles = get_tutorial_titles(state.current_lang)

        for title in titles:
            btn = ctk.CTkButton(
                self.sidebar,
                text=title,
                fg_color="transparent",
                hover_color=COLORS["primary"],
                text_color=("black", "white"),
                anchor="w",
                command=lambda t=title: self._show_tutorial(t)
            )
            btn.pack(fill="x", pady=2, padx=5)
            self.tutorial_buttons.append((btn, title))

        # Show the first tutorial
        if titles:
            self._show_tutorial(titles[0])

    def _show_tutorial(self, title: str):
        """Show specific tutorial content with rich text rendering"""
        self.current_tutorial = title

        content = get_tutorial_content(state.current_lang, title)

        self.text_widget.configure(state="normal")
        self.text_widget.delete("1.0", "end")
        
        # Use rich text rendering
        self._render_rich_text(content)
        
        self.text_widget.configure(state="disabled")

        # Update button styles
        for btn, btn_title in self.tutorial_buttons:
            if btn_title == title:
                btn.configure(fg_color=COLORS["primary"])
            else:
                btn.configure(fg_color="transparent")

    def update_language(self):
        """Update interface language"""
        self.btn_exit.configure(text=LANGUAGES[state.current_lang]["Exit"])
        self._create_tutorial_buttons()

    def on_show(self):
        """Called when the interface is shown"""
        self._create_tutorial_buttons()