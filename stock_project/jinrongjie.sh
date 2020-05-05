rm -rf result/jinrongjie.csv
docker run -i --rm --name scrapycontainer_jinrongjie -v /home/cyy/:/usr/src/app -w /usr/src/app/scrapy/jinrongjie  python_scrapy scrapy crawl jinrongjiespider

sleep 50

#python common/sendmail.py result/scrapystockinfo.csv
