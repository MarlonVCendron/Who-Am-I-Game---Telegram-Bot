from flask import Flask
from flask import Response
from flask import request

from flask_sslify import SSLify

import re
import json
import requests

token = '1017619539:AAEAwBnuqNwAm-G9ZIm3JeLOjBJgCbwEqEY'

app = Flask(__name__)
sslify = SSLify(app)

def parse_message(message):
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']

    pattern = r'/[a-zA-Z]'
    ticker = re.findall(pattern, txt)

    if ticker:
        symbol = ticker[0][1:].upper()
    else:
        symbol = ''

    return chat_id, symbol

def send_message(chat_id, text=''):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}

    r = requests.post(url, json=payload)
    return r

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        msg = request.get_json()
        chat_id, symbol = parse_message(msg)

        if not symbol:
            # send_message(chat_id, 'Wrong data')
            return Response('Ok', status=200)

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
