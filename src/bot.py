from telebot import TeleBot, types

import settings, messages, logging, db, markups, handler

bot = TeleBot(token=settings.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message:types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.MESSAGE_HELLO,
        reply_markup=markups.get_empty_markup()
    )
    logging.info(f'Пользователь {message.from_user.username} использовал команду /start')
    
    db.insert_user(message.from_user.username, message.from_user.id)
    

@bot.message_handler(commands=['menu'])
def menu_message(message:types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.MESSAGE_MENU,
        reply_markup=markups.get_menu_markup()
    )
    
    logging.info(f'Пользователь {message.from_user.username} использовал команду /menu')
    bot.register_next_step_handler(message, subject_choice)


def subject_choice(message:types.Message):
    choice = message.text.lower()
    if choice in settings.SUBJECT_LIST:
        logging.info(f'Пользователь {message.from_user.username} выбрал предмет {choice.capitalize()}')
        bot.send_message(
            chat_id=message.chat.id,
            text=messages.MESSAGE_CHOICE.format(choice=choice),
            reply_markup=markups.get_empty_markup()
        )
        bot.register_next_step_handler(message, search, choice)

    elif choice == settings.CANCEL_WORD:
        logging.info(f'Пользователь {message.from_user.username} отменил выбор предмета')
        return
    else:
        logging.info(f'Пользователь {message.from_user.username} выбрал предмет неверно --> повторный выбор')
        bot.send_message(
            chat_id=message.chat.id,
            text=messages.MESSAGE_CHOICE_SUBJECT_ERROR,
            reply_markup=markups.get_menu_markup(need_cancel=True)
        )
        bot.register_next_step_handler(message, subject_choice)

def search(message:types.Message, choice):
    search = message.text.lower()

    # if search == settings.CANCEL_WORD:
    #     #TODO:
    #     #Добавить сообщение которое будет отправляться после отмены
    #     return
    for symbol in settings.SPECIAL_SYMBOLS:
        search = search.replace(symbol,'')

    search = search.split(" ")
    response = handler.search_in_json(*search)
    

    bot.send_message(message.chat.id, text='\n'.join(response), parse_mode='HTML')

    bot.register_next_step_handler(message, search, choice)

if __name__ == "__main__":
    try:
        logging.info('Бот запущен')
        bot.infinity_polling()
    except Exception as e:
        logging.error(f'Ошибка.')
    finally:
        logging.info(f'Бот завершил работу')
    