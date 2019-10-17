import telebot
from flask import Flask, request
import os 

TOKEN = '864467999:AAE_GoBsrJMIKpTzIsMGmp_fCLP4hN_l2pI'

bot= telebot.TeleBot(token= TOKEN)
server = Flask(__name__)

def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i

# using decorator function
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome ')

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, 'How are you') 

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'type commands such as: /start, /hello, /help etc')

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '@': # in case it's just the '@', skip
        pass
    else:
        insta_link = "https://instagram.com/{}".format(at_text[1:])
        bot.reply_to(message, insta_lin

   
@server.route('/' + TOKEN, methods= ['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))  ])
    return "!", 200
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://nameless-oasis-29324.herokuapp.com/ '+ TOKEN)
    return "!", 200
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))