from selenium.webdriver.common.by import By


class WindowHandlePage:
    window1 = (By.XPATH, "//li[text()='Learn about Button']")
    window2 = (By.XPATH, "//li[text()='Learn about Links']")
    message = (By.CSS_SELECTOR, ".css-aqzroz")
    def __init__(self,driver):
        self.driver=driver
    def click_window1(self):
        self.driver.find_element(*WindowHandlePage.window1).click()
        return self
    def click_window2(self):
        self.driver.find_element(*WindowHandlePage.window2).click()
        return self
    def handle_windows(self):
        windowtitles = self.driver.window_handles
        self.driver.switch_to.window(windowtitles[1])
        window1_message = self.driver.find_element(*WindowHandlePage.message).text
        if window1_message == "Button":
            self.driver.close()
        else:
            assert False
        self.driver.switch_to.window(windowtitles[2])
        window2_message = self.driver.find_element(*WindowHandlePage.message).text
        if window2_message == "Link":
            self.driver.close()
        else:
            assert False
        return self
