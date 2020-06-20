rm -rf result/liaogu.csv
path=$(dirname "$PWD")
docker run -i --rm --name scrapycontainer_liaogu -v $path:/usr/src/app -w /usr/src/app/scrapy/liaogu  python_scrapy_splash  scrapy crawl liaogu_spider
#sleep 50

#python common/sendmail.py result/scrapystockinfo.csv
