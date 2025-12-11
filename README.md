# Migurudia Engine

A lightweight game development engine based on Pygame, offering visual code editing, real-time preview, and one-click export functionality.

## Project Structure

```
migurudia/
├── main.py                 # Program entry point
├── config/                 # Configuration module
│   ├── __init__.py
│   ├── settings.py         # Global settings and state management
│   └── languages.py        # Multi-language support
├── ui/                     # User Interface module
│   ├── __init__.py
│   ├── app.py              # Main application
│   ├── home_frame.py       # Home page interface
│   ├── editor_frame.py     # Editor interface
│   └── tutorial_frame.py   # Tutorial interface
├── editor/                 # Code Editor module
│   ├── __init__.py
│   ├── syntax_highlight.py # Syntax highlighting
│   ├── autocomplete.py     # Autocompletion
│   └── line_numbers.py     # Line number display
├── runtime/                # Runtime module
│   ├── __init__.py
│   ├── key_bridge.py       # Tkinter-Pygame keyboard bridge
│   ├── launcher_script.py  # Pygame launch script generation
│   └── game_runner.py      # Game running control
├── file_ops/               # File Operations module
│   ├── __init__.py
│   ├── project_io.py       # Project save/load
│   ├── asset_import.py     # Asset import
│   └── export.py           # Export functionality
├── data/                   # Data module
│   ├── __init__.py
│   └── tutorials.py        # Tutorial content
└── assets/                 # Asset files
    ├── README.md
    ├── migurudia.ico       # (To be added)
    └── migurudia.png       # (To be added)
```

## Installation Dependencies

```bash
pip install customtkinter pygame pillow jedi
```

Optional dependencies (for exporting EXE):

```bash
pip install pyinstaller
```

## Running

```bash
cd migurudia
python main.py
```

## Module Descriptions

### config/

  - `settings.py`: Global state management (AppState class), color constants
  - `languages.py`: Chinese and English multi-language dictionary

### ui/

  - `app.py`: Main application class MigurdiaApp, manages interface switching
  - `home_frame.py`: Home page interface, containing create/load/import buttons
  - `editor_frame.py`: Code editor interface, containing preview window and console
  - `tutorial_frame.py`: Tutorial viewing interface

### editor/

  - `syntax_highlight.py`: Python syntax highlighting
  - `autocomplete.py`: Code completion based on Jedi
  - `line_numbers.py`: Line number display and synchronization

### runtime/

  - `key_bridge.py`: Synchronize keyboard state between Tkinter and Pygame subprocesses via temporary files
  - `launcher_script.py`: Generate embedded Pygame launch script
  - `game_runner.py`: Manage start and stop of Pygame subprocess

### file\_ops/

  - `project_io.py`: Saving and loading of project files
  - `asset_import.py`: Image/audio asset import
  - `export.py`: Export as Python script or EXE

### data/

  - `tutorials.py`: Chinese and English tutorial content

## Development Guide

### Add New Feature

1.  Determine the module the feature belongs to
2.  Create a new file or extend existing files in the corresponding module
3.  Export the new feature in the module's `__init__.py`
4.  Call the new feature in the UI layer

### Add New Language

1.  Add new language in `LANGUAGES` dictionary in `config/languages.py`
2.  Add corresponding tutorial translation in `TUTORIALS_DATA` in `data/tutorials.py`
3.  Add option in the language selector in `ui/home_frame.py`

## License

MIT License

# Migurudia Engine中文版README

一个基于 Pygame 的轻量级游戏开发引擎，提供可视化代码编辑、实时预览和一键导出功能。

## 项目结构

```
migurudia/
├── main.py                 # 程序入口
├── config/                 # 配置模块
│   ├── __init__.py
│   ├── settings.py         # 全局设置和状态管理
│   └── languages.py        # 多语言支持
├── ui/                     # 用户界面模块
│   ├── __init__.py
│   ├── app.py              # 主应用程序
│   ├── home_frame.py       # 主页界面
│   ├── editor_frame.py     # 编辑器界面
│   └── tutorial_frame.py   # 教程界面
├── editor/                 # 代码编辑器模块
│   ├── __init__.py
│   ├── syntax_highlight.py # 语法高亮
│   ├── autocomplete.py     # 自动补全
│   └── line_numbers.py     # 行号显示
├── runtime/                # 运行时模块
│   ├── __init__.py
│   ├── key_bridge.py       # Tkinter-Pygame 键盘桥接
│   ├── launcher_script.py  # Pygame 启动脚本生成
│   └── game_runner.py      # 游戏运行控制
├── file_ops/               # 文件操作模块
│   ├── __init__.py
│   ├── project_io.py       # 项目保存/加载
│   ├── asset_import.py     # 资源导入
│   └── export.py           # 导出功能
├── data/                   # 数据模块
│   ├── __init__.py
│   └── tutorials.py        # 教程内容
└── assets/                 # 资源文件
    ├── README.md
    ├── migurudia.ico       # (需要添加)
    └── migurudia.png       # (需要添加)
```

## 安装依赖

```bash
pip install customtkinter pygame pillow jedi
```

可选依赖（用于导出 EXE）：
```bash
pip install pyinstaller
```

## 运行

```bash
cd migurudia
python main.py
```

## 模块说明

### config/
- `settings.py`: 全局状态管理（AppState 类）、颜色常量
- `languages.py`: 中英文多语言字典

### ui/
- `app.py`: 主应用类 MigurdiaApp，管理界面切换
- `home_frame.py`: 主页界面，包含创建/加载/导入按钮
- `editor_frame.py`: 代码编辑器界面，包含预览窗口和控制台
- `tutorial_frame.py`: 教程查看界面

### editor/
- `syntax_highlight.py`: Python 语法高亮
- `autocomplete.py`: 基于 Jedi 的代码补全
- `line_numbers.py`: 行号显示和同步

### runtime/
- `key_bridge.py`: 通过临时文件在 Tkinter 和 Pygame 子进程间同步键盘状态
- `launcher_script.py`: 生成嵌入式 Pygame 启动脚本
- `game_runner.py`: 管理 Pygame 子进程的启动和停止

### file_ops/
- `project_io.py`: 项目文件的保存和加载
- `asset_import.py`: 图片/音频资源导入
- `export.py`: 导出为 Python 脚本或 EXE

### data/
- `tutorials.py`: 中英文教程内容

## 开发指南

### 添加新功能
1. 确定功能所属模块
2. 在对应模块中创建新文件或扩展现有文件
3. 在模块的 `__init__.py` 中导出新功能
4. 在 UI 层调用新功能

### 添加新语言
1. 在 `config/languages.py` 的 `LANGUAGES` 字典中添加新语言
2. 在 `data/tutorials.py` 的 `TUTORIALS_DATA` 中添加对应教程翻译
3. 在 `ui/home_frame.py` 的语言选择器中添加选项

## 许可证

MIT License# Migurudia_Engine
A lightweight game engine built with Pygame CE and CustomTkinter (CTK), designed for teaching Python programming and game development fundamentals. It provides a Scratch-like introduction to help beginners transition smoothly into writing Python code and creating their first games.
