# Librerías
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
import pandas as pd

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
driver.get('https://panel.firesoft.cl/')

user = "cbpa9"
password = "d5g6h1"

#buscar campos a llenar
input_user = driver.find_element(By.XPATH, '//input[@name="user"]')
input_pass = driver.find_element(By.XPATH, '//input[@name="clave"]')

input_user.send_keys(user)
input_pass.send_keys(password)

#buscar boton de login
boton = driver.find_element(By.XPATH, '//button[@type="submit"]')

#presionar  boton de login
boton.click()

#busqueda de activos en ctel
ahora = driver.find_element(By.XPATH, '//a[@href="https://panel.firesoft.cl/cuarteles/ahora"]')
ahora.click()

#buscarvoluntarios
r=0

dataRows = driver.find_elements(By.CSS_SELECTOR, '.box-body .box-body > table tr ')

for dataRow in dataRows:
#    print(dataRow.text)
    
        
#telegram messagge

    def telegram_bot_sendtext(bot_message):
        
        bot_token = "1744522001:AAETJD0DJG9H_e2W082wggMmGJrsuYpOlfU"
        bot_chatID = "-588104867"
        send_text = 'https://api.telegram.org/bot'+ bot_token +'/sendMessage?chat_id='+ bot_chatID + '&parse_mode=Markdown&text=' + bot_message

        response = requests.get(send_text)
    
        return response.json()

for dataRow in dataRows:
    mensaje = telegram_bot_sendtext("\U0001F692" + "VOLUNTARIOS EN CUARTEL " + "\U0001F692")
    test = telegram_bot_sendtext(dataRow.text) 
    driver.close()



    
sys.exit()







   











