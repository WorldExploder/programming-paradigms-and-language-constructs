import sys
from bot import reply
from telegram_api import run_bot


if __name__ == '__main__':
    if '--demo' in sys.argv:
        for message in ['/start', 'Лабораторные', 'Вариант', 'Помощь', '???']:
            answer, keyboard = reply(1, message)
            print('Пользователь:', message)
            print('Бот:', answer)
        print('Кнопки:', keyboard['keyboard'])
    else:
        run_bot(reply)
