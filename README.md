# Сайт поставщики Новосибирска

Статическая версия части сайта по поиску поставщиков из Новосибирска.
Сайт построен с помощью шаблонизатора *Jinja*  генератора *staticjinga*


[Главная страница](https://onlinealex.github.io/22_proto_markup/)

[Заявки](https://onlinealex.github.io/22_proto_markup/leads.html)


# Как изменять

## Требования
Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 выше

И  пакетов из requirements.txt
```bash
pip install -r requirements.txt # или командой pip3
```

Помните, рекомендуется использовать [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) для лучшего управления пакетами.
## Насройки

По умолчанию `build.py` генерирует html файлы
(котрые не начинаются на "_" или ".") из папк `/template` в папку `/`

## Как запустить
Стандатной командой `python` (на некоторых компьютерах `python3`)

```bash
$ python build.py
```
> Запуск для всех ОС одинаковый


# Цели проекта
Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)