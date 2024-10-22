import os
import re
import subprocess
import sys
import traceback
import pkgutil

# Ensure setuptools is installed
try:
    import pkg_resources
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'setuptools'])
    import pkg_resources

# Function to get a list of all standard library modules
def get_standard_modules():
    standard_libs = {mod.name for mod in pkgutil.iter_modules() if mod.module_finder.path == os.path.dirname(sys.executable)}
    return standard_libs

def find_imports(directory):
    imports = set()
    pattern = re.compile(r'^\s*import\s+(\w+)|^\s*from\s+(\w+)')
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r') as f:
                    for line in f:
                        match = pattern.match(line)
                        if match:
                            imports.add(match.group(1) or match.group(2))
    return imports

def is_user_defined_module(module_name, directory):
    for root, _, files in os.walk(directory):
        if f"{module_name}.py" in files:
            return True
    return False

def install_packages(packages, project_dir):
    installed = []
    already_installed = []
    failed = {'not_found': [], 'permission_denied': [], 'other': []}

    standard_modules = get_standard_modules()

    for package in packages:
        if package in standard_modules:
            print(f"Skipping standard module: {package}")
            continue

        if is_user_defined_module(package, project_dir):
            print(f"Skipping user-defined module: {package}")
            continue

        try:
            print(f"Installing package: {package}")
            result = subprocess.check_output([sys.executable, '-m', 'pip', 'install', package], stderr=subprocess.STDOUT)
            result_text = result.decode('utf-8')
            if 'Requirement already satisfied' in result_text:
                already_installed.append(package)
            else:
                installed.append(package)
        except subprocess.CalledProcessError as e:
            error_message = str(e.output.decode('utf-8')).lower()
            if 'no matching distribution found' in error_message:
                failed['not_found'].append(package)
            elif 'permission denied' in error_message:
                failed['permission_denied'].append(package)
            else:
                failed['other'].append(package)

    return installed, already_installed, failed

def main():
    try:
        # Ensure pip is available
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pip'])

        # Find and install necessary imports
        project_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"Scanning project directory: {project_dir}")

        required_packages = find_imports(project_dir)
        print(f"Packages to install: {required_packages}")

        # Include non-standard library installations
        installed, already_installed, failed = install_packages(required_packages, project_dir)

        print("\nPip installs completed successfully:")
        for package in installed:
            print(f"  - {package}")

        print("\nPip installs already installed:")
        for package in already_installed:
            print(f"  - {package}")

        print("\nPip installs failed (No matching distribution found):")
        for package in failed['not_found']:
            print(f"  - {package}")

        print("\nPip installs failed (Permission denied):")
        for package in failed['permission_denied']:
            print(f"  - {package}")

        print("\nPip installs failed (Other reasons):")
        for package in failed['other']:
            print(f"  - {package}")

        print("All required packages have been processed.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()

