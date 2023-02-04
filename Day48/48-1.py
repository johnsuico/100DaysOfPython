from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r'C:\Users\JohnC\Projects\ChromeDriver\chromedriver.exe'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

AMAZON_URL = 'https://www.amazon.com/Fujifilm-X-T5-Mirrorless-Digital-Camera/dp/B0BK2MW5HV/ref=sr_1_3?keywords=fujifilm%2Bxt5&qid=1675437005&sprefix=fujifilm%2Bx%2Caps%2C160&sr=8-3&ufe=app_do%3Aamzn1.fos.4dd97f68-284f-40f5-a6f1-1e5b3de13370&th=1'

driver.get(AMAZON_URL)

price_whole_element = driver.find_element(By.CLASS_NAME, 'a-price-whole')
price_decimal_element = driver.find_element(By.CLASS_NAME, 'a-price-fraction')

price_whole = price_whole_element.text.replace(',', '')
price_decimal = price_decimal_element.text
price = float(price_whole + '.' + price_decimal)

print(price)

driver.quit()