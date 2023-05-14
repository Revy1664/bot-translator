import telebot
import translators as ts

from config import TOKEN


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
	"""
		"start" command handler
	"""

	bot.send_message(message.chat.id, f"Привет, <b>{message.from_user.first_name}</b>😄😄! Меня зовут <b>{bot.get_me().first_name}</b>. Я помогу тебе с переводом🙃. Введи <i>/help</i> для большей информации🔥🔥🔥", parse_mode="html")

@bot.message_handler(commands=["help"])
def send_help(message):
	"""
		"help" command handler
	"""
	with open("content/help.txt", "r", encoding="utf-8") as file:
		bot.send_message(message.chat.id, file.read())

@bot.message_handler(commands=["translate"])
def send_translate(message):
	"""
		"translate" command handler
	"""

	sent_msg = bot.send_message(message.chat.id, "Введи текст сообщения😊")
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

	try:
		translated_message = ts.translate_text(text, to_language=to_lang)
	except Exception:
		

	bot.send_message(message.chat.id, translated_message)

bot.infinity_polling()