mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
run:
	python3 manage.py runserver 127.0.0.1:8000
create:
	python3 manage.py createsuperuser
