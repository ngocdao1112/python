# # POST

# import requests
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# api_url = "https://tagent-dev-api.tma-mgmt.com/account-service/login"
# data = { "username": "manager1", 
#         "password": "tma_12Tma" }
# response1 = requests.post(api_url, json = data, verify=False)
# access_token = response1.json()['access_token']

# print(response1.json())

# # ====================================================================

# # GET

# api_url = "https://tagent-dev-api.tma-mgmt.com/account-service/api/v1/user/getAll?first=1&max=100"

# response2 = requests.get(api_url, headers={'Authorization': 'Bearer ' + access_token}, verify=False)
# print(response2.json())


# ===================================================
# #!/usr/bin/env python

# import sys
# import requests

# def get_api_response(api_url):
#     response = requests.get(api_url)
#     return response.text

# def main():
#     # Read AGI environment variables
#     agi_env = {}
#     for line in sys.stdin:
#         key, value = line.strip().split(':', 1)
#         agi_env[key.strip()] = value.strip()

#     # Get API URL from AGI environment
#     api_url = "https://example.com/api"  # Replace with your API URL

#     # Make API call
#     api_response = get_api_response(api_url)

#     # Output response to AGI
#     print("SET VARIABLE API_RESPONSE {}".format(api_response))
#     print("EXEC Playback hello-world")  # Example: Play a message using Asterisk

# if __name__ == "__main__":
#     main()

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
    # Login API URL and credentials
    login_url = "https://tagent-dev-api.tma-mgmt.com/account-service/login"
    login_data = { "username": "manager1", "password": "tma_12Tma" }

    # Get access token
    access_token = get_access_token(login_url, login_data)
    print("Access Token:", access_token)

    # Get user data API URL
    user_api_url = "https://tagent-dev-api.tma-mgmt.com/account-service/api/v1/user/getAll?first=1&max=100"

    # Make API call to get user data
    user_data_response = get_api_response(user_api_url, headers={'Authorization': 'Bearer ' + access_token})
    print("\nUser Data Response:\n", user_data_response)

    # Print responses
    print("\nLogin API Response:\n", user_data_response)

if __name__ == "__main__":
    main()
