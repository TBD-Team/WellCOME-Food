install:
	pip install -r requirements.txt

docker-build:
	sudo docker build --tag backend_web:latest .

migrate:
	sudo docker exec -it backend_web_1 python manage.py migrate
