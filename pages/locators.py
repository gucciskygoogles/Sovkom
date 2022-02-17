from selenium.webdriver.common.by import By
from make_data import DataFromTable

class MainPageLocators:

    p = DataFromTable()
    CREDIT_BTN = (By.XPATH, f'//a[text()="{p.get_value(3)}"]')

class CreditPageLocators:

    p = DataFromTable()
    CREDIT_CASH_BTN = (By.XPATH, f'//span[text()="{p.get_value(4)}"]')

class CreditCashPageLocators:

    CREDIT_INPUT = (By.XPATH, '//input[@inputmode="numeric"]')
    PRICE = (By.XPATH, '//*[@id="credit-sum"]/div[1]/input')
    PAY = (By.XPATH, '//*[@id="monthly-payment"]/span')
    MINIMALIZE_SUM = (By.XPATH, '//*[@id="credit-sum"]/div[1]/button[1]')