from selenium import webdriver
import pytest

from utilities.datareader import DataReader

def pytest_addoption(parser):
    parser.addoption("--headless",action="store_true",default=False)

@pytest.fixture(params=["Chrome","Edge"])
def browser_launch(request):
    browser=request.param
    type=request.config.getoption("--headless")
    if browser=="Chrome":
        if not type:
            driver = webdriver.Chrome()
            driver.implicitly_wait(3)
            url = DataReader().url()
            driver.get(url)
            driver.set_window_size(1920, 1080)
            yield driver
            driver.quit()
        else:
            option=webdriver.ChromeOptions()
            option.add_argument("--headless")
            driver = webdriver.Chrome(options=option)
            driver.implicitly_wait(3)
            url = DataReader().url()
            driver.get(url)
            driver.set_window_size(1920, 1080)
            yield driver
            driver.quit()

    elif browser=="Edge":
        if not type:
            driver = webdriver.Edge()
            driver.implicitly_wait(3)
            url = DataReader().url()
            driver.get(url)
            driver.set_window_size(1920, 1080)
            yield driver
            driver.quit()
        else:
            option=webdriver.EdgeOptions()
            option.add_argument("--headless")
            driver = webdriver.Edge(options=option)
            driver.implicitly_wait(3)
            url = DataReader().url()
            driver.get(url)
            driver.set_window_size(1920, 1080)
            yield driver
            driver.quit()
