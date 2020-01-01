docker build -t python/scrapy1 .
docker run -it --rm --name scrapycontainer -v /home/cyy/scrapy/eastmoney:/usr/src/app -w /usr/src/app  python/scrapy1 scrapy crawl eastmoneyscore
