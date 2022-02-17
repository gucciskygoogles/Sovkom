import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from make_data import DataFromTable
from make_data import File


def test_case(browser):
    p = DataFromTable()
    url = p.get_value(1)
    browser.get(f'http://{url}')
    input_field = browser.find_element(By.NAME, "text")
    input_field.click()
    input_field.send_keys(p.get_value(2))
    input_field.send_keys(Keys.RETURN)
    browser.find_element(By.LINK_TEXT, "Совкомбанк - кредиты наличными и карты рассрочки...").click()
    assert p.get_value(2) in browser.title
    browser.find_element(By.XPATH, f'//a[text()="{p.get_value(3)}"]').click()
    window = browser.window_handles[1]
    browser.switch_to.window(window)
    browser.find_element(By.XPATH, f'//span[text()="{p.get_value(4)}"]').click()
    credit_field = browser.find_element(By.XPATH, '//input[@inputmode="numeric"]')
    credit_field.click()
    price = browser.find_element(By.XPATH, '//*[@id="credit-sum"]/div[1]/input')
    price_value = int(price.get_attribute('value')[0:-2].replace(' ', ''))
    while price_value != int(p.get_value(5)):
        browser.find_element(By.XPATH, '//*[@id="credit-sum"]/div[1]/button[1]').click()
        price_value = int(price.get_attribute('value')[0:-2].replace(' ', ''))
    pay = browser.find_element(By.XPATH, '//*[@id="monthly-payment"]/span')
    pay_value = int(pay.text[0:-2])
    file = File()
    file.write_in_file(price_value, pay_value)
    while price_value < int(p.get_value(7)):
        needed_value = price_value + int(p.get_value(6))
        for i in range(0, len(str(price_value)) + 1):
            price.send_keys(Keys.BACKSPACE)
            time.sleep(0.1)
        price.send_keys(needed_value / 100)
        price_value = needed_value
        time.sleep(3)
        pay = browser.find_element(By.XPATH, '//*[@id="monthly-payment"]/span')
        pay_value = int(pay.text[0:-2].replace(' ', ''))
        file.write_in_file(price_value, pay_value)
    browser.save_screenshot("src/screen.png")
