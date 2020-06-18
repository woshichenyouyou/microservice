rm -rf result/jinrongjie.csv
path=$(dirname "$PWD")
docker run -i --rm --name scrapycontainer_jinrongjie -v $path:/usr/src/app -w /usr/src/app/scrapy/jinrongjie  python_scrapy scrapy crawl jinrongjiespider

sleep 50

#python common/sendmail.py result/scrapystockinfo.csv
