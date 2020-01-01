FROM python:3.7.6-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 --default-timeout=100 install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

#COPY . .

#CMD [ "python", "./helloworld.py" ]
