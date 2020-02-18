import json

import requests

from github_ReposCommits import getRepos, getCommits

import unittest

class testGithubAPI(unittest.TestCase):

    def testGithubAPI_1(self): 
        self.assertEqual(getRepos('ZainRaza14'), 30)

    def testGithubAPI_2(self): 
        self.assertEqual(getCommits('ZainRaza14', 'AI-Car-Controller'), 126)
        
    


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
