from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r'C:\Users\JohnC\Projects\ChromeDriver\chromedriver.exe'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

article_count = int(driver.find_element(By.CSS_SELECTOR, '#articlecount a').text.replace(',', ''))

print(article_count)

driver.quit()