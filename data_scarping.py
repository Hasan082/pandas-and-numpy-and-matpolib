import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/IBM'

response = requests.get(url)

html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

links = soup.find_all('a')

for link in links:
    print(link.get('href'))




