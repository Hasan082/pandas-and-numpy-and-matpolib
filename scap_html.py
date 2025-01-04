import requests
from bs4 import BeautifulSoup
import html5lib

html = ("<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> "
        "Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> "
        "Salary: $73,200, 000</p></body></html>")

soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())
print(soup.title.string)
for h3 in soup.find_all('h3'):
    print(h3.string.strip())

table_data = ("<table><tr><td id='flight' >Flight No</td><td>Launch site</td><td>Payload "
              "mass</td></tr><tr><td>1</td><td><a "
              "href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td><td>300 kg</td></tr><tr><td>2</td><td><a "
              "href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a "
              "href='https://en.wikipedia.org/wiki/Florida'>Florida</a> </td><td>80 kg</td></tr></table>")


soup2 = BeautifulSoup(table_data, 'html.parser')

for i, row in enumerate(soup2.find_all('tr')):
    for j, cell in enumerate(row):
        if cell.string:
            print(cell.string.strip())


# Scarp all Image===========

url = "https://web.archive.org/web/20230224123642/https://www.ibm.com/us-en/"
data  = requests.get(url).text
soup3 = BeautifulSoup(data, 'html.parser')

for img in soup3.find_all('img'):
    print(img.get('src'))


