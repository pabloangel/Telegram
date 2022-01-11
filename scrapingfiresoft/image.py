import telegram
import time




def telegram_bot_sendtext(bot_message): 
    bot_token = "1744522001:AAETJD0DJG9H_e2W082wggMmGJrsuYpOlfU"
    bot_chatID = "-540254493"
    send_text = 'https://api.telegram.org/bot'+ bot_token +'/sendMessage?chat_id='+ bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        
    response = requests.get(send_text)
    
    return response.json()

with open('photo.jpg', 'rb') as photo_file:
    telegram_bot_sendtext(photo_file)



    