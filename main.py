import datetime


import telebot

from config import TOKEN
from db import get_notes_from_db, createdb, save_data, delete_data

bot = telebot.TeleBot(TOKEN)

def get_welcome() -> str:
    current_time = datetime.datetime.now()
    if 0<= current_time.hour <6:
        return 'Доброй ночи!'
    if 6<= current_time.hour <12:
        return 'Доброе утро!'
    if 12<= current_time.hour <18:
        return 'Добрый день!'
    else:
        return 'Добрый вечер!'

@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = f'{get_welcome()} Я бот для твоих заметок)\n\n'\
           f'Список команд:\n'\
           f'/get_all - получить все имеющиеся заметки\n'\
           f'/add_note - добавить заметку \n'\
           f'/delete_note - удалить заметку'

    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['get_all'])
def get_all(message: telebot.types.Message):
    bot.send_message(message.chat.id,get_notes_from_db())






@bot.message_handler(commands=['add_note'])
def add_note(message: telebot.types.Message):
    text=f'Чтобы добавить заметку, напишите через значок "_" номер и текст заметки'
    bot.send_message(message.chat.id, text)



@bot.message_handler(commands=['delete_note'])
def delete_note(message: telebot.types.Message):
    text = f'Чтобы удалить заметку, напишите значок "!" и номер заметки'
    bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda message: message.text.startswith('!'))
def minus_note(message: telebot.types.Message):
    minus_text=message.text
    numb=minus_text[1]
    delete_data(number=int(numb), )
    bot.send_message(message.chat.id, 'Номер заметки и её содержание были успешно удалены')


@bot.message_handler()
def plus_note(message: telebot.types.Message):
    plus_text=message.text.split('_')
    if len(plus_text)==1:
        bot.send_message(message.chat.id, 'Не было значка "_" или "!", если вы хотели добавить заметку или удалить её ')
    elif len(plus_text)==2:
        number = plus_text[0]
        content = plus_text[1]
        bot.send_message(message.chat.id, 'Номер заметки и её содержание были успешно добавлены')
        save_data(number=int(number), content=content)
    else:
        bot.send_message(message.chat.id, 'Слишком много "_"')



if __name__=='__main__':
    createdb()
    print ('Бот запущен')
    bot.infinity_polling()
