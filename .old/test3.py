from a_a_db_manager import get_connection
import json

def fetch_sqltable_data(conn, sql_script):
    cursor = conn.cursor()
    cursor.execute(sql_script)
    rows = cursor.fetchall()
    return [dict(EmailAddress=row.EmailAddress, FirstName=row.FirstName, LastName=row.LastName) for row in rows]

def main():
    print("Starting main function...")
    conn = get_connection()
    if conn:
        print("Fetching data from the SQL table...")
        sql_script = 'SELECT TOP 10 * FROM dbo.DimCustomer'  # Customize your SQL query here
        try:
            sqltable_data = fetch_sqltable_data(conn, sql_script)
            print("Data fetched successfully. Here it is:")
            print(json.dumps(sqltable_data, indent=4))
        except Exception as e:
            print(f"An error occurred during data fetching: {e}")
            input("Press any key to exit...")
        conn.close()
    else:
        print("Failed to establish a connection to SQL Server.")
        input("Press any key to exit...")

if __name__ == "__main__":
    print("Executing script...")
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    input("Press any key to exit...")
