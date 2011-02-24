# pip install github2
from github2.client import Github

from random import choice

github = Github()
repos = github.repos.network('github/pycon2011')

print "And the winners are..."
print "*drumroll*"
print "%s and %s!" % ( choice(repos)['owner'], choice(repos)['owner'] )
