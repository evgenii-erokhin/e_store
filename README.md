# Интернет магазин одежды.
Это учебный проект интернет магазина в котором реализовано слкдующие:    
Для покупателя:
+ регистрация в интернет магазине
+ выбор товара и добавление в карзину
+ оплата покупок удобным способом

Для сотрудника магазина:   
+ добавления новго товара через админ панель
+ 

Проект реализован на Class Base Views

Попробовал использовать планировщик асинхроных задач Celery
 ## Технологии

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)
 ## Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:
  ```
  git clone git@github.com:evgenii-erokhin/e_store.git
  ```
  ```
  cd e_store
  ```
2. Cоздать и активировать виртуальное окружение:

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
3. Установоить зависимости:
```
pip install -r requirements.txt
```
4. Перейти в дерикторию `yatube` выполнить миграции и создать супер-пользователя:
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
5. Запустить сервер разработки:
```
python manage.py runserver
```
### Автор
**Евгений Ерохин**
<br>

<a href="https://t.me/juandart" target="_blank">
<img src=https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white />
</a>
<a href="mailto:evgeniierokhin@proton.me?">
<img src=https://img.shields.io/badge/ProtonMail-8B89CC?style=for-the-badge&logo=protonmail&logoColor=white />
</a>

