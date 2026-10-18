import unittest
from bot import RegistrationBot


class StateMachineTests(unittest.TestCase):
    def setUp(self):
        self.bot = RegistrationBot()
        self.bot.reply(1, '/start')

    def test_three_state_registration(self):
        self.assertEqual(self.bot.sessions[1]['state'], 'NAME')
        self.bot.reply(1, 'Анна')
        self.assertEqual(self.bot.sessions[1]['state'], 'GROUP')
        self.bot.reply(1, 'ИУ5-31Б')
        self.assertEqual(self.bot.sessions[1]['state'], 'CONFIRM')
        self.assertIn('Запись принята', self.bot.reply(1, 'Да')[0])
        self.assertEqual(self.bot.sessions[1]['state'], 'NAME')

    def test_empty_input_and_confirmation(self):
        self.bot.reply(1, ' ')
        self.assertEqual(self.bot.sessions[1]['state'], 'NAME')
        self.bot.reply(1, 'Анна')
        self.bot.reply(1, ' ')
        self.assertEqual(self.bot.sessions[1]['state'], 'GROUP')
        self.bot.reply(1, 'ИУ5-31Б')
        self.bot.reply(1, 'возможно')
        self.assertEqual(self.bot.sessions[1]['state'], 'CONFIRM')
        self.bot.reply(1, 'Нет')
        self.assertEqual(self.bot.sessions[1]['state'], 'NAME')

    def test_users_are_independent_and_cancel_resets(self):
        self.bot.reply(1, 'Анна')
        self.bot.reply(2, '/start')
        self.assertEqual(self.bot.sessions[2]['state'], 'NAME')
        self.assertEqual(self.bot.sessions[1]['state'], 'GROUP')
        self.bot.reply(1, '/cancel')
        self.assertEqual(self.bot.sessions[1], {'state': 'NAME'})
