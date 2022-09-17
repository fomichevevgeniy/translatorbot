from data.loader import bot, db
from telebot.types import Message, ReplyKeyboardRemove
from keyboards.inline import generate_languages
from googletrans import Translator
from .commands import command_start
@bot.message_handler(regexp='Начать перевод')
def start_processing(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Для выбора на какой язык перести. Выберите ниже.',
                     reply_markup=ReplyKeyboardRemove())
    bot.send_message(chat_id, 'Выберите язык', reply_markup=generate_languages())


def finish_translate(message: Message, lang):
    # А функция будет создана на следующем уроке
    chat_id = message.chat.id
    ru_text = message.text
    translator = Translator()
    translated_text = translator.translate(text=ru_text, src='ru', dest=lang).text
    bot.send_message(chat_id, translated_text)
    db.insert_into_db(telegram_id=chat_id,
                      original_text=ru_text,
                      src='ru',
                      dest=lang,
                      translated_text=translated_text)

    command_start(message)





