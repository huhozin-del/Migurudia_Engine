"""connect key state Tkinter between Pygame"""

import json
import os
import tempfile
import pygame


# key mapping (☉д⊙)(I spend like a week to figure this thing out finally works I hate tkinter and pygame keycode system)
KEY_MAP = {
    # lowercase letters
    'a': pygame.K_a, 'b': pygame.K_b, 'c': pygame.K_c, 'd': pygame.K_d,
    'e': pygame.K_e, 'f': pygame.K_f, 'g': pygame.K_g, 'h': pygame.K_h,
    'i': pygame.K_i, 'j': pygame.K_j, 'k': pygame.K_k, 'l': pygame.K_l,
    'm': pygame.K_m, 'n': pygame.K_n, 'o': pygame.K_o, 'p': pygame.K_p,
    'q': pygame.K_q, 'r': pygame.K_r, 's': pygame.K_s, 't': pygame.K_t,
    'u': pygame.K_u, 'v': pygame.K_v, 'w': pygame.K_w, 'x': pygame.K_x,
    'y': pygame.K_y, 'z': pygame.K_z,

    # uppercase letters
    'A': pygame.K_a, 'B': pygame.K_b, 'C': pygame.K_c, 'D': pygame.K_d,
    'E': pygame.K_e, 'F': pygame.K_f, 'G': pygame.K_g, 'H': pygame.K_h,
    'I': pygame.K_i, 'J': pygame.K_j, 'K': pygame.K_k, 'L': pygame.K_l,
    'M': pygame.K_m, 'N': pygame.K_n, 'O': pygame.K_o, 'P': pygame.K_p,
    'Q': pygame.K_q, 'R': pygame.K_r, 'S': pygame.K_s, 'T': pygame.K_t,
    'U': pygame.K_u, 'V': pygame.K_v, 'W': pygame.K_w, 'X': pygame.K_x,
    'Y': pygame.K_y, 'Z': pygame.K_z,

    # number keys
    '0': pygame.K_0, '1': pygame.K_1, '2': pygame.K_2, '3': pygame.K_3,
    '4': pygame.K_4, '5': pygame.K_5, '6': pygame.K_6, '7': pygame.K_7,
    '8': pygame.K_8, '9': pygame.K_9,

    # function keys
    'F1': pygame.K_F1, 'F2': pygame.K_F2, 'F3': pygame.K_F3, 'F4': pygame.K_F4,
    'F5': pygame.K_F5, 'F6': pygame.K_F6, 'F7': pygame.K_F7, 'F8': pygame.K_F8,
    'F9': pygame.K_F9, 'F10': pygame.K_F10, 'F11': pygame.K_F11, 'F12': pygame.K_F12,

    # modifier keys
    'Shift_L': pygame.K_LSHIFT,
    'Shift_R': pygame.K_RSHIFT,
    'Control_L': pygame.K_LCTRL,
    'Control_R': pygame.K_RCTRL,
    'Alt_L': pygame.K_LALT,
    'Alt_R': pygame.K_RALT,
    'Win_L': pygame.K_LMETA,
    'Win_R': pygame.K_RMETA,
    'Caps_Lock': pygame.K_CAPSLOCK,

    # control keys
    'space': pygame.K_SPACE,
    'Return': pygame.K_RETURN,
    'Escape': pygame.K_ESCAPE,
    'Tab': pygame.K_TAB,
    'BackSpace': pygame.K_BACKSPACE,
    'Delete': pygame.K_DELETE,
    'Insert': pygame.K_INSERT,
    'Print': pygame.K_PRINT,

    # navigation keys
    'Home': pygame.K_HOME,
    'End': pygame.K_END,
    'Prior': pygame.K_PAGEUP,
    'Next': pygame.K_PAGEDOWN,

    # arrow keys
    'Up': pygame.K_UP,
    'Down': pygame.K_DOWN,
    'Left': pygame.K_LEFT,
    'Right': pygame.K_RIGHT,

    # punctuation and symbols
    'minus': pygame.K_MINUS,
    'equal': pygame.K_EQUALS,
    'bracketleft': pygame.K_LEFTBRACKET,
    'bracketright': pygame.K_RIGHTBRACKET,
    'backslash': pygame.K_BACKSLASH,
    'semicolon': pygame.K_SEMICOLON,
    'apostrophe': pygame.K_QUOTE,
    'comma': pygame.K_COMMA,
    'period': pygame.K_PERIOD,
    'slash': pygame.K_SLASH,
    'grave': pygame.K_BACKQUOTE,

    # numpad keys
    'KP_0': pygame.K_KP0, 'KP_1': pygame.K_KP1, 'KP_2': pygame.K_KP2,
    'KP_3': pygame.K_KP3, 'KP_4': pygame.K_KP4, 'KP_5': pygame.K_KP5,
    'KP_6': pygame.K_KP6, 'KP_7': pygame.K_KP7, 'KP_8': pygame.K_KP8,
    'KP_9': pygame.K_KP9,
    'KP_Decimal': pygame.K_KP_PERIOD,
    'KP_Divide': pygame.K_KP_DIVIDE,
    'KP_Multiply': pygame.K_KP_MULTIPLY,
    'KP_Subtract': pygame.K_KP_MINUS,
    'KP_Add': pygame.K_KP_PLUS,
    'KP_Enter': pygame.K_KP_ENTER,
    'Num_Lock': pygame.K_NUMLOCK,
}

# keys that need special handling(〒︿〒)(you wont understand my pain figuring this thing out)
SPECIAL_KEYS = {
    'Tab', 'Shift_L', 'Shift_R', 'Control_L', 'Control_R',
    'Alt_L', 'Alt_R', 'Return', 'Escape'
}


class KeyBridge:
    """Keyboard State Bridge for synchronizing keyboard status between Tkinter and Pygame subprocesses"""

    def __init__(self):
        self.pressed_keys = set()
        self.state_path = os.path.join(
            tempfile.gettempdir(),
            f"migu_keys_{os.getpid()}.json"
        )

    def update(self, key_name: str, is_pressed: bool):
        """update key state"""
        if key_name not in KEY_MAP:
            return

        if is_pressed:
            self.pressed_keys.add(key_name)
        else:
            self.pressed_keys.discard(key_name)

        self._save_state()

    def _save_state(self):
        """save current key state to temporary file"""
        try:
            with open(self.state_path, 'w') as f:
                json.dump(list(self.pressed_keys), f)
        except Exception:
            pass

    def reset(self):
        """reset key state"""
        self.pressed_keys.clear()
        self._save_state()

    def initialize(self):
        """initialize key bridge"""
        self.reset()
        os.environ['MIGU_KEY_FILE'] = self.state_path

    def cleanup(self):
        """cleanup temporary key state file"""
        try:
            os.unlink(self.state_path)
        except Exception:
            pass

    def get_key_map_string(self) -> str:
        """get key map as string for Pygame subprocess"""
        parts = [f"'{k}': {v}" for k, v in KEY_MAP.items()]
        return "{" + ", ".join(parts) + "}"


# Instantiate a global KeyBridge
key_bridge = KeyBridge()
