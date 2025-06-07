import telebot
import os
import random
advs = ['меньше проводите времени в душе','пользуйтесь велосипедом или ходите пешком','выключайте свет','пользуйтесь многоразовыми сумками']
bot = telebot.TeleBot("7704115421:AAHykbkd5vqZPMuRj5w-9WJX26g0UZIhGJw")    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой экобот (/help если нужна помощь с командами)")


@bot.message_handler(commands=['mem'])
def send_mem(message):
    images = os.listdir('images')
    mem = random.choice(images)
    with open(f'images/{mem}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)


@bot.message_handler(commands=['adv'])
def send_adv(message):
    adv = random.choice(advs)
    bot.reply_to(message,adv)


@bot.message_handler(commands=['help'])
def send_commands(message):
    bot.reply_to(message,'/adv - даёт совет,/mem - случайный мем.')

bot.polling()