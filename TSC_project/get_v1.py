import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_all_user(access_token):
    api_url = "https://tagent-dev-api.tma-mgmt.com/account-service/api/v1/user/getAll?first=1&max=100"

    response2 = requests.get(api_url, headers={'Authorization': 'Bearer ' + access_token}, verify=False)
    print(response2.json())