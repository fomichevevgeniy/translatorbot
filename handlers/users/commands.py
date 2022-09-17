from data.loader import bot, db
from telebot.types import Message
from keyboards.reply import start_translate

@bot.message_handler(commands=['start'])
def command_start(message: Message):

    chat_id = message.chat.id
    bot.send_message(chat_id, f'Здравствуйте, {message.from_user.full_name}')
    bot.send_message(chat_id, 'Для начала перевода, нажмите на кнопку ниже.',
                     reply_markup=start_translate())
