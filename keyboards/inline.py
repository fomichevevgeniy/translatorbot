from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.configs import LANGUAGES

def generate_languages():
    markup = InlineKeyboardMarkup(row_width=2) # Сколько кнопок в строчку
    buttons = []
    for code, lang in LANGUAGES.items():
        btn = InlineKeyboardButton(text=lang, callback_data=f'lang_{code}')
        # Русский  (lang_ru)
        buttons.append(btn)
    markup.add(*buttons)
    return markup


# lst = [1,2,3]
#
# print(*lst)
