


docker run -it --rm --name scrapycontainer -v /home/microservice/:/usr/src/app -w /usr/src/app/scrapy/  python_scrapy scrapy startproject tonghuashun
docker run -it --rm --name scrapycontainer -v /home/microservice/:/usr/src/app -w /usr/src/app/scrapy/tonghuashun  python_scrapy scrapy genspider tonghuashun http://doctor.10jqka.com.cn/



docker build -t python/scrapy1 .
docker run -it --rm --name scrapycontainer -v /home/cyy/:/usr/src/app -w /usr/src/app/scrapy/eastmoney  python_scrapy scrapy crawl eastmoneyscore
docker run -it -v /home/cyy:/usr/src/app -w /usr/src/app/scrapy python_pika python3 stock_list.py
docker run -it --rm --name scrapycontainer -v /home/cyy/:/usr/src/app -w /usr/src/app/scrapy/stockscrapy  python_scrapy scrapy crawl tonghuashun
docker run -it --rm --name scrapycontainer -v /home/cyy/:/usr/src/app -w /usr/src/app/scrapy/jinrongjie  python_scrapy scrapy crawl jinrongjiespider
docker run -it --rm --name scrapycontainer -v /home/cyy/:/usr/src/app -w /usr/src/app/scrapy/jinrongjie_score  python_scrapy scrapy crawl jinrongjiespider
docker run -it --rm --name scrapycontainer -v /home/cyy/:/usr/src/app -w /usr/src/app/scrapy/dazhihui_xiaozhi  python_scrapy1 scrapy crawl dazhihui
