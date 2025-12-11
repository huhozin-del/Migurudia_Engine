"""syntax_highlight module"""

import re
import keyword
import builtins

# get all built-in function names
BUILTIN_FUNCS = [f for f in dir(builtins) if callable(getattr(builtins, f))]

# syntax highlight patterns
PATTERNS = [
    (r"\"\"\".*?\"\"\"|\".*?\"|'.*?'", "string"),
    (r"#[^\n]*", "comment"),
    (r"\b(" + "|".join(keyword.kwlist) + r")\b", "keyword"),
    (r"\b(" + "|".join(BUILTIN_FUNCS) + r")\b", "builtin"),
    (r"\b\d+(\.\d+)?\b", "number"),
    (r"\bdef\s+([A-Za-z_]\w*)", "function"),
    (r"\bclass\s+([A-Za-z_]\w*)", "class"),
]

# syntax highlight colors
HIGHLIGHT_COLORS = {
    "keyword": "#0077CC",
    "builtin": "#0099FF",
    "string": "#FF77AA",
    "comment": "#55AA55",
    "number": "#AA55FF",
    "function": "#FFAA00",
    "class": "#FF5500",
}


def _get_tk_text_widget(ctk_textbox):
    """get underlying Tk Text widget from CTkTextbox"""
    for name in ("textbox", "text", "_text", "text_widget"):
        if hasattr(ctk_textbox, name):
            return getattr(ctk_textbox, name)
    return ctk_textbox


def highlight_code(textbox, event=None):
    """
    apply syntax highlighting to the textbox
    
    Args:
        textbox: CTkTextbox to highlight
        event: (optional) triggering event
    """
    text_widget = _get_tk_text_widget(textbox)

    # clear existing tags
    for tag in text_widget.tag_names():
        try:
            text_widget.tag_delete(tag)
        except:
            pass

    content = textbox.get("1.0", "end-1c")

    # do the comments first!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!(ノ▼Д▼)ノ
    comment_spans = []
    for m in re.finditer(r"#[^\n]*", content):
        s, e = m.start(), m.end()
        comment_spans.append((s, e))
        text_widget.tag_add("comment", f"1.0+{s}c", f"1.0+{e}c")

    def in_comment(s, e):
        """检查位置是否在注释内"""
        for cs, ce in comment_spans:
            if s >= cs and e <= ce:
                return True
        return False

    # apply other patterns
    for pattern, tag in PATTERNS:
        if tag == "comment":
            continue
        for m in re.finditer(pattern, content, re.DOTALL):
            s, e = m.start(), m.end()
            if in_comment(s, e):
                continue
            text_widget.tag_add(tag, f"1.0+{s}c", f"1.0+{e}c")

    # configure tag colors
    try:
        for tag, color in HIGHLIGHT_COLORS.items():
            text_widget.tag_config(tag, foreground=color)
    except:
        pass
