release: python manage.py migrate --noinput
release: python manage.py loaddata db.json
web: gunicorn pypro.wsgi --log-file -