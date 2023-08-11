import pytest
from selenium import webdriver

"""
In pytest, hook functions are functions that can be used to extend or
modify the behavior of pytest. They are called automatically by pytest at
specific times during the test run.

The pytest_configure function is a hook function in pytest that is called once the
configuration object has been created and all plugins and initial conftest files have been loaded.

The pytest_addoption function is a hook function in pytest that is used to add custom command-line options to the
pytest command. It takes a single argument, parser, which is an instance of the argparse.ArgumentParser class.
"""


def pytest_addoption(parser):
    parser.addoption("--browser")


"""
Define the browser fixture function with a single argument, request.
Within the browser function, use the request.config.getoption() method 
to get the value of the --browser option passed to pytest on the command line
"""


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


"""
The pytest_metadata function is a hook function in pytest that allows you to
add custom metadata to the test report. This metadata can be used to provide
additional information about the test run, such as the environment, the test data,
or any other relevant information.
"""


def pytest_metadata(metadata):
    # To Add
    metadata["Environment"] = "Test"
    metadata["Project Name"] = "OrangeHRM"
    metadata["Module Name"] = "Employee"
    metadata["Tester"] = "Prince"
    # To Remove
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)


@pytest.fixture(params=[
    ("Admin", "admin123", "Pass"),
    ("Admin1", "admin123", "Fail"),
    ("Admin", "admin1234", "Fail"),
    ("Admin1", "admin1234", "Fail")
])
def getDataForLogin(request):
    return request.param


@pytest.fixture(params=[
    ("Prince", "Kurmi", "Pass"),
    ("", "admin123", "Fail"),
    ("Admin", "", "Fail")
])
def getDataForEmp(request):
    return request.param


# @pytest.fixture()
# def setup():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument("headless")
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     return driver
