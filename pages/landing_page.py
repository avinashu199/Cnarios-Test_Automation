from selenium.webdriver.common.by import By

from pages.menu_page import MenuPage


class LandingPage:
    hands_on_practise =(By.XPATH, "//h3[text()='Hands-On Practice']")
    def __init__(self,driver):
        self.driver=driver
    def click_hands_on_practice(self):
        self.driver.find_element(*LandingPage.hands_on_practise).click()
        return MenuPage(self.driver)

