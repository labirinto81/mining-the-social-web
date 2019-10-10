import json
import requests

# An unauthenticated request that doesn't contain an ?access_token=xxx query string
#url = "https://api.github.com/repos/ptwobrussell/Mining-the-Social-Web/stargazers"
url = "https://api.github.com/repos/labirinto81/mining-the-social-web"
response = requests.get(url)

# Display one stargazer
print(json.dumps(response.json()[0], indent=1))
print()

# Display headers
for (k,v) in response.headers.items():
    print(k, "=>", v)