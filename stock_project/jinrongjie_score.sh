rm -rf result/jinrongjie_score.csv
path=$(dirname "$PWD")
docker run -i --rm --name scrapycontainer_jinrongjie_score -v $path:/usr/src/app -w /usr/src/app/scrapy/jinrongjie_score  python_scrapy scrapy crawl jinrongjiespider
sleep 50

#python common/sendmail.py result/scrapystockinfo.csv
