import telegram
import time
bot_token = '1744522001:AAETJD0DJG9H_e2W082wggMmGJrsuYpOlfU'
chat_id = '540254493'

bot = telegram.Bot(token=bot_token)
with open('photo.jpg', 'rb') as photo_file:
    bot.sendPhoto(chat_id=chat_id, photo=photo_file, caption='Envio de imagen')