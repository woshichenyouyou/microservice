docker build -t python_flask .
docker run -it -p 5000:5000 -v /home/cyy:/usr/src/app -w /usr/src/app/flask python_flask python3 app.py

