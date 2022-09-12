# Проект "Foodgram"

версия c Docker, Continuous Integration на GitHub Actions

развернут по адресу http://84.252.138.138

![workflow](https://github.com/sarvilin/foodgram-project-react/actions/workflows/main.yml/badge.svg)

## Описание
Приложение «Продуктовый помощник»: сайт, на котором пользователи будут публиковать рецепты,
добавлять чужие рецепты в избранное и подписываться на публикации других авторов. 
Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно 
купить для приготовления выбранных блюд. 

Полная документация к API:  http://84.252.138.138/api/docs/redoc.html


###  Технологии
- Python 3.7
- Django 2.2.19
- DjangoREST framework 3.13.1

## Установка на локальном компьютере
Эти инструкции помогут вам создать копию проекта и запустить ее на локальном компьютере для целей разработки и тестирования.

### Установка Docker
Установите Docker, используя инструкции с официального сайта:
- для [Windows и MacOS](https://www.docker.com/products/docker-desktop)
- для [Linux](https://docs.docker.com/engine/install/ubuntu/). Отдельно потребуется установть [Docker Compose](https://docs.docker.com/compose/install/)

### Запуск проекта (на примере Linux)

- Склонируйте в текущую папку `git clone https://github.com/sarvilin/foodgram-project-react`
- Перейдите в папку `cd foodgram-project-react/infra`
- Создайте файл `.env` командой `touch .env` и добавьте в него переменные окружения для работы с базой данных:
```
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 
```
- Запустите docker-compose командой `sudo docker-compose up -d`


## Деплой на удаленный сервер
Для запуска проекта на удаленном сервере необходимо:





- скопировать на сервер файлы `docker-compose.yaml`, `.env` и папку `nginx` командами:
```
scp docker-compose.yaml  <user>@<server-ip>:
scp .env <user>@<server-ip>:
scp -r nginx/ <user>@<server-ip>:

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
```

### После каждого обновления репозитория (`git push`) будет происходить:
1. Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest из репозитория yamdb_final
2. Сборка и доставка докер-образов на Docker Hub.
3. Автоматический деплой.
4. Отправка уведомления в Telegram.


## После запуска проекта необходимо:

- Сделать миграции `sudo docker-compose exec backend python manage.py migrate`
- Соберите статику командой `sudo docker-compose exec backend python manage.py collectstatic --no-input`
- Создайте суперпользователя Django `sudo docker-compose exec backend python manage.py createsuperuser`
- Загрузите в базу данных ингредиенты `sudo docker-compose exec backend python3 manage.py loaddata ingredients.json`
- Загрузите в базу данных теги `sudo docker-compose exec backend python3 manage.py load_tags`

## Участники:

[Сарвилин Алексей](https://github.com/sarvilin/foodgram-project-react)