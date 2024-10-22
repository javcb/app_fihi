import os
import re

def get_imports(file_path):
    imports = set()
    pattern = re.compile(r'^\s*import\s+(\w+)|^\s*from\s+(\w+)')
    with open(file_path, 'r') as file:
        for line in file:
            match = pattern.match(line)
            if match:
                imports.add(match.group(1) or match.group(2))
    return imports

def scan_directory(directory):
    project_files = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                imports = get_imports(file_path)
                project_files[file_path] = imports
    return project_files

def print_tree(directory, prefix=''):
    contents = os.listdir(directory)
    contents = sorted(contents, key=lambda s: s.lower())
    pointers = ['|-- ' if i < len(contents) - 1 else '`-- ' for i in range(len(contents))]
    for pointer, path in zip(pointers, contents):
        full_path = os.path.join(directory, path)
        if os.path.isdir(full_path):
            print(f"{prefix}{pointer}{path}/")
            print_tree(full_path, prefix + ('|   ' if pointer == '|-- ' else '    '))
        else:
            print(f"{prefix}{pointer}{path}")

def print_dependencies(project_files):
    print("Project Directory and Dependencies:\n")
    for file_path, imports in project_files.items():
        print(f"File: {file_path}")
        if imports:
            print(f"  Imports: {', '.join(imports)}")
        else:
            print("  No imports found.")
        print()

def main():
    # Get the path of the current script
    script_path = os.path.abspath(__file__)
    # Get the directory one level above the current script
    parent_dir = os.path.dirname(os.path.dirname(script_path))
    print(f"Scanning parent directory: {parent_dir}\n")

    project_files = scan_directory(parent_dir)

    print("Directory Tree:")
    print_tree(parent_dir)
    
    print("\nDependencies:")
    print_dependencies(project_files)

if __name__ == "__main__":
    main()


