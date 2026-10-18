import unittest
from unittest.mock import patch
from bot import reply
from telegram_api import api_call


class BotTests(unittest.TestCase):
    def test_menu_has_buttons(self):
        text, keyboard = reply(1, '/start')
        self.assertIn('Выберите', text)
        self.assertIn(['Лабораторные', 'Вариант'], keyboard['keyboard'])

    def test_variant_and_unknown_message(self):
        self.assertIn('17', reply(1, 'Вариант')[0])
        self.assertIn('Неизвестная', reply(1, '???')[0])

    @patch('telegram_api.urlopen')
    def test_api_payload_with_mock(self, urlopen):
        response = urlopen.return_value.__enter__.return_value
        response.read.return_value = b'{"ok": true, "result": []}'
        self.assertEqual(api_call('test-token', 'getUpdates', {}), [])
