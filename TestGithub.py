
import unittest

import requests

import github_ReposCommits

from github_ReposCommits import getRepos, getCommits, getResponse

from unittest.mock import patch, Mock


@patch('github_ReposCommits.requests.get')
class testGithubAPI(unittest.TestCase):
    def testGithubAPI_1(mock_get):
    	mock_get.return_value.status_code = 200
    	response = getResponse('ZainRaza14')
    	assertEqual(response.status_code, 200)

    
        
    


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
