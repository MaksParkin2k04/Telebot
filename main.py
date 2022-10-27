import telebot
from telebot import types


bot = telebot.TeleBot('5785712093:AAFGxGzmd9cMEb6cV-xXblcw_6PsKaZ_qHo')

@bot.message_handler(commands = ['start'])
def start(message):
    mess = f'Привет , <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

# # @bot.message_handler()
# # def get_user_text(message):
# #     if message.text == "Hello":
# #         bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
# #     elif message.text == "id":
# #         bot.send_message(message.chat.id, f"Твой ID:{message.from_user.id} ", parse_mode='html')
# #     elif message.text == "photo":
# #         photo = open('1614256626_python_logo.jpg', 'rb')
# #         bot.send_photo(message.chat.id, photo)
#
#     else:
#         bot.send_message(message.chat.id, "Я тебя не понимаю(" , parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Вау! Крутое фото!", parse_mode='html')


@bot.message_handler(commands = ['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://www.youtube.com/watch?v=HodO2eBEz_8&t=1866s"))
    bot.send_message(message.chat.id, "Перейдите на сайт", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands = ['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('web')
    start = types.KeyboardButton('start')

    markup.add(website, start)
    bot.send_message(message.chat.id, "Перейдите на сайт", parse_mode='html', reply_markup=markup)
















bot.polling(none_stop = True)

