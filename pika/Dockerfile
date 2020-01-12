#FROM python:3.7.6-buster
FROM python:3.7.6-slim
WORKDIR /usr/src/app
COPY sources.list /etc/apt/
VOLUME ["/home/cyy/pika", "/usr/src/app"]
RUN apt-get install erlang-nox -y && \
    apt-get install rabbitmq-server -y
COPY requirements.txt ./
RUN pip3 --default-timeout=100 install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

#COPY . .

#CMD [ "python", "./helloworld.py" ]
