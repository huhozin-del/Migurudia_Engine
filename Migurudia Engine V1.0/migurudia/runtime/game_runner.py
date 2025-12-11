"""run and stop game"""

import sys
import os
import tempfile
import subprocess
import threading
import traceback

from config.settings import state
from .key_bridge import key_bridge
from .launcher_script import create_pygame_launcher_script


class GameRunner:
    """game runner to run and stop user code"""

    def __init__(self, console_widget, textbox_widget, preview_frame):
        """
        initialize GameRunner
        
        Args:
            console_widget: console output widget
            textbox_widget: code editor widget
            preview_frame: preveiw Frame
        """
        self.console = console_widget
        self.textbox = textbox_widget
        self.preview_frame = preview_frame

    def run(self):
        """run user code"""
        if state.is_running:
            print("⚠ Already running")
            return

        state.is_running = True
        self.console.delete("1.0", "end")
        self.textbox.configure(state="disabled")

        # reset key bridge
        key_bridge.reset()

        # initialize key bridge
        try:
            key_bridge.initialize()
        except Exception as e:
            self.console.insert("end", f"Error setting up key bridge: {e}\n", "error_tag")
            state.is_running = False
            self.textbox.configure(state="normal")
            return

        # ensure preview frame has focus
        self.preview_frame.configure(takefocus=True)
        self.preview_frame.focus_force()

        # get user code
        code = self.textbox.get("1.0", "end-1c")

        # create the Pygame launcher script
        embed_script = create_pygame_launcher_script(
            code,
            state.pygame_embed_window_id,
            state.preview_width,
            state.preview_height
        )

        # create temporary file for the script
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".py")
        tmp.write(embed_script.encode("utf-8"))
        tmp.close()

        # run in separate thread to avoid blocking UI
        def task():
            try:
                state.current_process = subprocess.Popen(
                    [sys.executable, "-u", tmp.name],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    stdin=subprocess.PIPE,
                    text=True,
                    encoding='utf-8',
                    bufsize=1
                )

                # read stdout
                while True:
                    output = state.current_process.stdout.readline()
                    if output == '' and state.current_process.poll() is not None:
                        break
                    if output:
                        self.console.insert("end", output)
                        self.console.see("end")

                # read stderr
                err = state.current_process.stderr.read()
                if err:
                    self.console.insert("end", err, "error_tag")
                    self.console.see("end")

                state.current_process.wait()

            except Exception:
                self.console.insert("end", traceback.format_exc(), "error_tag")

            finally:
                # clear
                try:
                    os.unlink(tmp.name)
                    key_bridge.cleanup()
                except:
                    pass

                state.is_running = False
                state.current_process = None
                key_bridge.reset()

                # restore textbox state in main thread
                self.textbox.after(100, lambda: self.textbox.configure(state="normal"))

        threading.Thread(target=task, daemon=True).start()

    #killllllllllllllllll the process(┛`д´)┛┻━┻
    def stop(self):
        """stop running user code"""
        if not state.is_running or state.current_process is None:
            return

        self.console.insert("end", "\n[System] Stopping process...\n", "error_tag")
        self.console.see("end")

        try:
            state.current_process.kill()
        except Exception as e:
            self.console.insert("end", f"\nError stopping: {e}\n", "error_tag")
