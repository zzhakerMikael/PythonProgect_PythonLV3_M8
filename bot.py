import telebot
from telebot import types
import sqlite3
import logging
from config import *

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Инициализация бота
token = TOKEN  # Замените на ваш токен
bot = telebot.TeleBot(token)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(
        message,
        "Привет! Я твой бот. Как я могу помочь тебе сегодня?"
    )
    bot.reply_to(
        message,
        "Доступные команды:\n"
        "/start - начать работу с ботом\n"
        "/help - показать это сообщение\n"
        "/about - узнать информацию о боте"
        "/start_test - Узнать к какой професии ты больше подходишь подходишь (Тэст)!"
    )

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "Доступные команды:\n"
        "/start - начать работу с ботом\n"
        "/help - показать это сообщение\n"
        "/about - узнать информацию о боте"
        "/start_test - Узнать к какой професии ты больше подходишь подходишь (Тэст)!"
    )
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['start_test'])
def test_command(message):
    connection = sqlite3.connect('my_database.db')
    cur = connection.cursor()
    stage = 1
    if stage == 1:
        






#if __name__ == '__main__':
#    try:
#        logging.info("Бот запущен")
#        bot.infinity_polling(skip_pending=True)
#    except Exception as e:
#        logging.error(f"Произошла ошибка: {str(e)}")

bot.polling(none_stop=True, interval=0)













































