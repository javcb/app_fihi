#************************************ReadMe*******************************************
# This script is used to identify the processes using the specified folder.
#
#**********************************End ReadMe*******************************************
import os
import psutil

def find_processes_using_folder(folder_path):
    processes_using_folder = []
    
    for proc in psutil.process_iter(['pid', 'name', 'open_files']):
        try:
            for file in proc.info['open_files'] or []:
                if folder_path in file.path:
                    processes_using_folder.append((proc.info['pid'], proc.info['name']))
                    break
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return processes_using_folder

def main():
    folder_path = input("Enter the folder directory: ").strip()
    
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return
    
    processes = find_processes_using_folder(folder_path)
    
    if processes:
        print("Processes using the folder:")
        for pid, name in processes:
            print(f"PID: {pid}, Name: {name}")
    else:
        print("No processes found using the folder.")

if __name__ == "__main__":
    main()
