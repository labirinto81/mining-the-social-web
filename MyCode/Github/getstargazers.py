from github import Github # pip install pygithub

# XXX: Specify your own access token here

ACCESS_TOKEN = '03c166090364f38fb8d88d0298c7c79507d0e5c6'

# Specify a username and repository of interest for that user.

USER = 'labirinto81'
REPO = 'mining-the-social-web'
#REPO = 'Mining-the-Social-Web-2nd-Edition'

client = Github(ACCESS_TOKEN, per_page=100)
user = client.get_user(USER)
repo = user.get_repo(REPO)

# Get a list of people who have bookmarked the repo.
# Since you'll get a lazy iterator back, you have to traverse
# it if you want to get the total number of stargazers.

stargazers = [ s for s in repo.get_stargazers() ]
print("Number of stargazers", len(stargazers))