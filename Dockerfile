FROM python:3.12.7

RUN apt-get update

RUN groupadd -g 1945 infotek && useradd -u 1945 -g infotek -s /bin/sh infotek

# RUN mkdir -p /data

RUN mkdir -p /code

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src/app /code/app

RUN chown -R infotek.infotek /code/app
USER infotek

EXPOSE 8001

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
