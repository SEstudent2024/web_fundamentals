import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.codingtemple.com')

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.title.text)