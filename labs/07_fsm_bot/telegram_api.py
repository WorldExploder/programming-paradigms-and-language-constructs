import json
import os
from urllib.request import Request, urlopen
from urllib.error import URLError


def api_call(token, method, payload):
    data = json.dumps(payload).encode('utf-8')
    request = Request(f'https://api.telegram.org/bot{token}/{method}', data=data,
                      headers={'Content-Type': 'application/json'})
    try:
        with urlopen(request, timeout=40) as response:
            answer = json.load(response)
    except (URLError, TimeoutError, ValueError):
        # Не выводим URL ошибки: он содержит секретный токен.
        raise RuntimeError('Не удалось обратиться к Telegram API') from None
    if not answer.get('ok'):
        raise RuntimeError('Telegram API отклонил запрос')
    return answer['result']


def run_bot(reply):
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    if not token:
        raise SystemExit('Задайте TELEGRAM_BOT_TOKEN или запустите main.py --demo')
    offset = 0
    print('Бот запущен. Для остановки нажмите Ctrl+C.')
    try:
        while True:
            updates = api_call(token, 'getUpdates', {'offset': offset, 'timeout': 30,
                                                   'allowed_updates': ['message']})
            for update in updates:
                message = update.get('message', {})
                if 'text' in message:
                    key = (message['chat']['id'], message['from']['id'])
                    text, keyboard = reply(key, message['text'])
                    payload = {'chat_id': message['chat']['id'], 'text': text}
                    if keyboard:
                        payload['reply_markup'] = keyboard
                    api_call(token, 'sendMessage', payload)
                offset = update['update_id'] + 1
    except KeyboardInterrupt:
        print('Бот остановлен.')
    except RuntimeError as error:
        raise SystemExit(str(error)) from None
