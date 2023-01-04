def test_github_repo(browse):
    # Open github login page
    browse.get('https://github.com/login')

    # Username
    username = browse.find_element_by_xpath('//*[@id="login_field"]')
    username.send_keys("AsmitaAnu")

    # Password
    password = browse.find_element_by_xpath('//*[@id="password"]')
    password.send_keys("Asmita@7878")

    # Click on sign in button
    signin = browse.find_element_by_xpath(
        '//*[@id="login"]/div[4]/form/div/input[11]')
    signin.click()

    if browse.title == "Sign in to GitHub · GitHub":
        assert False, "Failed to Login"

        # Create new repo.
        new_repo = browse.find_element_by_xpath('//*[@id="repos-container"]/h2/a')
        new_repo.click()

        # Enter Repo. name
        repositoryname = browse.find_element_by_xpath('//*[@id="repository_name"]')
        repositoryname.send_keys("Myrepo")

        # Optional

        # Enter Description

        description = browse.find_element_by_xpath(
            '//*[@id="repository_description"]')
        description.send_keys("desc")

        # Private Mode

        private = browse.find_element_by_xpath(
            '//*[@id="repository_visibility_private"]')
        private.click()

