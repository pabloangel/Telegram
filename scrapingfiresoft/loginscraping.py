from selenium import webdriver
from bs4 import BeautifulSoup
import requests

# Start the session
session = requests.Session()
from bs4 import BeautifulSoup


# Create the payload
payload = {'user':'cbpa9', 
          'clave':'d5g6h1'
         }

# Post the payload to the site to log in
s = session.post("https://panel.firesoft.cl/", data=payload)
page = requests.get('https://panel.firesoft.cl/cuarteles/ahora')

s = BeautifulSoup(s.content, 'html.parser')
page = BeautifulSoup(page.content, 'html.parser')

print(s.prettify())

