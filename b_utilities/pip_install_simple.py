
import subprocess
import sys

def install_package(package_name):
    try:
        print(f"Attempting to install package: {package_name}")
        result = subprocess.check_output([sys.executable, '-m', 'pip', 'install', package_name], stderr=subprocess.STDOUT)
        result_text = result.decode('utf-8')
        if 'Requirement already satisfied' in result_text:
            return f"The package '{package_name}' is already installed."
        else:
            return f"The package '{package_name}' was installed successfully."
    except subprocess.CalledProcessError as e:
        error_message = str(e.output.decode('utf-8')).lower()
        if 'no matching distribution found' in error_message:
            return f"Failed to install '{package_name}': No matching distribution found."
        elif 'permission denied' in error_message:
            return f"Failed to install '{package_name}': Permission denied."
        else:
            return f"Failed to install '{package_name}': {e}"

def main():
    package_name = input("Enter the name of the package you want to install: ").strip()
    result_message = install_package(package_name)
    print(result_message)

if __name__ == "__main__":
    main()
