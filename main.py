import telebot
from telebot import types

bot = telebot.TeleBot('5785712093:AAFGxGzmd9cMEb6cV-xXblcw_6PsKaZ_qHo')
age = 0;

@bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    mess_hello = f'Привет, <u><b>{user_name}</b></u>. Я умный бот по математике и  могу помочь решить тебе задачки'
    bot.send_message(message.chat.id, mess_hello, parse_mode='html')

    # mess_instruction = 'Если ты хочешь решить задачу, введи команду /zadan'
    # bot.send_message(message.chat.id, mess_instruction)
    mess_instruction = 'Если ты хочешь решить задачу, введи команду /1'
    bot.send_message(message.chat.id, mess_instruction)
    if message.text == "1":
        bot.send_message(message.chat.id, mess_hello, parse_mode='html')



@bot.message_handler(commands=['1'])
def num_1(message):
    mess = 'Квадратное уравнение'
    bot.send_message(message.chat.id, "Введите коэффы")
    bot.send_message(message.chat.id, "а = ")
    message.number = input()
    bot.send_message(message.chat.id, message.number)

# @bot.message_handler(commands = ['zadan'])
# def button(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("1", url="https://www.youtube.com/watch?v=HodO2eBEz_8"))
#     bot.send_message(message.chat.id, 'Выберите задачу', reply_markup= markup)


bot.polling(none_stop=True)
