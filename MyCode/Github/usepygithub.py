from github import Github

ACCESS_TOKEN = '6c0290bbdeaf247bc938fad14bb0a386f749f3b6'
USER = 'ptwobrussell'
REPO = 'Mining-the-Social-Web'

client = Github(ACCESS_TOKEN,per_page=100)
user = client.get_user(USER)
repo = user.get_repo(REPO)

stargazers = [ s for s in repo.get_stargazers()]
print("Number of stargazers", len(stargazers))


