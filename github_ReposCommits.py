import json

import requests



def getRepos(userName):
    tempRep = requests.get('https://api.github.com/users/'+userName+'/repos')
    tempRep = tempRep.json()
    return len(tempRep)
    

def getCommits(userName, repoName):
    tempCommitRep = requests.get('https://api.github.com/repos/'+userName+'/'+repoName+'/commits')
    tempCommitRep = list(tempCommitRep)
    return len(tempCommitRep)


def getResponse(username) :
    tempURL = 'https://api.github.com/users/'+username+'/repos'
    return requests.get(tempURL)