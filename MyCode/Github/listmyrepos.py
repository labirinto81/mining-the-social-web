import getpass
import sys
from github import Github



username = 'labirinto81'
pw = getpass.getpass()
g = Github(username, pw)

for repo in g.get_user().get_repos():
    print (repo.name)