# Librerías
from string import whitespace
import pandas as pd
import token
import requests
import tempfile
from os import remove
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
import pandas as pd
from datetime import date, datetime
from os import path


from urllib3.packages.six import u

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\equipo\\Desktop\\scrapingfiresoft\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

# Inicializamos el navegador
driver.get('http://despacho.uno/login')

user = "guestCBPA@exefire.com"
password = "iANtHORYdbUk"

#buscar campos a llenar
input_user = driver.find_element(By.XPATH, '//input[@name="email"]')
input_pass = driver.find_element(By.XPATH, '//input[@name="password"]')

input_user.send_keys(user)
input_pass.send_keys(password)

#buscar boton de login
boton = driver.find_element(By.XPATH, '//button[@type="submit"]')

#presionar  boton de login
boton.click()

#busqueda de activos en ctel
#ahora = driver.find_element(By.XPATH, '//a[@href="https://panel.firesoft.cl/cuarteles/ahora"]')
#ahora.click()
remove('airplane.png')
driver.save_screenshot("airplane.png")

files={'photo':open('airplane.png','rb')}

resp = requests.post('https://api.telegram.org/bot1744522001:AAETJD0DJG9H_e2W082wggMmGJrsuYpOlfU/sendPhoto?chat_id=-739081735', files=files)

print(resp.status_code)
print("Imagen enviada correctamente!")



driver.close()
driver.quit()
#revision de metodo que elimina la imagenes enviadar por telegram













