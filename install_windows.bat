pip install -r requirements.txt
python manage.py makemigrations pullgerAccountManager
python manage.py makemigrations com__bbbpip
python manage.py makemigrations djTaskBrocker
python manage.py makemigrations pullgerDataSynchronization
python manage.py migrate
python manage.py createsuperuser