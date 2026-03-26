import time

from selenium.webdriver.common.by import By


class FramePage:
    card_number = (By.CSS_SELECTOR, "#cardNumber")
    expiry = (By.CSS_SELECTOR, "#expiry")
    cvv = (By.CSS_SELECTOR, "#cvv")
    paynow =(By.CSS_SELECTOR, "#pay-btn")
    close = (By.CSS_SELECTOR, ".css-j7n7h8")
    def __init__(self,driver):
        self.driver=driver
    def switch_to_frame(self):
        frame=self.driver.find_element(By.XPATH, "//iframe[@title='Payment Form']")
        self.driver.switch_to.frame(frame)
        return self
    def enter_payment_details(self,card_number,cvv,expiry):
        self.driver.find_element(*FramePage.card_number).send_keys(card_number)
        self.driver.find_element(*FramePage.expiry).send_keys(expiry)
        self.driver.find_element(*FramePage.cvv).send_keys(cvv)
        return self
    def click_paynow(self):
        self.driver.find_element(*FramePage.paynow).click()
        return self
    def switch_back(self):
        self.driver.switch_to.default_content()
        self.driver.find_element(*FramePage.close).click()
        return self

