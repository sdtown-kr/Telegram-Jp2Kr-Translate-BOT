import telepot
import requests

bot_token = 'BOT TOKEN HERE'
bot = telepot.Bot(bot_token)
chat_id = 'ID HERE'

def get_translate(text):
    client_id = "Papago Client ID HERE"
    client_secret = "Papago Client Secret HERE"

    data = {'text' : text,
            'source' : 'ja',
            'target': 'ko'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id":client_id,
              "X-Naver-Client-Secret":client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode==200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        print("Error Code:" , rescode)


def handle(msg):
    chat_text = msg['text']
    trans = get_translate(chat_text)
    bot.sendMessage(chat_id, trans)
bot.message_loop(handle)

while True:
    pass
