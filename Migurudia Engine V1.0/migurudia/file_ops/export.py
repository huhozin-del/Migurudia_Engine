"""game export function(.PY AND .EXE)"""

import os
import sys
import tempfile
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog

from runtime.launcher_script import get_standalone_code


def export_as_python(textbox):
    """
    export as standalone .PY file
    
    Args:
        textbox: code editor widget
    """
    file_path = filedialog.asksaveasfilename(
        defaultextension=".py",
        filetypes=[("Python Files", "*.py")],
        title="Export as Python"
    )

    if not file_path:
        return

    code = textbox.get("1.0", "end-1c")
    standalone_code = get_standalone_code(code)

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(standalone_code)
        print(f"[Exported] {file_path}")
        print(f"[Info] Run with: python {os.path.basename(file_path)}")
    except Exception as e:
        print(f"[Error] Export failed: {e}")


def export_as_exe(textbox):
    """
    export as standalone .EXE file
    
    Args:
        textbox: code editor widget
    """
    # check PyInstaller availability
    try:
        import PyInstaller
        pyinstaller_available = True
    except ImportError:
        pyinstaller_available = False

    if not pyinstaller_available:
        print("[Error] PyInstaller not found!")
        print("[Info] Install it with: pip install pyinstaller")

        result = tk.messagebox.askyesno(
            "PyInstaller Not Found",
            "PyInstaller is required to create EXE files.\n\n"
            "Do you want to install it now?\n"
            "(This may take a minute)"
        )

        if result:
            print("[Info] Installing PyInstaller...")
            try:
                subprocess.run(
                    [sys.executable, "-m", "pip", "install", "pyinstaller"],
                    check=True
                )
                print("[Success] PyInstaller installed!")
            except Exception as e:
                print(f"[Error] Failed to install PyInstaller: {e}")
                return
        else:
            return

    # ask for output file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".exe",
        filetypes=[("Executable", "*.exe")],
        title="Export as EXE"
    )

    if not file_path:
        return

    output_dir = os.path.dirname(file_path)
    exe_name = os.path.splitext(os.path.basename(file_path))[0]

    code = textbox.get("1.0", "end-1c")
    standalone_code = get_standalone_code(code)

    temp_py = os.path.join(tempfile.gettempdir(), f"{exe_name}_temp.py")

    try:
        with open(temp_py, 'w', encoding='utf-8') as f:
            f.write(standalone_code)

        print(f"[Info] Building EXE... This may take a minute.")
        print(f"[Info] Output: {file_path}")

        # Locate assets
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            # Assumes assets are in a sibling 'assets' directory
            assets_dir = os.path.join(os.path.dirname(script_dir), "assets")
        except NameError:
            script_dir = os.getcwd()
            assets_dir = os.path.join(script_dir, "assets")

        icon_ico = os.path.join(assets_dir, "migurudia.ico")
        icon_png = os.path.join(assets_dir, "migurudia.png")

        print(f"[Debug] Assets dir: {assets_dir}")
        print(f"[Debug] ICO path: {icon_ico} (exists: {os.path.exists(icon_ico)})")
        print(f"[Debug] PNG path: {icon_png} (exists: {os.path.exists(icon_png)})")

        # Build command
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            "--noconsole",
            "--name", exe_name,
            "--distpath", output_dir,
            "--workpath", os.path.join(tempfile.gettempdir(), "pyinstaller_build"),
            "--specpath", tempfile.gettempdir(),
        ]

        # Include icons if they exist
        if os.path.exists(icon_ico):
            cmd.extend(["--icon", icon_ico])
            print(f"[Info] Using icon: {icon_ico}")

        if os.path.exists(icon_png):
            cmd.extend(["--add-data", f"{icon_png};."])
            print(f"[Info] Including: {icon_png}")

        cmd.append(temp_py)

        def build_task():
            try:
                result = subprocess.run(cmd, capture_output=True, text=True)

                if result.returncode == 0:
                    print(f"[Success] EXE created: {file_path}")
                    try:
                        os.unlink(temp_py)
                    except:
                        pass
                else:
                    print(f"[Error] Build failed:")
                    print(result.stderr)
            except Exception as e:
                print(f"[Error] Build failed: {e}")

        threading.Thread(target=build_task, daemon=True).start()

    except Exception as e:
        print(f"[Error] Export failed: {e}")
