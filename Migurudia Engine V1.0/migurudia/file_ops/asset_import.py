"""Asset Import Module"""

import os
import re
from tkinter import filedialog


def import_images(textbox, update_callback=None):
    """
    import image files
    
    Args:
        textbox: code editor
        update_callback: update callback
    """
    file_paths = filedialog.askopenfilenames(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp")],
        title="Import Images"
    )
    _insert_asset_code(textbox, file_paths, update_callback)


def import_sounds(textbox, update_callback=None):
    """
    import sound files
    
    Args:
        textbox: code editor
        update_callback: update callback
    """
    file_paths = filedialog.askopenfilenames(
        filetypes=[("Audio Files", "*.wav *.mp3 *.ogg")],
        title="Import Sounds"
    )
    _insert_asset_code(textbox, file_paths, update_callback)


def import_all_assets(textbox, update_callback=None):
    """
    import all asset files
    
    Args:
        textbox: code editor
        update_callback: update callback
    """
    file_paths = filedialog.askopenfilenames(
        filetypes=[
            ("All Assets", "*.png *.jpg *.jpeg *.gif *.bmp *.wav *.mp3 *.ogg"),
            ("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp"),
            ("Audio Files", "*.wav *.mp3 *.ogg"),
            ("All Files", "*.*")
        ],
        title="Import Assets"
    )
    _insert_asset_code(textbox, file_paths, update_callback)


def _insert_asset_code(textbox, file_paths, update_callback=None):
    """
    Insert asset loading code into the textbox.
    
    Args:
        textbox: code editor
        file_paths: list of file paths
        update_callback: update callback
    """
    if not file_paths:
        return

    code_lines = []

    for path in file_paths:
        filename = os.path.basename(path)
        # Sanitize variable name
        name = os.path.splitext(filename)[0]
        name = re.sub(r'[^a-zA-Z0-9_]', '_', name)
        ext = os.path.splitext(filename)[1].lower()

        if ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp']:
            code_lines.append(f'{name}_img = pygame.image.load(r"{path}")')
        elif ext in ['.wav', '.mp3', '.ogg']:
            code_lines.append(f'{name}_snd = pygame.mixer.Sound(r"{path}")')

    if code_lines:
        insert_code = "\n".join(code_lines) + "\n"
        textbox.insert("insert", insert_code)

        if update_callback:
            update_callback()

        print(f"[Asset] Imported {len(file_paths)} file(s)")
