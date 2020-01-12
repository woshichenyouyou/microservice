#FROM python:3.7.6-buster
FROM rabbitmq:3.8-rc-management-alpine
WORKDIR /usr/src/app
tar -xvf Python-3.7.6.tgz
mkdir /usr/src/
mv Python-3.7.6 /usr/src/

apk add build-base

tar -xvf Python-3.7.6.tgz

COPY requirements.txt ./
RUN pip3 --default-timeout=100 install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

#COPY . .

#CMD [ "python", "./helloworld.py" ]
