import requests as req
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

res = req.get(url="https://www.amazon.com/Fujifilm-X-T5-Mirrorless-Digital-Camera/dp/B0BK2MW5HV/ref=sr_1_3?keywords=fujifilm%2Bxt5&qid=1675437005&sprefix=fujifilm%2Bx%2Caps%2C160&sr=8-3&ufe=app_do%3Aamzn1.fos.4dd97f68-284f-40f5-a6f1-1e5b3de13370&th=1", headers=headers)

amazon_page = res.text

soup = BeautifulSoup(amazon_page, 'html.parser')

item_price = float(soup.select('span .a-offscreen')[0].getText().strip('$').replace(',', ''))

if item_price <= 1399.00:
    print(f'Item is below the target price point. Current price: ${item_price}')
else:
    print(f'Item is still above the target price point: ${item_price}')