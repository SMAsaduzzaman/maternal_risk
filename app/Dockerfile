FROM tiangolo/uwsgi-nginx-flask:python3.10

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ENV ENVIRONMENT production

COPY . .

EXPOSE 80/tcp

#CMD [ "python", "main.py""]