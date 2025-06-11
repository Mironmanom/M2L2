import telebot
import os
import random
advs = ['меньше проводите времени в душе!','пользуйтесь велосипедом или ходите пешком!','выключайте свет!','пользуйтесь многоразовыми сумками!']
facts = ['одна пальчиковая батарейка может загрязнить 400 литров воды или 20 квадратных метров земли!',
         '80% тропических лесов уже уничтожены из-за деятельности человека!',
         'каждый год исчезает 13 миллионов гектаров леса!',
         'за последние 50 лет растаяло 40% ледников мира!',
         'в океан ежегодно попадает 8 миллионов тонн пластика!',
         'только 3% мировых запасов пресной воды пригодны для использования человеком!',
         'пчёлы – одни из самых важных опылителей, обеспечивающих нам еду и биологическое разнообразие!'
]
bot = telebot.TeleBot("Token")    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой экобот (/help если нужна помощь с командами))")


@bot.message_handler(commands=['mem'])
def send_mem(message):
    images = os.listdir('images')
    mem = random.choice(images)
    with open(f'images/{mem}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)


@bot.message_handler(commands=['adv'])
def send_adv(message):
    adv = random.choice(advs)
    bot.reply_to(message,f'{adv} /help - для поиска команд')

@bot.message_handler(commands=['fact'])
def send_fact(message):
    fact = random.choice(facts)
    r_number = random.randint(1,3)
    number = ''
    if r_number == 1:
        number = 'А ты знал что, '
    elif r_number == 2:
        number = 'Оказывается '
    elif r_number == 3:  
        number = 'Интересный факт: '
    bot.reply_to(message,f'{number}{fact} /help - для поиска команд')

@bot.message_handler(commands=['help'])
def send_commands(message):
    bot.reply_to(message,'/adv - даёт совет,/mem - случайный мем.,/fact - случайный факт про экологию')

bot.polling()
