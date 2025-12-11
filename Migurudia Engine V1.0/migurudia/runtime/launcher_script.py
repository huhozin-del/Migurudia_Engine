"""Pygame launcher script generator"""

from .key_bridge import key_bridge


def create_pygame_launcher_script(user_code: str, window_id: int, width: int, height: int) -> str:
    """
    generate a pygame launcher script for embedding in Tkinter window.
    
    Args:
        user_code: code written by user
        window_id: Tkinter window ID, used to embed Pygame window
        width: preview window width
        height: preview window height
    
    Returns:
        Generated launcher script as a string
    """
    mapping_dict_str = key_bridge.get_key_map_string()

    script_content = f"""
import pygame
import sys
import os
import json
import traceback

TK_TO_PYGAME_KEY_MAP = {mapping_dict_str}

os.environ['SDL_WINDOWID'] = str({window_id})
if sys.platform == "win32":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

try:
    import ctypes
    if sys.platform == "win32":
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except:
            pass
    
    pygame.init()
    
    _temp_keys = pygame.key.get_pressed()
    KEY_ARRAY_SIZE = len(_temp_keys)
    print(f"[Migu] Detected KEY_ARRAY_SIZE: {{KEY_ARRAY_SIZE}}", file=sys.stderr)
    
    screen = pygame.display.set_mode(({width}, {height}), pygame.SCALED)
    pygame.display.set_caption("Migurudia Preview")

    def get_tk_key_state():
        key_file = os.environ.get('MIGU_KEY_FILE')
        pressed_tk_keys = set()
        
        if key_file:
            try:
                with open(key_file, 'r') as f:
                    pressed_tk_keys = set(json.load(f))
            except:
                pass
        
        key_state_dict = {{}}
        for tk_key_name in pressed_tk_keys:
            if isinstance(tk_key_name, str):
                pygame_key_code = TK_TO_PYGAME_KEY_MAP.get(tk_key_name)
                if pygame_key_code is not None:
                    key_state_dict[pygame_key_code] = True
        
        class KeyStateProxy:
            def __init__(self, state_dict, array_size):
                self._dict = state_dict
                self._size = array_size
            
            def __getitem__(self, key):
                return self._dict.get(key, False)
            
            def __len__(self):
                return self._size
        
        return KeyStateProxy(key_state_dict, KEY_ARRAY_SIZE)

    pygame.key.get_pressed = get_tk_key_state
    
    exec_scope = {{'pygame': pygame, 'screen': screen}}
    
    try:
        exec({repr(user_code)}, exec_scope)
    except Exception:
        print(traceback.format_exc(), file=sys.stderr)
        pygame.quit()
        sys.exit(1)

    if 'game_loop' in exec_scope:
        game_loop = exec_scope['game_loop']
        running = True
        clock = pygame.time.Clock()
        
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
            
            try:
                game_loop(screen, events)
            except Exception:
                print(f"Error in game_loop: {{traceback.format_exc()}}", file=sys.stderr)
                running = False
            
            pygame.display.flip()
            clock.tick(60)
            
        pygame.quit()
    else:
        print("Error: 'game_loop(screen, events)' not found.", file=sys.stderr)
        pygame.quit()

except Exception:
    print(f"System Error: {{traceback.format_exc()}}", file=sys.stderr)
finally:
    if pygame.get_init():
        pygame.quit()
"""
    return script_content


def get_standalone_code(user_code: str) -> str:
    """
    generate a standalone pygame script.
    
    Args:
        user_code: code written by user
    
    Returns:
        Generated standalone script as a string
    """
    header = '''import pygame
import random
import math
import sys
import os

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((854, 480))
pygame.display.set_caption("Migurudia Game")

# Set window icon
try:
    if getattr(sys, 'frozen', False):
        # Running as EXE
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)
    
    icon_path = os.path.join(base_path, "migurudia.png")
    if os.path.exists(icon_path):
        icon = pygame.image.load(icon_path)
        pygame.display.set_icon(icon)
except:
    pass

'''

    footer = '''

# Main loop
if __name__ == "__main__":
    if 'game_loop' in dir():
        clock = pygame.time.Clock()
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
            
            game_loop(screen, events)
            pygame.display.flip()
            clock.tick(60)
        
        pygame.quit()
        sys.exit()
    else:
        print("Error: game_loop(screen, events) not found!")
        pygame.quit()
        sys.exit(1)
'''
    return header + user_code + footer
