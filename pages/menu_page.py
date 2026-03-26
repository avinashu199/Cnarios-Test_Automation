from selenium.webdriver.common.by import By
import time

from pages.fileupload_page import FileUploadPage
from pages.frames_page import FramePage
from pages.webtables_page import WebtablesPage
from pages.windowhandle_page import WindowHandlePage
from utilities.scroll import Scroll
from utilities.waits import Waits


class MenuPage:
    frame = (By.XPATH, "//p[text()='iFrame']")
    file_upload = (By.XPATH, "//p[text()='File Upload']")
    table = (By.XPATH, "//p[text()='Table']")
    multi_window = (By.XPATH, "//p[text()='Multi Window']")
    try_it_yourself = (By.XPATH, "//div[@role='tablist']/child::button[2]")
    def __init__(self,driver):
        self.driver=driver
    def navigate_to_frame(self):
        self.driver.find_element(*MenuPage.frame).click()
        Scroll(self.driver).scroll_up()
        Waits(self.driver).element_to_be_clickable(MenuPage.try_it_yourself).click()
        return FramePage(self.driver)
    def navigate_to_fileupload(self):
        self.driver.find_element(*MenuPage.file_upload).click()
        Scroll(self.driver).scroll_up()
        Waits(self.driver).element_to_be_clickable(MenuPage.try_it_yourself).click()
        return FileUploadPage(self.driver)
    def navigate_to_table(self):
        self.driver.find_element(*MenuPage.table).click()
        Scroll(self.driver).scroll_up()
        Waits(self.driver).element_to_be_clickable(MenuPage.try_it_yourself).click()
        return WebtablesPage(self.driver)
    def navigate_to_multi_window(self):
        self.driver.find_element(*MenuPage.multi_window).click()
        Scroll(self.driver).scroll_up()
        Waits(self.driver).element_to_be_clickable(MenuPage.try_it_yourself).click()
        return WindowHandlePage(self.driver)
