
"""configuration module"""

from .settings import state, COLORS, DEFAULT_PREVIEW_WIDTH, DEFAULT_PREVIEW_HEIGHT
from .languages import LANGUAGES, get_text

__all__ = [
    'state', 
    'COLORS', 
    'DEFAULT_PREVIEW_WIDTH', 
    'DEFAULT_PREVIEW_HEIGHT',
    'LANGUAGES', 
    'get_text'
]
