"""file operations: save, load, new file"""

import os
from tkinter import filedialog

from config.settings import state
from config.languages import LANGUAGES


def save_file(textbox, app_window):
    """
    save current file
    
    Args:
        textbox: code editor widget
        app_window: main application window
    """
    code = textbox.get("1.0", "end-1c")

    if state.current_file_path:
        try:
            with open(state.current_file_path, 'w', encoding='utf-8') as f:
                f.write(code)
            print(f"[Saved] {state.current_file_path}")
        except Exception as e:
            print(f"[Error] Save failed: {e}")
    else:
        save_file_as(textbox, app_window)


def save_file_as(textbox, app_window):
    """
    save as new file
    
    Args:
        textbox: code editor widget
        app_window: main application window
    """
    file_path = filedialog.asksaveasfilename(
        defaultextension=".py",
        filetypes=[
            ("Python Files", "*.py"),
            ("Migurudia Project", "*.migu"),
            ("All Files", "*.*")
        ],
        title="Save As"
    )

    if not file_path:
        return

    code = textbox.get("1.0", "end-1c")
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)
        state.current_file_path = file_path
        app_window.title(f"Migurudia V0.1 - {os.path.basename(file_path)}")
        print(f"[Saved] {file_path}")
    except Exception as e:
        print(f"[Error] Save failed: {e}")


def load_file(textbox, app_window, update_callback=None):
    """
    load file into editor
    
    Args:
        textbox: code editor widget
        app_window: main application window
        update_callback: load callback that is updated
    
    Returns:
        bool: True if load successful, False otherwise
    """
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Python Files", "*.py"),
            ("Migurudia Project", "*.migu"),
            ("All Files", "*.*")
        ],
        title="Open File"
    )

    if not file_path:
        return False

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()

        textbox.delete("1.0", "end")
        textbox.insert("1.0", code)
        state.current_file_path = file_path
        app_window.title(f"Migurudia V0.1 - {os.path.basename(file_path)}")

        if update_callback:
            update_callback()

        print(f"[Loaded] {file_path}")
        return True

    except Exception as e:
        print(f"[Error] Load failed: {e}")
        return False


def new_file(textbox, app_window, update_callback=None):
    """
    create a new file in editor
    
    Args:
        textbox: code editor widget
        app_window: main application window
        update_callback: update callback
    """
    textbox.delete("1.0", "end")
    state.current_file_path = None
    app_window.title("Migurudia V0.1")

    if update_callback:
        update_callback()

    print("[New File]")
