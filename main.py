import telebot
import translators as ts

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def welcome(message):
	"""
		"start" command handler
	"""

	sent_msg = bot.send_message(message.chat.id, "Привет!😄 \b Я переведу для тебя любое предложение😊")
	bot.register_next_step_handler(sent_msg, text_handler)

def text_handler(message):
	"""
		Text for translate
	"""

	text = message.text
	sent_msg = bot.send_message(message.chat.id, f"Отлично😉 \n На какой язык хочешь перевести?🤔")
	bot.register_next_step_handler(sent_msg, to_lang_handler, text)

def to_lang_handler(message, text):
	"""
		To language
	"""

	to_lang = message.text
	translated_message = ts.translate_text(text, to_language=to_lang)

	bot.send_message(message.chat.id, translated_message)


bot.infinity_polling()