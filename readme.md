Тестовое задание: "Проект на Django. КиНаходка - сервис по совету фильмов"

Старт 24.09.2023 ~03:30

БД - PostgreSQL

По этапам:
1. django-admin startproject 'kino' / cd kino / py manage.py startapp 'kinahodka'
2. Первоначальная миграция + создание superuser (py manage.py migrate superuser) ()
3. Набросок схемы БД по внутрянке фильма (название, режиссер, год.)
4. Подключение постреса
5. Создание моделей, миграция, добавление в админку инфы о моделях