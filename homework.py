import requests
from bs4 import BeautifulSoup

url = 'https://www.groupon.com/browse/salt-lake-city?lat=40.234&lng=-111.659&locality=Provo&administrative_area=UT&query=escape+room&address=Provo%2C+UT&division=salt-lake-city&locale=en_US'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537/6',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'origin': url,
    'referer': url
}
page = requests.get(url, headers=HEADERS)

soup = BeautifulSoup(page.content, 'html.parser')

deals = soup.find_all('div', class_='cui-content')

for deal in deals:
  title = deal.find('div', class_='cui-udc-title')
  if title:
    title = title.text.strip()

  location = deal.find('span', class_='cui-location-name')
  if location:
    location = location.text.strip()
  else:
    continue
  
  original_price = deal.find(class_='cui-price-original')
  if original_price:
    original_price = original_price.text.strip()
  else:
    continue
  
  discount_price = deal.find(class_='cui-price-discount')
  if discount_price:
    discount_price = discount_price.text.strip()
  else:
    continue
  
  star_raitings = deal.find(class_='numeric-count')
  if star_raitings:
    star_raitings = star_raitings.text.strip()
  else:
    continue
  
  print(f'{title}\n  {location}\n  Original Price: {original_price}\n  Discounted Price: {discount_price}\n  {star_raitings} Star Rating\n')