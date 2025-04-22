# ДЗ 1

Задание - создание Dockerfile from scratch

Сборка контейнера: `docker build -t python-app .`

Запуск контейнера:  

`echo "hello world hello docker" | docker run -i python-app`

или

`docker run -i python-app < input.txt`
