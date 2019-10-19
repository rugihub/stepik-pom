import pytest
from selenium import webdriver

def pytest_addoption(parser):     
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en or ru")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    language = "en"
    if user_language == "en": language = "en"
    elif user_language == "ru": language = "ru"
    else:
        raise pytest.UsageError("--language should be en or ru")  
    
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")   
            
    yield browser
    print("\nquit browser..")
    browser.quit()
