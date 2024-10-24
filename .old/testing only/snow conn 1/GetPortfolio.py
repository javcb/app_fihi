# import Auth, configparser, json, os, requests, structlog
import requests, json
# from DefaultSettings import *
import msal
from requests.auth import HTTPProxyAuth
# log = structlog.get_logger()

# configParser = configparser.ConfigParser()   
# configPath = os.path.join(os.path.dirname(__file__), 'config.txt')
# configParser.read(configPath)
 
# baseUri = configParser.get('config', 'uri')

# configParser = configparser.ConfigParser()   
# configPath = os.path.join(os.path.dirname(__file__), 'config.txt')
# configParser.read(configPath)

uri = "https://client031.layeronesoftware.com:8085/POne/"
login = "svcRestApi031@client031cloud.onmicrosoft.com"
password = "DG1fL(x*KgOJ"
authority = "https://login.microsoftonline.com/organizations"
clientId = "2d3dec58-6fa8-4453-accd-5956dad5a881"
scope = "api://2d3dec58-6fa8-4453-accd-5956dad5a881/Api.Read"
DefaultValuationMode = 'Aperture'
DefaultStartDate = '2024-07-17'
DefaultEndDate = '2024-07-17'
DefaultForwardDate = '2023-12-07'
DefaultStrategy = 'TEST'

app = msal.PublicClientApplication(clientId, authority=authority)

result = app.acquire_token_by_username_password(login, password, scopes=[scope])
token = result["access_token"]


headers = {'Content-type': 'application/json',
           'Accept': 'text/plain',
           'Authorization': 'Bearer ' + token,
           'Proxy-Authorization': "6$9J!qhFPQ4s@Y"}
query = """SELECT   {Ticker},
                    {Security Description},
                    {ISIN},
                    {Sid},
                    {Legal Entity},
                    {Clearing Broker},
                    {Manager},
                    {Strategy},
                    {End Date},
                    {position_id},
                    {Forward Date},
                    {Bloomberg Global},
                    {Maturity Date Aperture},
                    {Fund Theoretical NAV End},
                    {Security Type}, {Bloomberg Code - Long},
                    {Gross MV}, {Option Strike}, {LoanX ID},
                    {End Forward}, {Any Coupon}, {Underlying Security Description},
                    {Exchange Country}, {Option Put Call Flag}, {Weighted Average End Price [N]},
                    {CUSIP}, {End Market Value}, {End Market Value [N]}, {End Price [N]},
                    {Implied Vol Today}, {Security Subtype}, {Security Expiration Date},
                    {Currency}, {Underlying Ticker}, {Underlying FX From Currency},
                    {FX From Currency}, {End FX Rate}, {End FX Rate Adj}, {Strategy 2},
                    {Strategy 3}, {FX To Currency}, {Underlying FX To Currency}, {End K Vol}
            FROM    {P1TC.Position}
            WHERE   {ReportingGroup.Id} = 4
            GROUP   BY {Sid}, {Legal Entity}, {Clearing Broker}, {Manager}, {Strategy}, {Forward Date}
                                    
							"""
postfilters = """""" 
withLocks = 'false'
proxy = {
    'http': "http://andrew.dennis%40apertureinvestors.com:Aperture_AD!@250-wired-zwcrqjvkgj.dynamic-m.com",
    'https': "http://andrew.dennis%40apertureinvestors.com:Aperture_AD!@250-wired-zwcrqjvkgj.dynamic-m.com"
}

# auth = HTTPProxyAuth("andrew.dennis@apertureinvestors.com", "6$9J!qhFPQ4s@Y")
response = requests.get(uri + "/Portfolio",
                        params = {'query': query, 
                                  'startDate': DefaultStartDate, 
                                  'endDate': DefaultEndDate, 
                                  'valuationMode': DefaultValuationMode,
                                  'postfilters': postfilters,
                                  'withLocks': withLocks},
                        proxies=proxy,
                        
                        headers=headers)



def process():
    result = json.loads(response.content)
    # print(result)

    print(type(result))


    # result= get_pql(query, DefaultStartDate, DefaultEndDate, DefaultValuationMode, postfilters, withLocks)

    result = json.loads(response.content)[0]
        

    yield (result['ticker'], result['manager'])

# 250-wired-zwcrqjvkgj.dynamic-m.com :
print(list(process()))