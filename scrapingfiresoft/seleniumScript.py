# Librerías
from string import whitespace
import pandas as pd
import token
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
import pandas as pd
from datetime import date, datetime

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

#prueba de funciones varias
dataRows = driver.find_elements(By.CSS_SELECTOR, '.box-body .box-body > table tr ')
columnas = driver.find_elements(By.CSS_SELECTOR, '.box-body > table td ')
cuarteles = columnas[0]
disponibles = columnas[1]

#image = driver.get_screenshot_as_file("C:\\Users\\equipo\\Desktop\\scrapingfiresoft\\screen\\image.png")

for dataRow in dataRows:
    print("\n" + dataRow.text  + "\n" + "\n")
          
    
        
#telegram messagge

    def telegram_bot_sendtext(bot_message):
        
        bot_token = "1744522001:AAETJD0DJG9H_e2W082wggMmGJrsuYpOlfU"
        bot_chatID = "-540254493"
        send_text = 'https://api.telegram.org/bot'+ bot_token +'/sendMessage?chat_id='+ bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        
        response = requests.get(send_text)
    
        return response.json()

#funcion para sacar screen
    def screenshot(d):
        folder = "C:\\Users\\equipo\\Desktop\\scrapingfiresoft\\screen\\"
        time_string = time.asctime().replace(":", " ")      
        file_name = folder + time_string +".png"
        d.save_screenshot(file_name)
        d.get_screenshot_as_file(file_name)
        files ={'photo':open("C:\\Users\\equipo\\Desktop\\scrapingfiresoft\\screen\\" + file_name )}
        resp = requests.post('https://api.telegram.org/bot1744522001:AAETJD0DJG9H_e2W082wggMmGJrsuYpOlfU/sendPhoto?chat_id=-540254493', files=file_name)
        print(resp.status_code)


#funcion para enviar foto

    #files={'photo' :open('C:\Users\equipo\Desktop\scrapingfiresoft\screen')}
        

#ejecuta el screen
    imagen = screenshot(driver)

    #Día actual
    today = date.today()
    #Fecha actual
    now = datetime.now()

  
for dataRow in dataRows:
    mensaje = telegram_bot_sendtext("\U0001F692" + "Voluntarios en " + cuarteles.text + "\U0001F692")
    msj  = telegram_bot_sendtext("Cantidad en cuartel: " + disponibles.text)
    test = telegram_bot_sendtext(dataRow.text + "\n" + " " + "\n")
    format = telegram_bot_sendtext("Fin comentario - " + now.strftime('%d/%m/%Y') +"\n"+ "Proxima actualizacion dentro de 30 minutos más")
    print(cuarteles.text)
    print(disponibles.text)
    
    

    format = now.strftime('Día :%d/%m/%Y, Hora: %H, Minutos: %M, Segundos: %S')
    print(format)
    driver.close()
    driver.quit()





    









   











