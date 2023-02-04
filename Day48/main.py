from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = r'C:\Users\JohnC\Projects\ChromeDriver\chromedriver.exe'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie_element = driver.find_element(By.CSS_SELECTOR, '#cookie')

items = driver.find_elements(By.CSS_SELECTOR, '#store div')
item_ids = [item.get_attribute('id') for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie_element.click()

    if time.time() > timeout:

        all_prices = driver.find_elements(By.CSS_SELECTOR, '#store b')
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != '':
                cost = int(element_text.split('-')[1].strip().replace(',', ''))
                item_prices.append(cost)

        cookie_upgrades = {}
        for i in range(len(item_prices)):
            cookie_upgrades[item_prices[i]] = item_ids[i]

        money_element = driver.find_element(By.ID, 'money').text
        if ',' in money_element:
            money_element = money_element.replace(',', '')
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, 'cps').text
        print(cookie_per_s)
        break

driver.quit()