from flask import Flask, Request
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

app = Flask(__name__)


@app.route("/createJIRA", methods=['POST'])
def createJIRA():
    url = "https://saikishanjira.atlassian.net/rest/api/3/issue"
    github_payload = Request.get_json()
    print(github_payload)
    # Provide Your Email Address and API Token for username and password
    # you will have to create environment variables for these 2
    EMAIL = os.getenv("EMAIL")
    API_TOKEN = os.getenv("API_TOKEN")

    auth = HTTPBasicAuth(EMAIL, API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": "My First Jira Ticket.",
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    }
                ],
                "type": "doc",
                "version": 1
            },
            "issuetype": {
                "id": "10001"
                # Need to entry IssueType by ID. GO to Jira. Click on Manages Custom Filters. Select the issue Type
                # and from the URl You get the id for the issue type
            },
            "project": {
                "key": "SAIK"
                # You can give the project key here
            },

            "summary": "First, Jira Ticket",
        },
        "update": {}
    })

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))


app.run("0.0.0.0", port=5050)
