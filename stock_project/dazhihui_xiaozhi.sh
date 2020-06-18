rm -rf result/dazhihui.csv
path=$(dirname "$PWD")

docker run -i --rm --name scrapycontainer_dazhihui -v $path:/usr/src/app -w /usr/src/app/scrapy/dazhihui_xiaozhi  python_scrapy scrapy crawl dazhihui
sleep 50

#python common/sendmail.py result/scrapystockinfo.csv
