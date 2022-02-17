from pages.base_page import BasePage
from pages.locators import CreditPageLocators
from pages.credit_cash_page import CreditCashPage

class CreditPage(BasePage):

    def going_to_credit_cash_page(self):
        credit_cash_btn = self.browser.find_element(*CreditPageLocators.CREDIT_CASH_BTN)
        credit_cash_btn.click()
        return CreditCashPage(browser=self.browser, url=self.url)


