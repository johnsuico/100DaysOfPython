from bs4 import BeautifulSoup, os

dirname = os.path.dirname(__file__)
website_path = os.path.join(dirname, './website.html')

with open(website_path, encoding='utf-8') as file:
    contents = file.read()

# Ex 45-1
soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)

# Ex 45-2
# Find multiple elements
all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get('href'))
    pass

heading = soup.find(name='h1', id='name')
# print(heading)

section_heading = soup.find(name='h3', class_='heading')
# print(section_heading)

company_url = soup.select_one(selector='p a')
print(company_url)