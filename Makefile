migration: 
	python manage.py migrate

create_superuser:
	export DJANGO_SUPERUSER_PASSWORD=password
# ifeq ($(IS_USER_EXISTS), False)
# 	$(python manage.py createsuperuser --no-input --username admin --email dmitri.sherbak@gmail.com)
# endif

runserver: migration
	python manage.py runserver 0.0.0.0:8000