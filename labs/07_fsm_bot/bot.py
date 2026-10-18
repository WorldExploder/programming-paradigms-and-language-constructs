class RegistrationBot:
    """Три состояния: NAME, GROUP, CONFIRM. Данные хранятся в памяти."""
    NAME, GROUP, CONFIRM = 'NAME', 'GROUP', 'CONFIRM'

    def __init__(self):
        self.sessions = {}

    def reply(self, user, text):
        if text in ('/start', '/cancel') or user not in self.sessions:
            self.sessions[user] = {'state': self.NAME}
            return 'Введите имя. /cancel начинает ввод заново.', {'remove_keyboard': True}

        session = self.sessions[user]
        text = text.strip()
        if session['state'] == self.NAME:
            if not text:
                return 'Имя не должно быть пустым.', None
            session['name'] = text
            session['state'] = self.GROUP
            return 'Введите группу, например ИУ5-31Б.', None

        if session['state'] == self.GROUP:
            if not text:
                return 'Группа не должна быть пустой.', None
            session['group'] = text
            session['state'] = self.CONFIRM
            message = f"Имя: {session['name']}; группа: {text}. Всё верно?"
            return message, {'keyboard': [['Да', 'Нет']], 'resize_keyboard': True}

        if text.casefold() == 'да':
            message = f"Запись принята: {session['name']}, {session['group']}."
            self.sessions[user] = {'state': self.NAME}
            return message + ' Можно ввести новое имя.', {'remove_keyboard': True}
        if text.casefold() == 'нет':
            self.sessions[user] = {'state': self.NAME}
            return 'Введите имя заново.', {'remove_keyboard': True}
        return 'Выберите Да или Нет.', None
