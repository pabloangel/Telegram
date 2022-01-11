
import requests

page = requests.get('https://panel.firesoft.cl/cuarteles/ahora')
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')


print(soup.prettify())

