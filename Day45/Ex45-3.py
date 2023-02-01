from bs4 import BeautifulSoup
import requests as req

res = req.get('https://news.ycombinator.com/')

yc_web_page = res.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.select('.titleline a')
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

article_scores = [int(score.getText().split()[0]) for score in soup.find_all(class_='score')]
max_value = max(article_scores)
max_value_index = article_scores.index(max_value)
# print(max_value_index)

# print(article_texts)
# print(article_links)
# print(article_scores)

# Print the highest score article
print(article_texts[max_value_index])
print(article_links[max_value_index])
print(article_scores[max_value_index])