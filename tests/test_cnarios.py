from pages.landing_page import LandingPage
import pytest

from utilities.datareader import DataReader

data=DataReader().payment_details()
@pytest.mark.parametrize("card_number,cvv,expiry_date",data)
def test_frames(browser_launch,card_number,cvv,expiry_date):
    driver=browser_launch
    menupage=LandingPage(driver).click_hands_on_practice()
    framepage=menupage.navigate_to_frame()
    framepage.switch_to_frame().enter_payment_details(card_number,cvv,expiry_date).click_paynow().switch_back()
def test_fileupload(browser_launch):
    driver=browser_launch
    menupage = LandingPage(driver).click_hands_on_practice()
    uploadpage = menupage.navigate_to_fileupload()
    uploadpage.upload_file().verify_preview()
def test_webtables(browser_launch):
    driver=browser_launch
    menupage = LandingPage(driver).click_hands_on_practice()
    webtable = menupage.navigate_to_table()
    webtable.handle_tables()
def test_windowhandles(browser_launch):
    driver=browser_launch
    menupage = LandingPage(driver).click_hands_on_practice()
    windows = menupage.navigate_to_multi_window()
    windows.click_window1().click_window2().handle_windows()


