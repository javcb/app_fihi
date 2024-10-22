import os
import subprocess
import sys

def install_package(package_name):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")

# Step 1: Install necessary packages if not already installed
install_package('pipreqs')
install_package('pip-review')

# Step 2: Change directory
os.chdir("C:\\Users\\amrjb\\OneDrive\\01_Dev\\02_Web_apps") # todo: update to relative path

# Step 3: Generate requirements.txt using python -m pipreqs
subprocess.call([sys.executable, '-m', 'pipreqs', '.', '--force'])

# Step 4: Update all packages using python -m pip-review
subprocess.call([sys.executable, '-m', 'pip-review', '--auto'])
