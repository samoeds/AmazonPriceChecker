from bs4 import BeautifulSoup
import requests
import telebot
import data

# # ---------------- GET PRICE ----------------------------- #


headers = {"Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
           "Accept-Encoding": "gzip, deflate, br, zstd",
           }
response = requests.get("https://appbrewery.github.io/instant_pot/", headers=headers)
# response = requests.get("https://a.co/d/5Nkf9mz", headers=headers)

amazon_page = response.text

soup = BeautifulSoup(amazon_page, "html.parser")

# print(soup)

price = float(soup.find(name="span", class_="aok-offscreen").get_text().split("$")[1])

print(f"Spirited away figure price: ${price}")


# #--------------Let Telegram-bot to send a message------- #

TOKEN = data.TOKEN
bot = telebot.TeleBot(TOKEN)
chat_id = data.CHAT_ID


@bot.message_handler(func=lambda message: True)
def send_message():
    bot.send_message(chat_id=chat_id, text=f"The price of instant pot has changed to: ${price}\n")

# # ------------- CHECK PRICE ------------------------------#


def check_price():
    if price >= 19:
        send_message()


check_price()
