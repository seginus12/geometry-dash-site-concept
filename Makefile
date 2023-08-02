migration: 
	python manage.py migrate

creating_superuser:
	export DJANGO_SUPERUSER_PASSWORD=password
# ifeq ($(IS_USER_EXISTS), False)
# 	$(python manage.py createsuperuser --no-input --username admin --email dmitri.sherbak@gmail.com)
# endif

tesing:
	python manage.py test gd

start: migration creating_superuser tesing
	python manage.py runserver 0.0.0.0:8000
