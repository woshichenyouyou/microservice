docker-compose -f rabbitmq/docker-compose.yaml up &
sleep 10
path=$(dirname "$PWD")
docker run -it -v $path:/usr/src/app -w /usr/src/app/logserver python_pika python3 log_server_if.py

docker start jenkins_set
