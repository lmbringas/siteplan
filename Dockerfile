FROM python:3.7.3-alpine3.10

RUN apk add --update \ 
    python-dev \
    build-base \
    linux-headers \
    pcre-dev \
    py-pip \
    jpeg-dev \
    zlib-dev \
    build-base \
    gcc \
    abuild \
    binutils \
    linux-headers \
    make \
    musl-dev \
    python-dev \
    g++ \
    freetype-dev

ADD requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

EXPOSE 8000
COPY . /app/website/
WORKDIR /app/website/

RUN python manage.py makemigrations
RUN python manage.py migrate 

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
