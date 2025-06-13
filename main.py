import telebot
import os
from dotenv import find_dotenv, load_dotenv

if find_dotenv('.env'):
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


# Простая логика обработки текста
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text.lower()

    if 'привет' in text:
        bot.reply_to(message, "Привет!")
    elif 'пока' in text:
        bot.reply_to(message, "Пока!")
    else:
        bot.reply_to(message, "Я тебя не понял. Напиши 'привет' или 'пока'.")

if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()
