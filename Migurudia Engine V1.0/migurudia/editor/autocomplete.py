"""suto-completion functions"""

import customtkinter as ctk

try:
    import jedi
    JEDI_AVAILABLE = True
except ImportError:
    JEDI_AVAILABLE = False
    print("[Warning] jedi not installed, autocomplete disabled")


class AutoCompletePopup:
    """auto-completion popup"""

    def __init__(self, master, textbox):
        """
        initialize auto-completion popup
        
        Args:
            master: parent widget
            textbox: code editor CTkTextbox
        """
        self.textbox = textbox
        self.popup = ctk.CTkToplevel(master)
        self.popup.withdraw()
        self.popup.overrideredirect(True)

        self.frame = ctk.CTkScrollableFrame(self.popup, width=120, height=120)
        self.frame.pack(fill="both", expand=True)

        self.labels = []
        self.visible = False
        self.selected_index = 0

        # bindings QAQ
        textbox.bind("<Down>", self.on_down)
        textbox.bind("<Up>", self.on_up)
        textbox.bind("<Return>", self.on_enter)
        textbox.bind("<Escape>", lambda e: self.hide())
        textbox.bind("<Key>", self.on_text_change)

    def show(self, x: int, y: int, items: list):
        """
        show completion list
        
        Args:
            x: screen X coordinate
            y: screen Y coordinate
            items: list of completion items
        """
        # clear previous labels
        for lbl in self.labels:
            lbl.destroy()
        self.labels = []

        # create new labels
        for item in items:
            lbl = ctk.CTkLabel(
                self.frame,
                text=item,
                fg_color="transparent",
                text_color=("black", "white")
            )
            lbl.pack(fill="x", pady=1)
            lbl.bind("<Button-1>", lambda e, it=item: self.on_label_click(it))
            self.labels.append(lbl)

        self.selected_index = 0
        self.highlight_selected()
        self.popup.geometry(f"+{x}+{y}")
        self.popup.deiconify()
        self.visible = True

    def hide(self):
        """hide completion list"""
        self.popup.withdraw()
        self.visible = False

    def on_down(self, event):
        """choose next item"""
        if not self.visible:
            return
        if self.selected_index < len(self.labels) - 1:
            self.selected_index += 1
            self.highlight_selected()
        return "break"

    def on_up(self, event):
        """choose previous item"""
        if not self.visible:
            return
        if self.selected_index > 0:
            self.selected_index -= 1
            self.highlight_selected()
        return "break"

    def on_enter(self, event):
        """insert selected item"""
        if not self.visible:
            return
        word = self.labels[self.selected_index].cget("text")
        self.insert_completion(word)
        self.hide()
        return "break"

    def highlight_selected(self):
        """highlight selected item"""
        for i, lbl in enumerate(self.labels):
            lbl.configure(
                fg_color="#648CFF" if i == self.selected_index else "transparent"
            )

        # ensure selected item is visible
        try:
            lbl = self.labels[self.selected_index]
            self.frame.update_idletasks()
            canvas = self.frame._parent_canvas
            label_y = lbl.winfo_y()
            if label_y < canvas.canvasy(0) or label_y > canvas.canvasy(0) + canvas.winfo_height():
                canvas.yview_moveto(label_y / self.frame.winfo_height())
        except:
            pass

    def insert_completion(self, word: str):
        """insert selected completion into textbox"""
        index = self.textbox.index("insert")
        row, col = map(int, index.split("."))
        line = self.textbox.get(f"{row}.0", f"{row}.end")

        # find start of current word
        start_col = col
        while start_col > 0 and (line[start_col - 1].isalnum() or line[start_col - 1] == "_"):
            start_col -= 1

        # replace current word with completion
        self.textbox.delete(f"{row}.{start_col}", f"{row}.{col}")
        self.textbox.insert("insert", word)

    def on_label_click(self, item: str):
        """insert clicked item"""
        self.insert_completion(item)
        self.hide()
        self.textbox.focus_set()

    def on_text_change(self, event):
        """hide popup on text change"""
        if self.visible and event.keysym not in ("Up", "Down", "Return"):
            self.hide()


def show_suggestions(textbox, autocomplete: AutoCompletePopup, event=None):
    """
    show auto-completion suggestions
    
    Args:
        textbox: code editor (CTkTextbox)
        autocomplete: AutoCompletePopup instance
    """
    if not JEDI_AVAILABLE:
        return "break"

    code = textbox.get("1.0", "end-1c")
    index = textbox.index("insert")
    row, col = map(int, index.split("."))

    try:
        script = jedi.Script(code)
        completions = script.complete(row, col)
        items = [c.name for c in completions]

        if not items:
            autocomplete.hide()
            return "break"

        # get cursor position
        bbox = textbox.bbox("insert")
        if bbox:
            x = textbox.winfo_rootx() + bbox[0]
            y = textbox.winfo_rooty() + bbox[1] + bbox[3]
        else:
            x, y = 100, 100

        autocomplete.show(x, y, items)

    except Exception as e:
        print(f"Jedi error: {e}")

    return "break"
