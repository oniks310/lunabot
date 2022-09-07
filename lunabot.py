import telebot
from telebot import types
from datetime import datetime
import parser
import os

TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    #sti = open('static/AnimatedSticker.tgs', 'rb')
    #bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Добро пожаловать, в лунный бот! \
    Здесь ты можешь получить информацию о лунных сутках и холостой луне \
    ".format(message.from_user, bot.get_me()))
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Лунные сутки сегодня')
    item2 = types.KeyboardButton('Лунные сутки на месяц')

    markup.add(item1, item2)
    
    bot.send_message(message.chat.id,'Выберите интерисующую информацию', reply_markup=markup)


# @bot.message_handler(commands=['Лунные сутки сегодня'])
# def message_reply(message):

#     if message.text == "Лунные сутки сегодня":
#         bot.send_message(message.chat.id, str(random.randint(1, 100)))  
#     elif message.text == "Как дела?":
#         markup = types.InlineKeyboardMarkup(row_width=2)
#         item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
#         item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
#         markup.add(item1, item2)
        
#         bot.send_message(message.chat.id, "Отлично, сам как?", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, "Я не знаю такой команды")


@bot.message_handler(content_types='text')
def message_reply(message):
    
    if message.text=="Лунные сутки сегодня":
        bot.send_message(message.chat.id," Сегодня " + parser.today + "\n" + parser.info)
    elif message.text=="Лунные сутки на месяц":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Январь 2022')
        item2 = types.KeyboardButton('Ферваль 2022')
        item3 = types.KeyboardButton('Март 2022')
        item4 = types.KeyboardButton('Апрель 2022')
        item5 = types.KeyboardButton('Май 2022')
        item6 = types.KeyboardButton('Июнь 2022')
        item7 = types.KeyboardButton('Июль 2022')
        item8 = types.KeyboardButton('Август 2022')
        item9 = types.KeyboardButton('Сентябрь 2022')
        item10 = types.KeyboardButton('Октябрь 2022')
        item11 = types.KeyboardButton('Ноябрь 2022')
        item12 = types.KeyboardButton('Декабрь 2022')
        back = types.KeyboardButton('Назад')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, \
            item9, item10, item11, item12, back)
        bot.send_message(message.chat.id,"Выберите месяц", reply_markup=markup)
    
    elif message.text =='Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Лунные сутки сегодня')
        item2 = types.KeyboardButton('Лунные сутки на месяц')

        markup.add(item1, item2)
        
        bot.send_message(message.chat.id,'Выберите интерисующую информацию', reply_markup=markup)


bot.polling(none_stop=True)
