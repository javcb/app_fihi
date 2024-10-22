import pyodbc
import json
import os

CREDENTIALS_FILE = 'credentials.json'

def load_credentials():
    print("Loading credentials...")
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'r') as file:
            return json.load(file)
    return None

def save_credentials(server, database, username, password):
    print("Saving credentials...")
    credentials = {
        'server': server,
        'database': database,
        'username': username,
        'password': password
    }
    with open(CREDENTIALS_FILE, 'w') as file:
        json.dump(credentials, file)

def conn_ssms(server, database, username, password):
    connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    try:
        print("Attempting to connect to SQL Server...")
        conn = pyodbc.connect(connection_string)
        print("Connection to SQL Server was successful.")
        return conn
    except pyodbc.Error as e:
        print(f"Failed to connect to SQL Server: {e}")
        return None

def get_connection():
    credentials = load_credentials()
    if credentials:
        conn = conn_ssms(credentials['server'], credentials['database'], credentials['username'], credentials['password'])
        if conn:
            return conn
        else:
            print("Failed to connect with saved credentials.")

    while True:
        server = input("Enter server: ")
        database = input("Enter database: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        conn = conn_ssms(server, database, username, password)
        if conn:
            save_credentials(server, database, username, password)
            return conn
        else:
            print("Invalid credentials, please try again.")

