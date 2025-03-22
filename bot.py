from pymongo import MongoClient
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import urllib.parse
from dotenv import load_dotenv
import os
import requests
import gridfs

load_dotenv()
MONGO_STR = os.getenv("MONGO_STR")
BOT_TOKEN = os.getenv("BOT_TOKEN")

client = MongoClient(MONGO_STR)
db = client["telegram_db"]
collection = db["ImageWithCaption"]

fs = gridfs.GridFS(db)

async def store_photo_with_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        if update.message.caption:
            photo = update.message.photo[-1]
            file = await context.bot.get_file(photo.file_id)
            file_path = file.file_path
            response = requests.get(file_path)
            file_id = fs.put(response.content, filename=f"{update.message.from_user.id}_{photo.file_id}.jpg")
            data = {
            "user_id": update.message.from_user.id,
            "username": update.message.from_user.username,
            "message": update.message.caption,
            "image_id": file_id,
            "timestamp": update.message.date}
            collection.insert_one(data)
            await update.message.reply_text("Image + Text saved to MongoDB!")
        else:
            await update.message.reply_text("Please send Image with text")
    else:
        await update.message.reply_text("Please send Image with text")
       

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO | filters.CAPTION |filters.TEXT, store_photo_with_text))
    print("🚀 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
