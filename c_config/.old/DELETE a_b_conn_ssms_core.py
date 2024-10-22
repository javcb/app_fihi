import pyodbc
import os


#-----------------------------------------------------------------------------

def conn_ssms():
    server = 'JCB\\SQL_EXPRESS_1'  # Your server name
    database = 'Core'  # Your database name
    username = 'sa'  # Replace with your username
    password = '30Madison!'  # Replace with your password

    connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    
    #connection_string = f"DRIVER={{SQL Server}};SERVER={os.environ[server]};DATABASE={os.environ[database]};UID={username};PWD={password}"
    
    #conn = pyodbc.connect(
    #    f"DRIVER={{SQL Server}};SERVER={os.environ[server]};"
    #    f"DATABASE={os.environ[database]};UID={os.environ[username]};PWD={os.environ[password]}"
    #)

    try:
        conn = pyodbc.connect(connection_string)
        print("Connection to SQL Server was successful.")
        return conn
    except Exception as e:
        print(f"Failed to connect to SQL Server: {e}")
        return None


