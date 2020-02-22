docker-compose -f rabbitmq/docker-compose.yaml up &

docker run -it -v /home/cyy:/usr/src/app -w /usr/src/app/logserver python_pika python3 log_server_if.py
