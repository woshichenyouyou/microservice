rm -rf result/scrapystockinfo.csv
docker run -i --rm --name scrapycontainer -v /home/cyy/:/usr/src/app -w /usr/src/app/scrapy/stockscrapy  python_scrapy scrapy crawl tonghuashun
sleep 50

python common/sendmail.py result/scrapystockinfo.csv
