import  time
def test_github_repo(browse):
    # Open github login page
    browse.get('https://github.com/login')

    # Username
    username = browse.find_element_by_xpath('//*[@id="login_field"]')
    username.send_keys("AsmitaAnu")

    # Password
    password = browse.find_element_by_xpath('//*[@id="password"]')
    password.send_keys("AsmitaAnu1234")
    time.sleep(2)

    # Click on sign in button
    signin = browse.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[11]')
#    signin = browse.find_element_by_xpath('/html[1]/body[1]/div[1]/div[3]/main[1]/div[1]/div[4]/form[1]/div[1]/input[11]')
    signin.click()

# if browse.title == "Sign in to GitHub · GitHub":
#        assert False, "Failed to Login"
    time.sleep(2)

# Create new repo.
    new_repo = browse.find_element_by_xpath("//div[@data-target='loading-context.details']//a[@class='btn btn-sm btn-primary'][normalize-space()='New']")
    new_repo.click()

 # Enter Repo. name
    repositoryname = browse.find_element_by_xpath('//*[@id="repository_name"]')
    repositoryname.send_keys("Myrepo")
    time.sleep(2)

# Click on Create Repo
    create_repo = browse.find_element_by_xpath("//button[normalize-space()='Create repository']")
    create_repo.click()
    time.sleep(5.5)



