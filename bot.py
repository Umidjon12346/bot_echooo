from flask import Flask,request
import telegram

app = Flask(__name__)

Token = "6745554947:AAH0Xt-pNF7dasRCeI2BjgMuXN-1o-DzFbk"
bot = telegram.Bot(Token)
url = "https://umidjon12346.pythonanywhere.com/"
bot.delete_webhook()

@app.route("/",methods = ["POST"])
def user():
    data = request.get_json()
    bot.send_message(chat_id=data["result"]["message"]["from"],text=data["result"]["message"]["text"])
    return "HEllo"

if __name__=="__main__":
    app.run(debug=True)   