from telegram.ext import Updater, CommandHandler

token = "5872290236:AAHp-7Ey00NDBtGJLU5JmcBtGDaQcxgGlt0"

updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello! Welcome to the Simplilearn")

def help(update, context):
    update.message.reply_text(
    """
    /start -> Welcome to the Channel
    /help -> This particular message
    /content -> About playlists of simplilearn
    /Python -> The first video from Python Playlists
    /SQL -> The first video from SQL Playlists
    /Java -> The first video from Java Playlists
    /contact -> contact information
    """
    )

def content(udpate, context):
    udpate.message.reply_text("We have various playlists and articles available")

def Python(update, context):
    update.message.reply_text("tutorial link: https://www.youtube.com/watch?v=227uk4kDTM8")
    
def SQL(update, context):
    update.message.reply_text("tutorial link: https://www.youtube.com/watch?v=DvNHkJAR0BM&list=PLEiEAq2VkUUKL3yPbn8yWnatjUg0P0I-Z&index=2")
    
def Java(update, context):
    update.message.reply_text("tutorial link: https://www.youtube.com/watch?v=i6AZdFxTK9I&list=PLEiEAq2VkUUI5_Z4vOtWE6AMcSrYbth1t")
    
def contact(update, context):
    update.message.reply_text("You can contact n the registered mail id provided on the website")
    
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('Python', Python))
dispatcher.add_handler(CommandHandler('SQL', SQL))
dispatcher.add_handler(CommandHandler('Java', Java))
dispatcher.add_handler(CommandHandler('contact', contact))
dispatcher.add_handler(CommandHandler('content', content))
dispatcher.add_handler(CommandHandler('help', help))

updater.start_polling()
updater.idle()
