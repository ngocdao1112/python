#!/usr/bin/env python

import sys
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_access_token(api_url, data):
    response = requests.post(api_url, json=data, verify=False)
    return response.json().get('access_token')

def get_api_response(api_url, headers):
    response = requests.get(api_url, headers=headers, verify=False)
    return response.json()

def main():
    sys.stderr.write("\n\t\t\t========================= API log message ========================= \n")

    # Login API URL and credentials
    login_url = "https://tagent-dev-api.tma-mgmt.com/account-service/login"
    login_data = { "username": "manager1", "password": "tma_12Tma" }

    # Get access token
    access_token = get_access_token(login_url, login_data)
    sys.stderr.write("\nAccess Token: " + str(access_token) + "\n")

    # Get user data API URL
    user_api_url = "https://tagent-dev-api.tma-mgmt.com/account-service/api/v1/user/count/all"

    # Make API call to get user data
    user_data_response = get_api_response(user_api_url, headers={'Authorization': 'Bearer ' + access_token})

    # Print responses
    sys.stderr.write("\nLogin API Response: " + str(user_data_response) + "\n\n")

if __name__ == "__main__":
    main()

