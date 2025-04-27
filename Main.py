from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from pytube import YouTube
import os

TOKEN = "8101569569:AAEzTyObrG0Na4OzIJsyVZtZjS55s-wk018"

def start(update: Update, context: CallbackContext):
    update.message.reply_text('سلام! لینک یوتیوب رو بفرست تا دانلودش کنم 🎥')

def download_video(update: Update, context: CallbackContext):
    url = update.message.text
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(filename="video.mp4")
        update.message.reply_video(video=open('video.mp4', 'rb'))
        os.remove('video.mp4')
    except Exception as e:
        update.message.reply_text(f"خطا: {e}")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, download_video))
updater.start_polling()
updater.idle()
