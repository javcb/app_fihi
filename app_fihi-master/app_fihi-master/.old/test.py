import pyodbc

def conn_ssms():
    server = input("Enter the server name: ")
    database = input("Enter the database name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

    try:
        conn = pyodbc.connect(connection_string)
        print("Connection to SQL Server was successful.")
        return conn
    except Exception as e:
        print(f"Failed to connect to SQL Server: {e}")
        return None

# Call the function to connect to SQL Server using dynamic credentials
conn = conn_ssms()

# Use the connection object as needed
if conn:
    # Perform database operations using the conn object
    # ...
    conn.close()
else:
    print("Failed to establish a connection to SQL Server.")