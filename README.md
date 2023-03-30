# Проект парсинга pep
### Описание scrapy_parser_pep:
Благодаря этому парсеру можно:
- загрузить сводную таблицу PEP (status_summary.csv): номер PEP, имя PEP и статус PEP.
- загрузить статусы PEP (pep.csv): посчитать количество PEP в каждом статусе
     и общее количество PEP.

### УСТАНОВКА:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:ArtemBalandin81/scrapy_parser_pep.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

## Используемые технологии:

- Python 3.7
- Фреймворк Scrapy

## Некоторые примеры запросов парсера

- Запустить парсер:
- файлы 'status_summary.csv' и 'pep.csv' будут загружены в каталог 'results'

```
(venv) ...$ scrapy crawl pep
```
### Автор
[Артем Баландин](https://github.com/ArtemBalandin81)