# My Page

Тестовое приложение, содержащее набор сервисов, отображающее список знаков зодиака и выводящее информацию о них, созданное для ознакомления с Django Framework.

## Quickstart

Run the following commands to bootstrap your environment:
    
    pip install virtualenv
    git clone https://github.com/niksergs/Learning_Django_Project
    cd my_page

    python -m venv venv
    venv/Scripts/activate.bat
    pip install -r requirements.txt

Run the app locally:

    python manage.py runserver 0.0.0.0:8000

Run the app with gunicorn:

    pip install gunicorn
    gunicorn my_page.wsgi:application -b 0.0.0.0:8000
    
