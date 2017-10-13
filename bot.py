from telegram.ext import Updater, CommandHandler

API_TOKEN = '414864281:AAH59EPz2gI3FOJgQ58NcZIhTEkQ3fUSg8Y'

def start(bot, update):
	update.message.reply_text('Welcome {}'.format(update.message.from_user.first_name))

def hello(bot, update):
	update.message.reply_text('Hello {}, Nice to meet you :)'.format(update.message.from_user.first_name))

updater = Updater(API_TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
