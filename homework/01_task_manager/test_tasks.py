import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from main import load_tasks, save_tasks, add_task, complete_task


class TaskTests(unittest.TestCase):
    def test_add_and_complete(self):
        tasks = []
        self.assertEqual(add_task(tasks, 'Прочитать задание'), 1)
        complete_task(tasks, 1)
        self.assertTrue(tasks[0]['done'])

    def test_save_and_load(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / 'tasks.json'
            self.assertEqual(load_tasks(path), [])
            tasks = []
            add_task(tasks, 'Лабораторная 1')
            save_tasks(path, tasks)
            self.assertEqual(load_tasks(path), tasks)

    def test_input_errors(self):
        with self.assertRaises(ValueError):
            add_task([], ' ')
        with self.assertRaises(ValueError):
            complete_task([], 17)
