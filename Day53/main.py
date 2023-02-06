from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r'C:\Users\JohnC\Projects\ChromeDriver\chromedriver.exe'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

ZILLOW_URL = 'https://www.zillow.com/san-jose-ca-95138/rentals/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A37.35146168514399%2C%22east%22%3A-121.57184824487305%2C%22south%22%3A37.14567395575032%2C%22west%22%3A-121.87980875512696%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A98006%2C%22regionType%22%3A7%7D%5D%2C%22pagination%22%3A%7B%7D%7D'

driver.get(ZILLOW_URL)

prices_of_places = driver.find_elements(By.CSS_SELECTOR, 'li div span')

print(prices_of_places)

driver.quit()