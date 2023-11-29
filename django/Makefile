migration: 
	python manage.py migrate

collect_static: 
	python manage.py collectstatic --no-input

rungunicorn:
	gunicorn gdsite.wsgi:application --bind 0.0.0.0:8000

create_superuser:
	export DJANGO_SUPERUSER_PASSWORD=password
# ifeq ($(IS_USER_EXISTS), False)
# 	$(python manage.py createsuperuser --no-input --username admin --email dmitri.sherbak@gmail.com)
# endif

runserver: migration rungunicorn
	python manage.py runserver 0.0.0.0:8000