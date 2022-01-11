import time
import requests


def telegram_bot_sendtext(bot_message):
    
    bot_token = '1744522001:AAETJD0DJG9H_e2W082wggMmGJrsuYpOlfU'
    bot_chatID = '1115320056'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    test = telegram_bot_sendtext("Hola!!")
    print(test)

