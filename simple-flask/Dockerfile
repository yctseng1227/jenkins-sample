FROM python:3.9-alpine
MAINTAINER yctseng

COPY . /app
WORKDIR /app
ENV FLASK_APP=/app/autoapp.py

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]