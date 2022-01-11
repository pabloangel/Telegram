import requests 

files={'photo':open('D:\\airplane.png','rb')}

resp = requests.post('https://api.telegram.org/bot1744522001:AAETJD0DJG9H_e2W082wggMmGJrsuYpOlfU/sendPhoto?chat_id=-540254493', files=files)

print(resp.status_code)