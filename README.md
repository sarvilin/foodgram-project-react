# Проект "Foodgram"

версия c Docker, Continuous Integration на GitHub Actions

развернут по адресу http://84.252.138.138

![workflow](https://github.com/sarvilin/foodgram-project-react/actions/workflows/main.yml/badge.svg)

## Описание
Приложение «Продуктовый помощник»: сайт, на котором пользователи будут публиковать рецепты,
добавлять чужие рецепты в избранное и подписываться на публикации других авторов. 
Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно 
купить для приготовления выбранных блюд. 


## Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

## Установка на локальном компьютере
Эти инструкции помогут вам создать копию проекта и запустить ее на локальном компьютере для целей разработки и тестирования.

### Установка Docker
Установите Docker, используя инструкции с официального сайта:
- для [Windows и MacOS](https://www.docker.com/products/docker-desktop)
- для [Linux](https://docs.docker.com/engine/install/ubuntu/). Отдельно потребуется установть [Docker Compose](https://docs.docker.com/compose/install/)

### Запуск проекта (на примере Linux)

- Склонируйте в текущую папку `git clone https://github.com/sarvilin/foodgram-project-react`
- Перейдите в папку `cd foodgram-project-react`
- Создайте файл `.env` командой `touch .env` и добавьте в него переменные окружения для работы с базой данных:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 
```
- Запустите docker-compose командой `sudo docker-compose up -d`


## Деплой на удаленный сервер
Для запуска проекта на удаленном сервере необходимо:

- скопировать на сервер файлы `docker-compose.yaml` и  `nginx.conf` командой:
```
scp -r docker-compose.yml <user>@<server-ip>:/home/<user>
scp -r nginx/default.conf <user>@<server-ip>:/home/<user>/nginx
```
- создать переменные окружения в разделе `secrets` настроек текущего репозитория:
```
DOCKER_PASSWORD # Пароль от Docker Hub
DOCKER_USERNAME # Логин от Docker Hub
HOST # Публичный ip адрес сервера
USER # Пользователь зарегистрированный на сервере
PASSPHRASE # Если ssh-ключ защищен фразой-паролем
SSH_KEY # Приватный ssh-ключ
TELEGRAM_TO # ID телеграм-аккаунта
TELEGRAM_TOKEN # Токен бота
DB_ENGINE # django.db.backends.postgresql
DB_HOST # db
DB_NAME # postgres
DB_PORT # 5432
POSTGRESS_PASSWORD # пользователь postgres 
POSTGRES_USER # пароль postgres 
SECRET_KEY # секретный ключ Django
```

### После каждого обновления репозитория (`git push`) будет происходить:
1. Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest из репозитория foodgram-project-react
2. Сборка и доставка докер-образов на Docker Hub.
3. Автоматический деплой.
4. Отправка уведомления в Telegram.


## После запуска проекта необходимо:

- Создайте суперпользователя Django `sudo docker-compose exec backend python manage.py createsuperuser`
- Загрузите в базу данных ингредиенты `sudo docker-compose exec backend python3 manage.py loaddata ingredients.json`
- Загрузите в базу данных теги `sudo docker-compose exec backend python3 manage.py load_tags`

### *Backend by:*
[Сарвилин Алексей](https://github.com/sarvilin/foodgram-project-react)
### *Frontend by:*
https://github.com/yandex-praktikum/foodgram-project-react