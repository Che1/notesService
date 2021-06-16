### NotesService

Для запуска сервера необходимо поднять MongoDB (для удобства разработки есть docker-compose с mongo)

Отредактировать файл notesService/settings.py - указать в нем нужные параметры авторизации mongoDB
Установть все зависимости: 

`pip install -r requirements.txt`

Провести миграции:

`python manage.py migrate`
