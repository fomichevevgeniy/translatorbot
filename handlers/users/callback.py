from telebot.types import CallbackQuery
from data.loader import bot
from googletrans import Translator
from .text_handlers import finish_translate


@bot.callback_query_handler(lambda call: 'lang' in call.data)
def ask_text(call: CallbackQuery):
    chat_id = call.message.chat.id
    # lang_ru
    _, lang = call.data.split('_') # _ = lang   lang = ru
    msg = bot.send_message(chat_id, f'Введите текст, который вы хотите перести')
    bot.register_next_step_handler(msg, finish_translate, lang)






