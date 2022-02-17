from make_data import DataFromTable
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.main_page_sov import MainPage


class BrowserPage(BasePage):

    def going_to_site(self):
        p = DataFromTable()
        input_field = self.browser.find_element(By.NAME, "text")
        input_field.click()
        input_field.send_keys(p.get_value(2))
        input_field.send_keys(Keys.RETURN)
        self.browser.find_element(By.LINK_TEXT, "Совкомбанк - кредиты наличными и карты рассрочки...").click()
        return MainPage(browser=self.browser, url=self.url)