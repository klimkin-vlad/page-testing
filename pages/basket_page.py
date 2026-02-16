from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_basket_form_and_title_at_empty_basket():
        assert not self.is_element_present(*BasketPageLocators.BASKET_FORM), "Basket form is presented, but should not be"
        assert not self.is_element_present(*BasketPageLocators.BASKET_TITLE), "Basket title is presented, but should not be"
