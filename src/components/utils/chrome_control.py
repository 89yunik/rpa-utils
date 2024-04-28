from selenium import webdriver

class Chrome:
    def __init__(self, driver_path:str):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def get_url(self, url:str): self.driver.get(url)