from bs4 import BeautifulSoup as bs
import requests
import re

url = 'https://www.digikala.com/landing-page/?category%5B0%5D=5966&promotion_types%5B0%5D=incredible_offer&promotion_types%5B1%5D=promotion&promotion_times%5B0%5D=active'

r = requests.get(url)
soup = bs(r.text, 'html.parser')

val = soup.find_all('div', attrs = {"class" : "c-price__value-wrapper"})
name = soup.find_all('div', attrs = {"class" : "c-product-box__title"})
percent = soup.find_all('div', attrs = {"class" : "c-price__discount-oval"})

Price = []
for v in val:
    vv = re.findall(r'\d+,?\d+,?\d*', v.text.strip())
    sub_vv = re.sub(',', '', vv[0])
    Price.append(int(sub_vv))

percents = []
for p in percent:
    pp = re.findall(r'\d+', p.text.strip())
    sub_pp = re.sub(',', '', pp[0])
    percents.append(int(sub_pp))

for n, p, v in zip(name, percents, Price):
    if p > 30:
        print(n.text.strip())
        print(f"Percents: {p}%")
        print(f"Price: {v} Toman")
        print('-'*40)

# this page of digikala doesn't have a english title so I supposed to use persian title.