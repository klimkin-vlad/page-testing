from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import random
import string
import pytest

@pytest.mark.login
class TestLoginFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title = "Best book created by robot")
        self.link = self.product.link
        yield
        self.product.delete()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        time.sleep(5)

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_login_link()

@pytest.mark.add_to_basket
class TestAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title="Best book created by robot")
        self.link = self.product.link
        yield
        self.product.delete()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_basket_form_and_title_at_empty_basket()
    
    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()
        time.sleep(10)
        
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_basket_link()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        time.sleep(10)
        
    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(browser):
        page = ProductPage(browser, self.link, 0)
        page.open()
        page.should_be_basket_link()
        page.add_to_basket()
        page.should_disappear_success_message()
        time.sleep(10)
    
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        page = ProductPage(browser, self.link, 0)
        page.open()
        page.should_be_basket_link()
        page.add_to_basket()
        page.should_not_be_success_message()
        time.sleep(10)

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        email = str(time.time()) + "@fakemail.org"
        symbols = string.punctuation
        password = random.choice(symbols, k = 8)
        login_page.register_new_user(email, password)
        
    def test_user_cant_see_product_in_basket_opened_from_product_page(browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        self.setup()
        page.should_be_basket_link()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_basket_form_and_title_at_empty_basket()
    
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        self.setup()
        page.should_not_be_success_message()
        time.sleep(10)
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        self.setup()
        page.should_be_basket_link()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        time.sleep(10)
        
    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(browser):
        page = ProductPage(browser, self.link, 0)
        page.open()
        age.go_to_login_page()
        self.setup()
        page.should_be_basket_link()
        page.add_to_basket()
        page.should_not_be_success_message()
        time.sleep(10)
