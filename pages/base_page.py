from selenium.common.exceptions import NoSuchElementException, TimeoutException
from urllib3.exceptions import ReadTimeoutError
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import time

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.browser.implicitly_wait(self.timeout)
    
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
    
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    
    def is_not_element_present(self, how, what, timeout=4):
       try:
           WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
       except TimeoutException:
           return True
       return False
    
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    
    def open(self):
        attempt = 0
        while attempt < 4:
            print(f"Attempt: {attempt}")
            try:
                self.browser.get(self.url)
                time.sleep(5)
                return
            except ReadTimeoutError as e:
                self.browser.switch_to.new_window("tab")
                self.browser.implicitly_wait(self.timeout)
                attempt += 1
                if attempt > 4:
                    raise TimeoutException("Can't open link")     
