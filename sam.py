import telepot
from config import BOT_TOKEN, TELEGRAM_CHAT_ID
bot=telepot.Bot(BOT_TOKEN)
bot.sendMessage(TELEGRAM_CHAT_ID,str("hello"))
bot.sendPhoto(TELEGRAM_CHAT_ID,photo=open("msg.jpg",'rb'))