from config import *
import telebot


bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=["empesar","ayuda","help"])

def cmd_start(message):
    bot.reply_to(message,"¿Hola como estas?, que tal te esta yendo")
    
    
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id,"el comando no existe")
    else:
        bot.send_message(message.chat.id, " ¿Hola como estas?, que tal te esta yendo, si Tienes alguna consulta estos son los comandos que puedes usar   /empesar  /ayuda  /quien_soy") 
      
    if message.text.startswith("/quien_soy"):
         
        foto=open("./images/yo.png","rb")
        bot.send_photo(message.chat.id,foto, "¡ SOY FULL STACK DEVELOOPER !")
        
    
    
    
if __name__ == '__main__':
    print("el bot se ha iniciado")
    bot.infinity_polling()
    print('fin')   
    
