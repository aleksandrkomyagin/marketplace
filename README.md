## Тестовое задание на позицию Junior Python Разработчик

<div align=center>

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-4.1-blue)
![Django_REST_framework](https://img.shields.io/badge/Django_REST_framework-3.14.0-blue)
</div>

### Задача:

Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
* Django Модель Item с полями (name, description, price)
* API с двумя методами:
    * GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
	* GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

### Бонусные задачи:
* Запуск используя Docker
* Использование environment variables
* Просмотр Django Моделей в Django Admin панели

### Ресурсы API

* Ресурс **items/**: список товаров
* Ресурс **items/get/{id}**: получить конкретный товар
* Ресурс **items/buy/{id}**: покупка товара

<details>
  <summary>
    <h2>Запуск проекта на локальном сервере</h2>
  </summary>

> Для MacOs и Linux вместо python использовать python3

1. Клонировать репозиторий.
   ```
       $ git clone git@github.com:aleksandrkomyagin/marketplace.git
   ```
2. Создать и активировать виртуальное окружение.
   ```
       $ py -3.11 -m venv venv
   ```
   Для Windows:
   ```
       $ source venv/Scripts/activate
   ```
   Для MacOs/Linux:
   ```
       $ source venv/bin/activate
   ```
2. Запустить docker-compose из дирректории backend.Перед запуском в корне проекта создать файл .env, по шаблону(в корне проекта файл .env.example).
    ```
        $ docker-compose up --build
    ```
3. Создать суперпользователя.
    ```
        $ docker-compose exec backend python manage.py createsuperuser
    ```
- После выполнения вышеперечисленных инструкций бэкенд проекта будет доступен по адресу http://127.0.0.1:8000/

</details>

## Контакты
<div align=center>

[![Telegram Badge](https://img.shields.io/badge/-aleksandrkomyagin8-blue?style=social&logo=telegram&link=https://t.me/aleksandrkomyagin8)](https://t.me/aleksandrkomyagin8) [![Gmail Badge](https://img.shields.io/badge/-aleksandrkomyagin8@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:aleksandrkomyagin8@gmail.com)](mailto:aleksandrkomyagin8@gmail.com)

</div>