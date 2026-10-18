"""Запуск всех модульных и BDD-проверок из корня репозитория."""
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent
directories = [
    'labs/01_basics', 'labs/02_oop', 'labs/03_functional',
    'labs/04_testing', 'labs/05_patterns', 'labs/06_bot',
    'labs/07_fsm_bot', 'homework/01_task_manager', 'assessments/rk_02',
]
failed = []
for directory in directories:
    print(f'\n--- {directory} ---', flush=True)
    result = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-v'],
                            cwd=root / directory)
    if result.returncode:
        failed.append(directory)
for directory in ['labs/04_testing', 'labs/05_patterns']:
    print(f'\n--- BDD {directory} ---', flush=True)
    result = subprocess.run([sys.executable, '-m', 'behave', '--no-color'],
                            cwd=root / directory)
    if result.returncode:
        failed.append(directory + ' BDD')
if failed:
    print('Не прошли проверки:', ', '.join(failed))
    raise SystemExit(1)
print('\nВсе проверки пройдены.')
