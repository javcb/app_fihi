import sys
import os
import traceback
import json

print("Starting minimal script...")

try:
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Current directory: {current_dir}")

    # Construct the relative path to the subfolder
    subfolder_path = os.path.join(current_dir, 'a_config')
    print(f"Subfolder path: {subfolder_path}")

    # Add the subfolder to the Python path
    sys.path.append(subfolder_path)
    print(f"Updated sys.path: {sys.path}")

    # Import the module from the subfolder
    from a_b_conn_ssms_core import conn_ssms
    print("Module imported successfully")

    # SQL Server connection setup
    sql_script = 'SELECT TOP 10 * FROM dbo.DimCustomer'

    def fetch_sqltable_data():
        print("Inside fetch_sqltable_data function")
        conn = conn_ssms()
        if conn:
            print("Database connection successful")
            cursor = conn.cursor()
            cursor.execute(sql_script)
            rows = cursor.fetchall()
            conn.close()
            return [dict(EmailAddress=row.EmailAddress, FirstName=row.FirstName, LastName=row.LastName) for row in rows]
        else:
            print("Failed to connect to the database.")
            sys.exit(1)

    if __name__ == "__main__":
        print("Fetching data from the SQL table...")
        try:
            sqltable_data = fetch_sqltable_data()
            print("Data fetched successfully. Here it is:")
            print(json.dumps(sqltable_data, indent=4))
        except Exception as e:
            print(f"An error occurred during data fetching: {e}")
            traceback.print_exc()
        print("Script execution completed.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()
    print("Script execution completed.")




