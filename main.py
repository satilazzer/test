import sqlite3

from telebot import TeleBot


bot = TeleBot("6547124745:AAHkES88LxUctgqCUuHj13wWxaX98yVrUTc", parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Send me your token")


@bot.message_handler()
def commit_token(message):
    con = sqlite3.connect('DubaiTutor/db.sqlite3')
    cursor = con.cursor()
    print("Database created and Successfully Connected to SQLite")
    if cursor.execute(f"SELECT token_code FROM main_token WHERE token_code='{message.text}'"):
        cursor.execute(f"UPDATE main_token SET user_tg_id='{message.chat.id}' WHERE token_code='{message.text}'")
        con.commit()
        bot.reply_to(message, "Well, now it is connected")
    else:
        bot.reply_to(message, "Such kind of token doesnt exist")
    cursor.close()


bot.infinity_polling()
