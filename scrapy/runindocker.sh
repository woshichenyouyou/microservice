docker build -t python/scrapy1 .
docker run -it --rm --name scrapycontainer -v /home/cyy/scrapy/eastmoney:/usr/src/app -w /usr/src/app  python_scrapy scrapy crawl eastmoneyscore
docker run -it -v /home/cyy:/usr/src/app -w /usr/src/app/scrapy python_pika python3 stock_list.py
