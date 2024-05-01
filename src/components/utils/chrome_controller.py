from selenium import webdriver

class ChromeController:
    def __init__(self):
        self.driver = None
        
    def start_browser(self, driver_path:str): self.driver = webdriver.Chrome(executable_path=driver_path)

    def open_url(self, url:str): self.driver.get(url)

    def quit_browser(self):
        if self.driver: self.driver.quit()