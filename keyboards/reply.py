from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def start_translate():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text='Начать перевод')
    markup.add(btn)
    return markup
