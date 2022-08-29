import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: chrome or edge"
    )


@pytest.fixture(scope="class")
def begin_end(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        webdriver_obj = webdriver.Chrome(service=Service("C:/Users/dines/OneDrive/Documents/MyPythonProject/chromedriver.exe"))
    elif browser_name == "edge":
        webdriver_obj = webdriver.Edge(service=Service("C:/Users/dines/OneDrive/Documents/MyPythonProject/chromedriver.exe"))
    else:
        print("invalid browser name")
    webdriver_obj.get("http://automationpractice.com")
    webdriver_obj.maximize_window()
    webdriver_obj.implicitly_wait(5)
    mouse_hover = ActionChains(webdriver_obj)
    request.cls.webdriver_obj = webdriver_obj
    request.cls.mouse_hover = mouse_hover








