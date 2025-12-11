"""line numbers module"""


def update_line_numbers(textbox, line_numbers_widget, event=None):
    """
    update line numbers display
    
    Args:
        textbox: code editor CTkTextbox
        line_numbers_widget: show line number CTkTextbox
        event: (optional) event that triggered the update
    """
    total_lines = int(textbox.index('end-1c').split('.')[0])
    numbers = "\n".join(str(i) for i in range(1, total_lines + 1))

    line_numbers_widget.configure(state="normal")
    line_numbers_widget.delete("1.0", "end")
    line_numbers_widget.insert("1.0", numbers)
    line_numbers_widget.configure(state="disabled")


def setup_line_numbers(textbox, line_numbers_widget):
    """
    setup line numbers synchronization
    
    Args:
        textbox: code editor CTkTextbox
        line_numbers_widget: show line number CTkTextbox
    """
    def on_scroll(*args):
        """sync scrolling of line numbers with textbox"""
        line_numbers_widget.yview_moveto(textbox.yview()[0])
        update_line_numbers(textbox, line_numbers_widget)

    textbox.configure(yscrollcommand=on_scroll)
    textbox.bind("<KeyRelease>", lambda e: update_line_numbers(textbox, line_numbers_widget, e))
    textbox.bind("<MouseWheel>", lambda e: update_line_numbers(textbox, line_numbers_widget, e))

    # initial update
    update_line_numbers(textbox, line_numbers_widget)
