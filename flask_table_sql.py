from flask import Flask, render_template
import pyodbc
import pandas as pd
import subprocess
import sys
import os

app = Flask(__name__, template_folder='t_templates')

# Function to get a connection to the SQL Server
def get_connection():
    server = 'JCB\\SQL_EXPRESS_1'  # Replace with your server name
    database = 'Core'  # Replace with your database name
    username = 'sa'  # Replace with your username
    password = '30Madison!'  # Replace with your password
    connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    conn = pyodbc.connect(connection_string)
    return conn

@app.route('/')
def index():
    script_path = "C:\\Users\\amrjb\\OneDrive\\01_Dev\\02_Web_apps\\app_fihi\\d_data\\browse_sql.py"
    if not os.path.isfile(script_path):
        return f"Script path does not exist: {script_path}"
    
    try:
        result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        if result.returncode != 0:
            return f"Error running browse_sql.py: {result.stderr}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

    conn = get_connection()
    sql_query = 'SELECT TOP 10 * FROM dbo.DimCustomer'  # Customize your SQL query
    df = pd.read_sql(sql_query, conn)
    conn.close()
    return render_template('table_sql1.html', tables=[df.to_html(classes='data', header="true", index=False)])

if __name__ == '__main__':
    app.run(debug=True)
