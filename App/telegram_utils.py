import telegram

# token account telegram
my_token = ""
my_chatid = ''

# create Bot
bot = telegram.Bot(token=my_token)

# send text message


def send_telegram(photo_path="data/alert.png"):
    try:
        bot = telegram.Bot(token=my_token)
        bot.sendPhoto(chat_id=my_chatid, photo=open(
            photo_path, "rb"), caption="Có người đang đứng ở quầy hàng!!!")
    except Exception as ex:
        print("Can not send message telegram ", ex)

    print("Send sucess")