import os
import time
from datetime import datetime
import pandas as pd
import win32com.client as win32

# Configuration
onedrive_path = "C:\\Users\\amrjb\\OneDrive\\01_SourceData\\Admin"  # Update this to the specific OneDrive path you're monitoring
tracked_files_file = "tracked_files.csv"

# Email Configuration
recipient_email = "javier.c.benitez@gmail.com"
subject = "New File Notification"
body_template = "A new file has been added: {}"

"A new file has been added: {}"

# Load the list of already tracked files
if os.path.exists(tracked_files_file):
    tracked_files = pd.read_csv(tracked_files_file)
else:
    tracked_files = pd.DataFrame(columns=["Filename", "Timestamp"])

def send_email(file_name):
    body = body_template.format(file_name)
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient_email
    mail.Subject = subject
    mail.Body = body
    mail.Send()

def scan_folder():
    global tracked_files
    print(f"Scanning folder at {datetime.now()}")
    new_entries = []
    for root, dirs, files in os.walk(onedrive_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path not in tracked_files['Filename'].values:
                print(f"New file detected: {file}")
                send_email(file)
                new_entries.append({"Filename": file_path, "Timestamp": datetime.now()})
    
    if new_entries:
        new_df = pd.DataFrame(new_entries)
        tracked_files = pd.concat([tracked_files, new_df], ignore_index=True)
        tracked_files.to_csv(tracked_files_file, index=False)

while True:
    current_time = datetime.now().time()
    if current_time.hour >= 17:  # 5 PM EST
        print("Stopping script as it's past 5 PM EST")
        break
    scan_folder()
    time.sleep(1800)  # Sleep for 30 minutes