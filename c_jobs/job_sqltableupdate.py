import os
import pandas as pd
import pyodbc
from datetime import datetime

# Configuration
folder_path = "C:\\Path\\To\\Your\\Folder"  # Update this to the specific folder path
expected_headers = ["Column1", "Column2", "Column3"]  # Update this to the expected headers of your CSV files
sql_server = "JCB\\SQL_EXPRESS_1"
database = "Core"
username = "sa"
password = "30Madison!"
table_name = "your_table"

# Function to get a connection to the SQL Server
def get_connection():
    connection_string = f"DRIVER={{SQL Server}};SERVER={sql_server};DATABASE={database};UID={username};PWD={password}"
    conn = pyodbc.connect(connection_string)
    return conn

def main():
    # List to store error messages
    error_files = []
    
    # DataFrame to hold all the data
    appended_data = pd.DataFrame()
    
    # Scan the folder for CSV files
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            try:
                df = pd.read_csv(file_path)
                if list(df.columns) != expected_headers:
                    raise ValueError(f"Incorrect headers in file: {file_name}")
                appended_data = pd.concat([appended_data, df], ignore_index=True)
            except Exception as e:
                error_files.append(file_name)
                print(f"Error processing file {file_name}: {e}")

    # If there were any errors, print them
    if error_files:
        print("\nThe following files were skipped due to header mismatches:")
        for error_file in error_files:
            print(error_file)
    
    # Replace the content in the specified SQL Server table
    if not appended_data.empty:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table_name}")  # Clear existing content in the table
        for index, row in appended_data.iterrows():
            insert_query = f"INSERT INTO {table_name} ({', '.join(expected_headers)}) VALUES ({', '.join(['?'] * len(expected_headers))})"
            cursor.execute(insert_query, tuple(row))
        conn.commit()
        conn.close()
        print(f"Data from {len(os.listdir(folder_path)) - len(error_files)} files appended to the {table_name} table in SQL Server.")
    else:
        print("No data to append.")

if __name__ == "__main__":
    main()

