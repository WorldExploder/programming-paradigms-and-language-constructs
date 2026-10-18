import argparse
import json
from pathlib import Path


def load_tasks(path):
    """Если файл ещё не создан, начинаем с пустого списка."""
    path = Path(path)
    if not path.exists():
        return []
    with path.open(encoding='utf-8') as file:
        tasks = json.load(file)
    if not isinstance(tasks, list):
        raise ValueError('В файле должен находиться список задач')
    for task in tasks:
        if (not isinstance(task, dict) or not isinstance(task.get('id'), int)
                or not isinstance(task.get('title'), str)
                or not isinstance(task.get('done'), bool)):
            raise ValueError('Неверная структура задачи в файле')
    return tasks


def save_tasks(path, tasks):
    """Сохраняем данные в читаемом UTF-8 JSON."""
    with Path(path).open('w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


def add_task(tasks, title):
    """ID не зависит от позиции задачи в списке."""
    title = title.strip()
    if not title:
        raise ValueError('Название не должно быть пустым')
    task_id = max((task['id'] for task in tasks), default=0) + 1
    tasks.append({'id': task_id, 'title': title, 'done': False})
    return task_id


def complete_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            return
    raise ValueError('Задача не найдена')


def main():
    parser = argparse.ArgumentParser(description='Учебный список задач')
    parser.add_argument('--file', default='tasks.json')
    commands = parser.add_subparsers(dest='command', required=True)
    add = commands.add_parser('add')
    add.add_argument('title')
    commands.add_parser('list')
    done = commands.add_parser('done')
    done.add_argument('id', type=int)
    arguments = parser.parse_args()
    try:
        tasks = load_tasks(arguments.file)
        if arguments.command == 'add':
            print('Добавлена задача', add_task(tasks, arguments.title))
            save_tasks(arguments.file, tasks)
        elif arguments.command == 'done':
            complete_task(tasks, arguments.id)
            save_tasks(arguments.file, tasks)
            print('Задача выполнена:', arguments.id)
        else:
            for task in tasks:
                mark = 'x' if task['done'] else ' '
                print(f"[{mark}] {task['id']}: {task['title']}")
            if not tasks:
                print('Список задач пуст.')
    except (ValueError, OSError) as error:
        parser.exit(1, f'Ошибка: {error}\n')


if __name__ == '__main__':
    main()
