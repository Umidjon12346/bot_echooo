import telegram



Token = "6745554947:AAH0Xt-pNF7dasRCeI2BjgMuXN-1o-DzFbk"
bot = telegram.Bot(Token)
url = "https://umidjon12346.pythonanywhere.com/"
bot.setWebhook(url)
print(bot.get_webhook_info())