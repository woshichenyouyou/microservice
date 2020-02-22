docker run -it -v `pwd`:/root/app/ -w /root/app python_pika python producer.py info
docker exec -it festive_hertz /bin/bash
docker run -it -v /home/cyy:/usr/src/app -w /usr/src/app/test python_pika python3 test_locallog.py

