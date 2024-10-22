import requests
import json
import pyodbc

# Step 1: Fetch data from the BLS API
headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['CUUR0000SA0', 'SUUR0000SA0'], "startyear": "2011", "endyear": "2014"})
response = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)

if response.status_code == 200:
    json_data = json.loads(response.text)

    print(f"Error: {response.status_code} - {response.text}")

print(json_data)
