import requests

url = f'https://breaking-bad-quotes.herokuapp.com/v1/quotes/50' 

r = requests.get(url)

with open('BB.txt', 'a') as file:
   file.write(r.text)