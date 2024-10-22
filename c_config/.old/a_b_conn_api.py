from sys import api_version
import requests
import json
#import pyodbc

# Step 1: Fetch data from the BLS API
#headers = {'Content-type': 'application/json'}
#data = json.dumps({"seriesid": ['CUUR0000SA0', 'SUUR0000SA0'], "startyear": "2011", "endyear": "2014"})
#response = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)

#if response.status_code == 200:
#    json_data = json.loads(response.text)
#    print(f"Error: {response.status_code} - {response.text}")

#print(json_data)


#JB: create list of available api names on front end with required parameters to feed into these definitions
api_address = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'
headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['CUUR0000SA0', 'SUUR0000SA0'], "startyear": "2011", "endyear": "2014"})

def fetch_api_data(city):
    response = requests.post(f'api_address', data=data, headers=headers)
    return response.json()

#if fetch_api_data.status_code == 200:
#    json_data = json.loads(fetch_api_data.text)
#    print(f"Error: {fetch_api_data.status_code} - {fetch_api_data.text}")

print(fetch_api_data)


#optimized version example
#import requests

#def fetch_weather_data(city):
#    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.environ["WEATHER_API_KEY"]}')
#    return response.json()

