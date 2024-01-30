from flask import Flask,request
import telegram

app = Flask(__name__)

Token = "6745554947:AAH0Xt-pNF7dasRCeI2BjgMuXN-1o-DzFbk"
bot = telegram.Bot(Token)

@app.route("/", methods = ["POST"])
def user():
    data = request.get_json()
    print(data)
    bot.send_message(chat_id=data.message.chat.id,text= data.message.text)
    return "HElo"

if __name__=="__main__":
    app.run(debug=True)   