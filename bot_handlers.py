from bot import bot
from messages import*
from db import users_db
from telebot import types
from url import*


key = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
button_1 = types.KeyboardButton("Математичний аналіз")
button_2 = types.KeyboardButton("Лінійна алгебра та аналітична геометрія")
key.add(button_1,button_2)


@bot.message_handler(commands=['start','math']) 
def send_welcome1(message):
    bot.reply_to(message, HELLO_MESSAGE, reply_markup=key)


@bot.message_handler(commands=['start','math']) #Not ready now
def send_welcome(message):
    if not users_db.find_one({ "chat_id" : message.chat.id}):
        users_db.insert_one({ "chat_id" : message.chat.id})
        bot.reply_to(message, HELLO_MESSAGE, reply_markup=key)
    else:
        bot.reply_to(message, HELLO_AGAIN_MESSAGE, reply_markup=key)
    bot.reply_to(message, HELLO_MESSAGE, reply_markup=key)
    pass


@bot.message_handler(func=lambda callback:True)
def reply(message):
    if message.text == "Математичний аналіз":
        key = types.InlineKeyboardMarkup( row_width = 1)
        Mbutton_1 = types.InlineKeyboardButton(text = "Обчислення ліміту функції", url = MA_URL_1)
        Mbutton_2 = types.InlineKeyboardButton(text = "Обчислити суму арифметичної прогресії", url = MA_URL_2)
        Mbutton_3 = types.InlineKeyboardButton(text = "Знайти похідну функції", url = MA_URL_3)
        key.add(Mbutton_1,Mbutton_2,Mbutton_3)
        bot.send_message(message.chat.id, "Оберіть функцію", reply_markup=key)
    elif message.text == "Лінійна алгебра та аналітична геометрія":
        key = types.InlineKeyboardMarkup( row_width = 1)
        Lbutton_1 = types.InlineKeyboardButton(text = "Знайти обернену матрицю", url = LA_URL_1)
        Lbutton_2 = types.InlineKeyboardButton(text = "Обчислити визначник матриці", url = LA_URL_2)
        Lbutton_3 = types.InlineKeyboardButton(text = "Обчислити векторний добуток веткорів", url = LA_URL_3)
        Lbutton_4 = types.InlineKeyboardButton(text = "Знайти відстань від точки до прямої", url = LA_URL_4)
        Lbutton_5 = types.InlineKeyboardButton(text = "Знайти добуток матриць", url = LA_URL_5)
        Lbutton_6 = types.InlineKeyboardButton(text = "Розкласти вектор за базисом", url = LA_URL_6)
        key.add(Lbutton_1,Lbutton_2,Lbutton_3,Lbutton_4,Lbutton_5,Lbutton_6)
        bot.send_message(message.chat.id, "Оберіть функцію", reply_markup=key)
       

if __name__ == '__main__':
    bot.polling(none_stop=True)

