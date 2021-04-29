import requests
import sys
import csv
from time import sleep


def token(username, password,server):
    r = None
    headers = {'Content-Type': 'application/json'}
    url = 'https://' + server + '/api/fmc_platform/v1/auth/generatetoken'
    try:
        #print ("pushing .................generating auth token")
        #print("url: "+url)
        r = requests.post(url, headers=headers, auth=requests.auth.HTTPBasicAuth(username,password), verify=False)
        auth_headers = r.headers
        auth_token = auth_headers.get('X-auth-access-token', default=None)
        if auth_token == None:
            print("auth_token not found. Exiting...")
            #sleep(4)
            #auth_token = GetToken(username, password, server)
    except Exception as err:
        print ("Error in generating auth token --> "+str(err))
        #sleep(10)
        #auth_token = GetToken(username, password, server)

    #headers['X-auth-access-token']=auth_token
    return auth_token

