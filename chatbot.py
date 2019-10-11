import os, io
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters  # import modules
import chatbotmodel
import telegram
import json
import re
from chatbotmodel import get_token


bot_token = get_token()

ingamsung = telegram.Bot(token = bot_token)
updates = ingamsung.getUpdates()

# message reply function
# update is json format

def get_message(bot , update) :
    if update.message.text == "bye":
        ingamsung.sendMessage('Bye!')
        ingamsung.stop()
    else:
        #receiving message and complying automatically
        user_input_text = update.message.text
        tag_list = re.findall(r"#(\w+)", user_input_text)
        print(tag_list)
        update.message.reply_text("예, : " + str(tag_list) + "를 갖고 글을 써보겠습니다!")

        if len(tag_list) == 0:
            update.message.reply_text("아무런 태그를 주지 않으셨어요 ㅠㅠ")
            update.message.reply_text("혹시 해시태그를 붙이셔서 저한테 알려주실래요?")
        else:
            ingamsung.sendMessage("글은 한 번 써보았습니다!")
            # 여기에다가 모델을 붙일 예정


updater = Updater(bot_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

ingamsung = chatbotmodel.ingamsung_bot()

updater.start_polling(timeout=3, clean=True)
updater.idle()

ingamsung.start()
