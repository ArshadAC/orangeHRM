import pytest
from selenium import webdriver



# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     driver.get("https://opensource-demo.orangehrmlive.com/")
#     driver.implicitly_wait(10)
#     return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("launching chrome browser")

    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching firefox browser")

    elif browser == 'edge':
        driver = webdriver.Edge()
        print("launching edge browser")

    else:
        print("Headless Mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

def pytest_metadata(metadata):
     # To Add
    metadata["Environment"] = "Test"
    metadata["Project Name"] = "OrangeHRM"
    metadata["Module Name"] = "Add Employee"
    metadata["Tester"] = "Arshad"
    # To remove
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)

@pytest.fixture(params=[
    ("Admin","admin123","Pass"),
    ("Admin1","admin123","Fail"),
    ("Admin","admin1231","Fail"),
    ("Admin1","admin1231","Fail")
])
def getDataforlogin(request):
    return request.param