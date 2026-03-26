from selenium.webdriver.common.by import By

from utilities.datareader import DataReader


class FileUploadPage:
    upload_button = (By.XPATH, "//input[@type='file']")
    preview_loc = (By.CSS_SELECTOR, ".whitespace-pre-wrap")
    def __init__(self, driver):
        self.driver = driver
    def upload_file(self):
        filepath=DataReader().file_location()
        self.driver.find_element(*FileUploadPage.upload_button).send_keys(filepath)
        return self
    def verify_preview(self):
        preview = self.driver.find_element(*FileUploadPage.preview_loc).is_displayed()
        if preview:
            print(self.driver.find_element(*FileUploadPage.preview_loc).text)
        else:
            assert False
        return self