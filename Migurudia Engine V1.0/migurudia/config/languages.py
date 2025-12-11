#language system basically but only the text
"""multilingual support configuration"""

LANGUAGES = {
    "en": {
        "title": "Migurudia Engine",
        "create": "Create",
        "load": "Load",
        "import": "Import",
        "tutorials": "Tutorials",
        "theme": "Theme",
        "language": "Language",
        "File": "File",
        "New": "New",
        "Open": "Open",
        "Save": "Save",
        "SaveAs": "Save As",
        "Exit": "Exit",
        "Asset": "Asset",
        "Run": "Run",
        "Stop": "Stop",
        "ImportImage": "Import Image",
        "ImportSound": "Import Sound",
        "ImportAll": "Import All",
        "Export": "Export",
        "ExportExe": "Export as EXE",
        "ExportPy": "Export as Python"
    },
    "zh": {
        "title": "Migurudia Engine",
        "create": "新建",
        "load": "加载",
        "import": "导入",
        "tutorials": "教程",
        "theme": "主题",
        "language": "语言",
        "File": "文件",
        "New": "新建",
        "Open": "打开",
        "Save": "保存",
        "SaveAs": "另存为",
        "Exit": "退出",
        "Asset": "资源",
        "Run": "运行",
        "Stop": "停止",
        "ImportImage": "导入图片",
        "ImportSound": "导入音频",
        "ImportAll": "导入所有",
        "Export": "导出",
        "ExportExe": "导出为 EXE",
        "ExportPy": "导出为 Python"
    }
}

def get_text(lang: str, key: str) -> str:
    """get the string that the user choose"""
    return LANGUAGES.get(lang, LANGUAGES["en"]).get(key, key)
