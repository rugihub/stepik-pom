from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class MainPage(BasePage): 

    def go_to_login_page(self):
        #link = self.browser.find_element_by_css_selector("#login_link")
        link = self.browser.find_element_by_id("login_link")
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        link.click() 
        
    def should_be_login_link(self):
        #assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        
        #assert self.is_element_present(By.ID, "login_link"), "Login link is present"
       
    




