FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
#EXPOSE 5000

#CMD python3 app.py
ENTRYPOINT FLASK_APP=app.py flask run --host=0.0.0.0