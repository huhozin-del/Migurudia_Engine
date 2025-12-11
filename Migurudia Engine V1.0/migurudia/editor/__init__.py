"""code editor module"""

from .syntax_highlight import highlight_code, HIGHLIGHT_COLORS
from .autocomplete import AutoCompletePopup, show_suggestions
from .line_numbers import update_line_numbers, setup_line_numbers

__all__ = [
    'highlight_code',
    'HIGHLIGHT_COLORS',
    'AutoCompletePopup',
    'show_suggestions',
    'update_line_numbers',
    'setup_line_numbers',
]
