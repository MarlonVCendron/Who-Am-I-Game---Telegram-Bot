import tokens

from flask import Flask
from flask import Response
from flask import request

from flask_sslify import SSLify

import re
import json
import requests

import urllib.request
import urllib.parse

app = Flask(__name__)
sslify = SSLify(app)

BASE_URL = f'https://api.telegram.org/bot{tokens.BOT_TOKEN}/'

def parse_message(message):
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']

    pattern = r'^/[a-zA-Z]*'
    ticker = re.findall(pattern, txt)

    if ticker:
        symbol = ticker[0][1:].upper()
    else:
        symbol = ''

    return chat_id, symbol

def send_message(chat_id, text=''):
    # resp = urllib.request.urlopen(BASE_URL + 'sendMessage', urllib.parse.urlencode({
    #     'chat_id': str(chat_id),
    #     'text': text.encode('utf-8'),
    #     'disable_web_page_preview': 'true',
    #     'reply_markup': json.dumps({'inline_keyboard':[[{'text': 'a', 'callback_data': 'a'}, {'text': 'b', 'callback_data': 'b'}]]}),
    # })).read()
    #
    url = BASE_URL + 'sendMessage'
    d = {
        'chat_id': str(chat_id),
        'text': text.encode('utf-8'),
        'disable_web_page_preview': 'true',
        'reply_markup': json.dumps({'inline_keyboard':[[{'text': 'Sim', 'callback_data': 'a'}, {'text': 'Não', 'callback_data': 'b'}]]}),
    }

    f = urllib.parse.urlencode(d)
    f = f.encode('utf-8')

    req = urllib.request.Request(url, f)

    with urllib.request.urlopen(req,data=f) as u:
        resp = u.read()
        print(resp)

    # button_list = [
    #     InlineKeyboardButton("col1", callback_data='a'),
    #     InlineKeyboardButton("col2", callback_data='a'),
    #     InlineKeyboardButton("row 2", callback_data='a')
    # ]
    # reply_markup = InlineKeyboardMarkup(util.build_menu(button_list, n_cols=2))
    # json_keyboard = json.dumps({'inline-keyboard': [[{'text': 'Teste', 'callback_data': '2'}]]})
    # payload = {'chat_id': chat_id, 'text': text, 'reply_markup': json_keyboard}

    # r = requests.post(url, json=payload)
    # return r

def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        msg = request.get_json()
        chat_id, symbol = parse_message(msg)

        if not symbol:
            # send_message(chat_id, 'Wrong data')
            return Response('Ok', status=200)


        if symbol == 'START':
            send_message(chat_id, 'Iniciando um jogo...')
        else:
            send_message(chat_id, 'Luan Bananãozão')

        with open('telegram_request.json', 'w') as f:
            json.dump(msg, f)

        return Response('Ok', status=200)
    else:
        return '<h1>Quem sou eu?</h1>'

def main():
    pass


if __name__ == '__main__':
    # main()
    app.run(debug=True)
