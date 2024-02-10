# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

#Enter the URL of the jra software
url = "https://saikishanjira.atlassian.net/rest/api/3/project"

# Provide Your Email Address and API Token for username and password
EMAIL = input("Please enter your JIRA email address: ")
API_TOKEN = input("Enter your JIRA API-TOKEN for listing the projects: ")

auth = HTTPBasicAuth("sai.kishan.sastry@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
name = output[1]["name"]
print(name)