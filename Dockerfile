FROM python:3.12-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

# WSGIサーバー（Gunicorn）でアプリを起動
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
