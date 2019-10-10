import requests
import json

username = 'labirinto81' # Your GitHub username
password = 'Labirinto2017!' # Your GitHub password

# Note that credentials will be transmitted over a secure SSL connection
url = 'https://api.github.com/authorizations'
note = 'Mining the Social Web - Mining Github'
post_data = {'scopes':['repo'],'note': note }

response = requests.post(
    url,
    auth = (username, password),
    data = json.dumps(post_data),
    )

print("API response:", response.text)
print()
print("Your OAuth token is", response.json()['token'])

