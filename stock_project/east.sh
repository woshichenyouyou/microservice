rm -rf result/eastmoney.csv
path=$(dirname "$PWD")
docker run -i --rm --name scrapy_east_container -v $path:/usr/src/app -w /usr/src/app/scrapy/eastmoney  python_scrapy scrapy crawl eastmoneyscore
sleep 50
python common/sendmail.py result/eastmoney.csv
