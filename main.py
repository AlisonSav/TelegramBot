import telebot
from telebot import types

bot = telebot.TeleBot("6103719353:AAHGK1VXjF0JaoDvmar5bQhivY2UltLShEg")


@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Privetuli <b>{message.from_user.first_name} {message.from_user.last_name}</b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["website"])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Open Google", url="https://google.com"))
    bot.send_message(message.chat.id, "Opening...", reply_markup=markup)


@bot.message_handler(commands=["help"])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton("Google")
    start = types.KeyboardButton("Start")
    markup.add(website, start)
    bot.send_message(message.chat.id, "Menu", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "Halo":
        bot.send_message(message.chat.id, "I tebe Halo!", parse_mode="html")
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Your ID is: {message.from_user.id}", parse_mode="html")
    elif message.text == "photo":
        photo = open("mavka2.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'I dont understand you((', parse_mode="html")


@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Oe, good photo!")




bot.polling(none_stop=True)
