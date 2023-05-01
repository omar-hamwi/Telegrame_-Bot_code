
import telebot 
from decouple import config



# to create the bot 
BOT_TOKEN=config('BOT_TOKEN')
bot =telebot.TeleBot(BOT_TOKEN)


greeting=["hello","hi","welcome"]
asking_question=["course", "game","photo"]
target=["python","java","c++"]


@bot.message_handler(commands=['start','help'])
def content(message):
        bot.send_message( message.chat.id,("We have various classes and lesson to be good"))


def isMsg(message):
    return True

@bot.message_handler(func=isMsg)
def replay(message):
    words= message.text.split()



    if words[0].lower() in greeting:
        bot.reply_to(message,"hey how is going!")
    elif words[0].lower() in asking_question :
        bot.reply_to(message,"thanks for you ")


bot.polling()

