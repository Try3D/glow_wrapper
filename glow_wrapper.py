import subprocess
import os


class GlowWrapper:
    def __init__(self, glow_path=None):
        if glow_path:
            self.glow_path = glow_path
        else:
            current_directory = os.path.dirname(os.path.realpath(__file__))
            self.glow_path = os.path.join(current_directory, "glow", "glow")

    def render_markdown(self, input_file, width=80, style="dark"):
        try:
            return subprocess.check_output(
                [self.glow_path, "--width", str(width), "--style", style, input_file],
                stderr=subprocess.PIPE,
                universal_newlines=True,
            )
        except subprocess.CalledProcessError as e:
            return f'Error: {e}'
