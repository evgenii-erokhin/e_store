# Интернет магазин одежды.
Это учебный проект интернет магазина в котором реализовано следующее:    
Для покупателя:
+ регистрация в интернет магазине
+ выбор товара и добавление в карзину
+ оплата покупок удобным способом

Для сотрудника магазина:   
+ добавления новго товара через админ панель
+ 

Планирую применить в проекте:
+ планировщик асинхроных задач Celery
+ подключение БД Postgres
+ переписать проект на Class Based Views
+ Отправку электронных писем для подтверждения электронной почты
+ подключить авторизацию OAuth 2.0
+ Написать тесты для проекта
+ Подключения оплаты к заказам Stripe
+ 

 ## Технологии

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
 ## Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:
  ```
  git clone git@github.com:evgenii-erokhin/e_store.git
  ```
  ```
  cd e_store
  ```
2. В корне проекта создать файл .env по следуюзему образцу:
   ```
   NAME=store_db
   USER=stor_username
   PASSWORD=passw0rd1
   HOST=localhost
   PORT=5432
   
   EMAIL_BACKEND=smtp.yandex.ru
   EMAIL_PORT=465
   EMAIL_HOST_USER=your_email
   EMAIL_HOST_PASSWORD=password_of_your_app
   EMAIL_USE_SSL=True
   ```
3. Cоздать и активировать виртуальное окружение:

* Если у вас **Windows**:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
* Если у вас **Linux** или **macOS**:
```
python3 -m venv venv
```
```
source venv/bib/activate
```
4. Установоить зависимости:
```
pip install -r requirements.txt
```
5. Перейти в дерикторию `yatube` выполнить миграции и создать супер-пользователя:
```
cd store
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
6. Запустить сервер разработки:
```
python manage.py runserver
```
### Автор
**Евгений Ерохин**
<br>

<a href="https://t.me/juandart" target="_blank">
<img src=https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white />
</a>
<a href="mailto:evgeniy_erokhin@outlook.com?">
<img src=https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white/>
</a>

