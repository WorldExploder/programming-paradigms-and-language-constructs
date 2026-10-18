"""Распаковать исходный учебный набор без дополнительных библиотек."""
import gzip
from pathlib import Path

directory = Path(__file__).resolve().parent
with gzip.open(directory / 'data_light.json.gz', 'rb') as source:
    (directory / 'data_light.json').write_bytes(source.read())
print('Готово: data_light.json')
