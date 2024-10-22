# Create Data Access Layer (DAL): Combine data fetching from SQL Server and API.
import pyodbc
import requests
import json

    # Step 2: Connect to SQL Server
server = 'JCB\\SQL_EXPRESS_1'  # Your server name
database = 'Core'  # Your database name
username = 'sa'  # Replace with your username
password = '30Madison!'  # Replace with your password

connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'



def fetch_adventureworks_data():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT TOP 10 * FROM dbo.DimCustomer')
    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_adventureworks_storedproc():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute('EXEC dbo.GetCustomerData')
    rows = cursor.fetchall()
    conn.close()
    return [dict(EmailAddress=row.EmailAddress, FirstName=row.FirstName, LastName=row.LastName) for row in rows]
    
######################
##def fetch_weather_data(city):
##    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=your_api_key')
##    return response.json()
######################

def fetch_blsdata():
    headers = {'Content-type': 'application/json'}
    data = json.dumps({"seriesid": ['CUUR0000SA0', 'SUUR0000SA0'], "startyear": "2011", "endyear": "2014"})
    response = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
    return response.json()

#    if response.status_code == 200:
#        json_data = json.loads(response.text)
#        print(f"Error: {response.status_code} - {response.text}")

adventureworks_data = fetch_adventureworks_data()
adventureworks_sproc = fetch_adventureworks_storedproc()
#weather_data = fetch_weather_data('London')
blsdata = fetch_blsdata()

print(adventureworks_data)
print('--------------------------')
print(json.dumps(adventureworks_sproc))
print('--------------------------')
print(blsdata)
