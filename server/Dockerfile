FROM python:3-alpine

RUN apk add --no-cache build-base openssl-dev libffi-dev
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install pipenv
RUN pipenv install --deploy --system

EXPOSE 8080

RUN python build_database.py

ENTRYPOINT ["python3"]

CMD ["-m", "openapi_server"]