rm -rf result/dazhihui.csv
docker run -i --rm --name scrapycontainer_dazhihui -v /home/cyy/:/usr/src/app -w /usr/src/app/scrapy/dazhihui_xiaozhi  python_scrapy1 scrapy crawl dazhihui
sleep 50

#python common/sendmail.py result/scrapystockinfo.csv
