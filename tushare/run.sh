docker build -t python/tushare1 .
docker run -it --rm --name helloworld.py -v /home/cyy/tushare:/usr/src/app -w /usr/src/app python/tushare1  python3  helloworld.py
