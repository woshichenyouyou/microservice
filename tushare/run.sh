docker build -t python/tushare1 .
docker run -it --rm --name getstocklist -v /home/cyy/:/usr/src/app -w /usr/src/app/tushare python_tushare_pika  python3  get_stock_list.py
