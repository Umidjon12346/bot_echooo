from flask import Flask
import telegram
import app as ap

app = Flask(__name__)

chat_id = "1806482236"
@app.route("/")
def user():
    ap.bot.send_message(chat_id= chat_id,text="Hi")
    return "HEllo"

if __name__=="__main__":
    app.run(debug=True)   