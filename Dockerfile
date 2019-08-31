FROM python:3.7.4-stretch

WORKDIR /app

COPY . /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "main.py"]
