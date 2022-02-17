from pages.browser_page import BrowserPage
from make_data import DataFromTable


class TestCase:

    def test(self, browser, url):
        p = DataFromTable()
        browser.get(f'http://{url}')
        page = BrowserPage(browser, url)
        main_page = page.going_to_site()
        assert p.get_value(2) in browser.title
        credit_page = main_page.going_to_credit_page()
        window = browser.window_handles[1]
        browser.switch_to.window(window)
        credit_cash_page = credit_page.going_to_credit_cash_page()
        credit_cash_page.make_credit_lower_and_add_to_file()
        credit_cash_page.up_credit_and_add_to_file()

