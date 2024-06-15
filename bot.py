from logic import DB_Manager
from config import *
from telebot import TeleBot

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Я бот хранящий в себе информацию о людях которые плыли на титанике!) 
""")
@bot.message_handler(commands=['info'])
def get_info(message):
    res = manager.get_information()
    bot.send_message(message.chat.id, res)
    
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.infinity_polling()