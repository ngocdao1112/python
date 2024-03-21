import requests
import urllib3
import get_v1

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_url = "https://tagent-dev-api.tma-mgmt.com/account-service/login"
data = { "username": "agent1", 
        "password": "tma_12Tma" }
response1 = requests.post(api_url, json = data, verify=False)
access_token = response1.json()['access_token']
print(response1.json())

get_v1.get_all_user(access_token)