from bs4 import BeautifulSoup
import requests
import telebot
import data

# # ---------------- GET PRICE ----------------------------- #

response = requests.get("https://appbrewery.github.io/instant_pot/")
amazon_page = response.text

soup = BeautifulSoup(amazon_page, "html.parser")

# print(soup)

price = float(soup.find(name="span", class_="aok-align-center").get_text().split("$")[1])

print(f"Instant pot price: ${price}")


# #--------------Let Telegram-bot to send a message------- #

TOKEN = data.TOKEN
bot = telebot.TeleBot(TOKEN)
chat_id = data.CHAT_ID


@bot.message_handler(func=lambda message: True)
def send_message():
    bot.send_message(chat_id=chat_id, text=f"The price of instant pot has changed to: ${price}\n")

# # ------------- CHECK PRICE ------------------------------#


def check_price():
    if price <= 99.99:
        send_message()

# # -------------- CHECK TIME ------------------------------#


check_price()
