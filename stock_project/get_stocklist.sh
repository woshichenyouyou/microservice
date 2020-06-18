path=$(dirname "$PWD")
docker run -i --rm --name getstocklist -v $path:/usr/src/app -w /usr/src/app/tushare python_tushare_pika  python3  get_stock_list.py
