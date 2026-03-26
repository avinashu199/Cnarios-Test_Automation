from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Waits:
    def __init__(self, driver):
        self.driver=driver
    def element_to_be_clickable(self,locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.element_to_be_clickable(locator))