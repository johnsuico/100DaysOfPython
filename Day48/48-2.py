from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r'C:\Users\JohnC\Projects\ChromeDriver\chromedriver.exe'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.python.org')

event_dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_titles = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
events = {}

for i in range(len(event_dates)):
    events[i] = {
        'date': event_dates[i].text,
        'title': event_titles[i].text
    }

print(events)

driver.quit()