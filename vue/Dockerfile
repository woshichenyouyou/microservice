FROM ubuntu:latest
RUN apt-get update -y && \
    apt-get dist-upgrade -y && \
    apt-get autoremove -y && \
    apt-get clean -y

RUN apt-get -y install curl

RUN curl --silent --location https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get install nodejs -y

RUN npm install -g cnpm --registry=https://registry.npm.taobao.org && \
    cnpm  install -g @vue/cli

WORKDIR /root/app

#ENTRYPOINT ["npm", "start"]
