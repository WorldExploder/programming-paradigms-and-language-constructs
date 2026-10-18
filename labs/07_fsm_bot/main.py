import sys
from bot import RegistrationBot
from telegram_api import run_bot


if __name__ == '__main__':
    bot = RegistrationBot()
    if '--demo' in sys.argv:
        for message in ['/start', 'Анна', 'ИУ5-31Б', 'Да']:
            answer, keyboard = bot.reply(1, message)
            print('Пользователь:', message)
            print('Бот:', answer)
            print('Состояние:', bot.sessions[1]['state'])
    else:
        run_bot(bot.reply)
