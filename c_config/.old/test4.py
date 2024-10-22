import sys
import os
import traceback
import json

print("Starting minimal script...")

try:
    # Get the path of the current script
    script_path = os.path.abspath(__file__)

    # Print the current directory
    print("Current script:", script_path)

    # Get the directory one level above the current script
    parent_dir = os.path.dirname(os.path.dirname(script_path))

    # Print the parent directory
    print("Parent directory:", parent_dir)

    # Iterate over all subfolders in the base directory
    for root, dirs, files in os.walk(parent_dir):
        # Check if the module file exists in the current subfolder
        module_path = os.path.join(root, 'a_1_sql_login.py')
        if os.path.isfile(module_path):
            # Add the parent folder of the module to the Python path
            sys.path.append(os.path.dirname(module_path))
            break

    # Import the module from the subfolder
    try:
        from a_1_sql_login import get_connection
    except ModuleNotFoundError:
        print("The module a_1_sql_login could not be found.")
        print("Python search paths:")
        for path in sys.path:
            print(path)

    #----------------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------
    from decimal import Decimal

    class DecimalEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Decimal):
                return float(obj)
            return super(DecimalEncoder, self).default(obj)

    def fetch_sqltable_data(conn, sql_script):
        try:
            print("Creating cursor...")
            cursor = conn.cursor()
            print("Executing SQL script...")
            cursor.execute(sql_script)
            print("Fetching all rows...")
            rows = cursor.fetchall()
            print("Rows fetched successfully.")
            # Get column names
            columns = [column[0] for column in cursor.description]
            # Construct a list of dictionaries with column names as keys
            results = [dict(zip(columns, row)) for row in rows]
            return results
        except pyodbc.Error as e:
            print(f"An error occurred while fetching data: {e}")
            traceback.print_exc()
            return []

    def main():
        print("Starting main function...")
        conn = get_connection()
        if conn:
            print("Fetching data from the SQL table...")
            sql_script = 'SELECT * FROM dbo.DimCustomer'  # Customize your SQL query here to fetch all columns
            try:
                sqltable_data = fetch_sqltable_data(conn, sql_script)
                if sqltable_data:
                    print("Data fetched successfully. Here it is:")
                    print(json.dumps(sqltable_data, indent=4, cls=DecimalEncoder))
                    print(f"Total number of records fetched: {len(sqltable_data)}")
                else:
                    print("No data fetched.")
            except Exception as e:
                print(f"An error occurred during data fetching: {e}")
                traceback.print_exc()
            finally:
                conn.close()
        else:
            print("Failed to establish a connection to SQL Server. Please check your credentials and try again.")

    if __name__ == "__main__":
        print("Executing script...")
        try:
            main()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            traceback.print_exc()
        print("Script execution completed.")
    #----------------------------------------------------------------------------------------------
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()
    print("Script execution completed.")
