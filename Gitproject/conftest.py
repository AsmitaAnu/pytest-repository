import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service = Service("C:\Users\bisoia\Downloads\chromedriver_win32\chromdriver.exe")
#driver = webdriver.Chrome(service=service)
@pytest.fixture
def browse():
# Create Chrome Object
    driver = webdriver.Chrome()
    yield driver
 #   driver.close()
#    service = Service(r"C:\Users\bisoia\Downloads\chromedriver_win32\chromdriver.exe")
 #driver = webdriver.Chrome(service=service)



