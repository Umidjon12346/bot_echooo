from flask import Flask
import telegram

app = Flask(__name__)

Token = "6745554947:AAH0Xt-pNF7dasRCeI2BjgMuXN-1o-DzFbk"
bot = telegram.Bot(Token)
chat_id = "1806482236"

statust = bot.get_webhook_info()

@app.route("/")
def user():
    bot.send_message(chat_id= chat_id,text=str(statust))
    return "HEllo"

if __name__=="__main__":
    app.run(debug=True)   