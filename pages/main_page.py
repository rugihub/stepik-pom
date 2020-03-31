from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class MainPage(BasePage): 

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)        
        
    def should_be_login_link(self):
        #assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not present"
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not present"
              
       
    



