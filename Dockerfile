FROM python:3.12.1

WORKDIR /var/app

COPY ./requirements.txt ./requirements.txt

COPY ./app /var/app/

COPY ./.env /var/.env

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uwsgi", "--socket", "0.0.0.0:8000", "--protocol=http", "-w", "run:app"]
