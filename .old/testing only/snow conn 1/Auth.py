import msal
import os
import configparser

def GetToken():
    configParser = configparser.ConfigParser()   
    configPath = os.path.join(os.path.dirname(__file__), 'config.txt')
    configParser.read(configPath)

    login = configParser.get('config', 'login')
    pwd = configParser.get('config', 'pass')
    authority = configParser.get('config', 'tenant')
    clientId = configParser.get('config', 'clientId')
    scope = configParser.get('config', 'scope')

    app = msal.PublicClientApplication(clientId, authority=authority)

    result = app.acquire_token_by_username_password(login, pwd, scopes=[scope])

    # print(result)
    return result["access_token"]
    