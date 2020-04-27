rm -rf result/*
docker run -it --rm --name getstocklist -v /home/cyy/:/usr/src/app -w /usr/src/app/tushare python_tushare_pika  python3  get_stock_list.py
sleep 5
#docker run -it --rm --name scrapycontainer -v /home/cyy/scrapy/eastmoney:/usr/src/app -w /usr/src/app  python_scrapy scrapy crawl eastmoneyscore
docker run -it --rm --name scrapycontainer -v /home/cyy/:/usr/src/app -w /usr/src/app/scrapy/eastmoney  python_scrapy scrapy crawl eastmoneyscore &
docker run -it --rm --name scrapycontainer -v /home/cyy/:/usr/src/app -w /usr/src/app/scrapy/stockscrapy  python_scrapy scrapy crawl tonghuashun
#sleep 5
#python3 common/csvctl.py result/eastmoney.csv result/eastmoney_sort.csv 2
sleep 50
python common/sendmail.py result/eastmoney.csv

python common/sendmail.py result/scrapystockinfo.csv