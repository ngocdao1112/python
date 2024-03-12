import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url, verify=False)
print(response.json())