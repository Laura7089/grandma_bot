FROM python:3.7.4-alpine

LABEL maintainer="Laura Duffy"

WORKDIR /app
COPY . /app

RUN addgroup -S grandma && adduser -S grandma -G grandma
RUN chown -R grandma:grandma /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

USER grandma
CMD ["python", "main.py"]
