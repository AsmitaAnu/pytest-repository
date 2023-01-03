import requests

def git_repo():
    personal_access_token = "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"
    api_base_url = "https://api.github.com"

    data = {
        "name": "pytest-repository",
        "description": "This is my new repository",
        "private": False
    }
    response = requests.post(f"{api_base_url}/user/repos", json=data,
                             headers={"Authorization": f"Bearer {personal_access_token}"})
    return response.status_code

def test_git_repo():
    #value = git_regsiter()
    #assert value == 201
    assert git_repo() == 201

def git_login():
    username = 'AsmitaAnu'
    token = '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'

    login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(username, token))
    return login
    print('login')

#def test_git_login():
 #   assert git_login() == 201