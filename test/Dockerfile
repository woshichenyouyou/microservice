FROM python:3.7.7-alpine
WORKDIR /usr/src/app
RUN apk add postgresql-dev
COPY requirements.txt ./
RUN pip3 --default-timeout=100 install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

#COPY . .

#CMD [ "python", "./helloworld.py" ]
