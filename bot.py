import telebot;
import random
import time
from telebot import types
from telebot import datetime

token = 'Токен'

bot = telebot.TeleBot(token)

MALPASSWORD = 'abcdefghijklmnopqrstuvwxyz'
BOLPASSWORD = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERPASSWORD = '1234567890'
SIMVOLPASSWORD = '-_=+!&%$#@'


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnPasswordGenerator = types.KeyboardButton('Сгенерировать пароль')
    markup.add(btnPasswordGenerator)
    bot.send_message(message.chat.id,"Привет, я бот🤖, сейчас доступно только генерация пароля, в будущем будет больше", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    print('--------------------------------------------------------------------------')
    print('Дата и время: ', datetime.now())
    print('Имя: {0}'.format(message.from_user.first_name))
    print('Username: {0}'.format(str(message.from_user.username)))
    print('Chat Id: {0}'.format(str(message.chat.id)))
    print('Сообщение: {0}'.format(message.text))
    if message.text == 'Сгенерировать пароль':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnBack = types.KeyboardButton('Назад в начальное меню')
        markup.add(btnBack)
        bot.send_message(message.chat.id,"Введите кол-во символов в пароле (Максимум 72 символа, минимум 6)", reply_markup=markup)
    elif message.text == 'Назад в начальное меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btnPasswordGenerator = types.KeyboardButton('Сгенерировать пароль')
            markup.add(btnPasswordGenerator)
            bot.send_message(message.chat.id,'Мы вернулись в начальное меню', reply_markup=markup)
    elif message.text.isdigit():
        number = int(message.text)
        if number <= 5:
            bot.send_message(message.chat.id,'Введите число больше 5')
        elif number > 72:
            bot.send_message(message.chat.id,'Введите число меньше 72')
        else:
            allPassword = MALPASSWORD + BOLPASSWORD + NUMBERPASSWORD + SIMVOLPASSWORD
            length = number
            password = ''.join(random.sample(allPassword, length))
            bot.send_message(message.chat.id,'Идет генерация пароля...')
            time.sleep(3)
            bot.send_message(message.chat.id,password)
            print('--------------------------------------------------------------------------')
            print('Дата и время: ', datetime.now())
            print('Имя: {0}'.format(message.from_user.first_name))
            print('Username: {0}'.format(str(message.from_user.username)))
            print('Пароль: ',password)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btnPasswordGenerator = types.KeyboardButton('Сгенерировать пароль')
            markup.add(btnPasswordGenerator)
            bot.send_message(message.chat.id,'Мы вернулись в начальное меню', reply_markup=markup)
        


bot.infinity_polling()


