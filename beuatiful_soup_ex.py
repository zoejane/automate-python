import bs4
import requests

res=requests.get('http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems =soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span7.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')

print(elems[0].text.strip())
