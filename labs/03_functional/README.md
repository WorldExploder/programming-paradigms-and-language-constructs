# Лабораторная работа 3

## Функциональные возможности Python

Решить все семь задач: генератор field, генератор случайных чисел, итератор Unique, две сортировки по модулю, декоратор print_result, два контекстных менеджера времени и цепочка f1–f4 для обработки вакансий. Функции f1–f3 содержат по одному выражению, f4 использует zip и генератор зарплат.

Вариант: 17, где он предусмотрен заданием.

Источник: https://github.com/ugapanyuk/BKIT_2022/wiki/lab_python_fp

Python 3.10 или новее. Установите зависимости из корневого requirements.txt.

## Запуск из этой папки

```bash
python lab_python_fp/field.py
python lab_python_fp/gen_random.py
python lab_python_fp/unique.py
python lab_python_fp/sort.py
python lab_python_fp/print_result.py
python lab_python_fp/cm_timer.py
python -m lab_python_fp.process_data data_demo.json
python unpack_data.py
python -m unittest discover -v
```

field пропускает None и отсутствующие поля, сохраняя нулевые значения. Unique принимает список или генератор и сравнивает строки без учёта регистра при ignore_case=True, сохраняя исходное написание. Декоратор возвращает результат функции. Таймеры не подавляют исключения. Цепочка вакансий использует job-name из исходного учебного набора.

Полный исходный набор включён в data_light.json.gz. После распаковки: `python -m lab_python_fp.process_data data_light.json`.

## Результаты

Все семь задач выполнены. Цепочка отдельно запущена на полном исходном data_light.json; исходный файл хранится без изменений в архиве gzip. Случайные зарплаты попадают в диапазон 100000–200000. Результаты случайного генератора и время при повторном запуске изменяются.

Отчёт: [DOCX](report.docx), [PDF](report.pdf), [Markdown](report.md). Протокол запусков: [results.txt](results.txt).
