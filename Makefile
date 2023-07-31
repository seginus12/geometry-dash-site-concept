migration: 
	python manage.py migrate

creating_superuser:
	export DJANGO_SUPERUSER_PASSWORD=password
	IS_USER_EXISTS=$(python is_user_exists.py admin)
	echo $(IS_USER_EXISTS)
ifeq ($(IS_USER_EXISTS), False)
	$(python manage.py createsuperuser --no-input --username admin --email dmitri.sherbak@gmail.com)
endif

start: migration creating_superuser
	python manage.py runserver 0.0.0.0:8000
