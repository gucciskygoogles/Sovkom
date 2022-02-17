from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.credit_page import CreditPage


class MainPage(BasePage):

    def going_to_credit_page(self):
        credit_btn = self.browser.find_element(*MainPageLocators.CREDIT_BTN)
        credit_btn.click()
        return CreditPage(browser=self.browser, url=self.url)

