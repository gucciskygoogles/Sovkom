from pages.base_page import BasePage
from pages.locators import CreditCashPageLocators
from make_data import DataFromTable
from make_data import File
from selenium.webdriver.common.keys import Keys
import time

class CreditCashPage(BasePage):

    def make_credit_lower_and_add_to_file(self):
        p = DataFromTable()
        file = File()
        credit_input = self.browser.find_element(*CreditCashPageLocators.CREDIT_INPUT)
        credit_input.click()
        price = self.browser.find_element(*CreditCashPageLocators.PRICE)
        price_value = int(price.get_attribute('value')[0:-2].replace(' ', ''))
        while price_value != int(p.get_value(5)):
            self.browser.find_element(*CreditCashPageLocators.MINIMALIZE_SUM).click()
            price_value = int(price.get_attribute('value')[0:-2].replace(' ', ''))
        pay = self.browser.find_element(*CreditCashPageLocators.PAY)
        pay_value = int(pay.text[0:-2])
        file.write_in_file(price_value, pay_value)

    def up_credit_and_add_to_file(self):
        p = DataFromTable()
        file = File()
        price = self.browser.find_element(*CreditCashPageLocators.PRICE)
        price_value = int(price.get_attribute('value')[0:-2].replace(' ', ''))

        while price_value < int(p.get_value(7)):
            needed_value = price_value + int(p.get_value(6))
            for i in range(0, len(str(price_value)) + 1):
                price.send_keys(Keys.BACKSPACE)
                time.sleep(0.1)
            price.send_keys(needed_value / 100)
            price_value = needed_value
            time.sleep(2)
            pay = self.browser.find_element(*CreditCashPageLocators.PAY)
            pay_value = int(pay.text[0:-2].replace(' ', ''))
            file.write_in_file(price_value, pay_value)
        self.browser.save_screenshot("src/screen.png")


