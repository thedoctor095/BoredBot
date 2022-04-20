import logging
from boredom import get_request as gr
from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello!\nMy name is BoredomBot!\nType /help to see what I can do!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('BoredomBot at your service!\nDepending on your boredom level I can suggest a few activities to try out!\n'
                              'Type /anything to suggest a random activity for you to try.\n'
                              'Type /education to suggest educational activities for you to try.\n'
                              'Type /recreational to suggest recreational activities for you to try.\n'
                              'Type /social to suggest social activities for you to try.\n'
                              'Type /diy to suggest Do It Yourself activities for you to try.\n'
                              'Type /charity to suggest charity activities for you to try.\n'
                              'Type /cooking to suggest cooking activities for you to try.\n'
                              'Type /relaxation to suggest relaxation activities for you to try.\n'
                              'Type /music to suggest activities which imply music.\n'
                              'Type /busywork to suggest activities that keep you occupied.\n')


def boredom_request(update, context):
    update.message.reply_text(gr(update.message.text.replace("/", "")))


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler('anything', boredom_request))
    dp.add_handler(CommandHandler('education', boredom_request))
    dp.add_handler(CommandHandler('recreational', boredom_request))
    dp.add_handler(CommandHandler('social', boredom_request))
    dp.add_handler(CommandHandler('diy', boredom_request))
    dp.add_handler(CommandHandler('charity', boredom_request))
    dp.add_handler(CommandHandler('cooking', boredom_request))
    dp.add_handler(CommandHandler('relaxation', boredom_request))
    dp.add_handler(CommandHandler('music', boredom_request))
    dp.add_handler(CommandHandler('busywork', boredom_request))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
