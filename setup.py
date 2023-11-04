import os
import subprocess

try:
    subprocess.run(['go', 'install', 'github.com/charmbracelet/glow@latest'])

    go_bin_path = subprocess.check_output(['go', 'env', 'GOBIN'], universal_newlines=True).strip()

    glow_binary_path = os.path.join(go_bin_path, 'glow')
    glow_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'glow')
    os.makedirs(glow_directory, exist_ok=True)
    os.rename(glow_binary_path, os.path.join(glow_directory, 'glow'))

    print('Glow binary installed successfully!')
except Exception as e:
    print(f'Error: {e}')
