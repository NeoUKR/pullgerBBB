pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations pullgerAccountManager
python manage.py makemigrations org__bbb
python manage.py makemigrations djTaskBrocker
python manage.py migrate
python manage.py createsuperuser