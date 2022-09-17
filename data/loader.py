from .configs import TOKEN
from telebot import TeleBot
from database.database import DataBase


bot = TeleBot(TOKEN)

db = DataBase()