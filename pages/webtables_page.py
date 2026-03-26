from selenium.webdriver.common.by import By
import time

class WebtablesPage:
    def __init__(self,driver):
        self.driver=driver
    def handle_tables(self):
        originals = self.driver.find_elements(By.XPATH, "//td[contains(@class,'css-1nafdkn')][2]")
        original_list = []
        for original in originals:
            original_list.append(original.text)
        sorted_list = sorted(original_list)
        heading = self.driver.find_element(By.XPATH, "//div[text()='Position']")
        heading.click()
        time.sleep(3)
        finals = self.driver.find_elements(By.XPATH, "//td[contains(@class,'css-1nafdkn')][2]")
        final_list = []
        for final in finals:
            final_list.append(final.text)
        assert sorted_list == final_list
        return self