from selenium.webdriver.common.keys import Keys
from make_data import DataFromTable
from selenium.webdriver.common.by import By
from pages.main_page_sov import MainPage

class TestCase:

    def test_scen(self, browser, url):
        p = DataFromTable()
        browser.get(f'http://{url}')
        input_field = browser.find_element(By.NAME, "text")
        input_field.click()
        input_field.send_keys(p.get_value(2))
        input_field.send_keys(Keys.RETURN)
        browser.find_element(By.LINK_TEXT, "Совкомбанк - кредиты наличными и карты рассрочки...").click()
        assert p.get_value(2) in browser.title
        page = MainPage(browser, url)
        credit_page = page.going_to_credit_page()
        window = browser.window_handles[1]
        browser.switch_to.window(window)
        credit_cash_page = credit_page.going_to_credit_cash_page()
        credit_cash_page.make_credit_lower_and_add_to_file()
        credit_cash_page.up_credit_and_add_to_file()