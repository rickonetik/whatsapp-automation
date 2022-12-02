FROM python3

WORKDIR /app

COPY . . 

CMD [ "python3", "main.py" ]