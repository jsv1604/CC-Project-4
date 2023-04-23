# Follow Task-0 subtask-1

FROM python:3.8-alpine

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add --update 

RUN pip3 install --upgrade pip  

RUN pip3 install -r requirements.txt 

RUN rm -rf /var/cache/apk/*

COPY ./app /app

CMD ["python", "app.py"]