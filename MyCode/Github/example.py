from github import Github

ACCESS_TOKEN = '03c166090364f38fb8d88d0298c7c79507d0e5c6'

#Get My Repos
g = Github("labirinto81","Labirinto2017!")
g = Github(ACCESS_TOKEN)

for repo in g.get_user().get_repos():
    print("Name:" + repo.name)
    print("Stars: " + str(repo.stargazers_count))








