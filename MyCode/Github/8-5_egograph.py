import networkx as nx
from github import Github


ACCESS_TOKEN = '6c0290bbdeaf247bc938fad14bb0a386f749f3b6'
USER = 'ptwobrussell'
REPO = 'Mining-the-Social-Web'

client = Github(ACCESS_TOKEN,per_page=100)
user = client.get_user(USER)
repo = user.get_repo(REPO)
g = nx.DiGraph()
g.add_node(repo.name + '(repo)', type='repo', lang=repo.language, owner=user.login)

stargazers = [s for s in repo.get_stargazers()]

for sg in stargazers:
    g.add_node(sg.login + '(user)', type='user')
    g.add_edge(sg.login + '(user)', repo.name + '(repo)', type='gazes')


print(nx.info(g))
print()

