# Subir cambios cuidando que primero vayan los tests
# test para users
# readme con doc para correr
# diagrama de modelo
# swagger
# postman con coleccion
makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

create-superuser:
	python manage.py createsuperuser

shell-plus:
	python manage.py shell_plus

runserver:
	python manage.py runserver

coverage-run:
	coverage run --source='.' manage.py test

coverage-report:
	coverage report --omit='*migrations*' --skip-covered

model-diagram:
	python manage.py graph_models -a > models-diagram.dot