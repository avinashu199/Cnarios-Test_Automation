class Scroll:
    def __init__(self,driver):
        self.driver=driver
    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        return self