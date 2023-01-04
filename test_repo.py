import requests
def git_create_repo():

    personal_access_token = "ghp_tqyftdodijlwsdoudgftytg"
    api_base_url = "https://api.github.com"

    data = {
    "name": "pytest-repository",
    "description": "This is my new repository",
    "private": False
    }

    response = requests.post(f"{api_base_url}/user/repos", json=data, headers={"Authorization": f"Bearer {personal_access_token}"})

    return response.status_code

    

def test_git_create_repo():
    value = git_create_repo()
    assert value == 201


def git_login():

    personal_access_token = "ghp_tqyftdodijlwsdoudgftytg"
    api_base_url = "https://api.github.com"

    response = requests.get(f"{api_base_url}/user/repos", headers={"Authorization": f"Bearer {personal_access_token}"})

    #return response.status_code
    return response.status_code

    
def test_git_login():
    login = git_login()
    assert login == 200
