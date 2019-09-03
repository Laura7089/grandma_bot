LABEL maintainer="Laura Duffy"

FROM python:3.7.4-alpine

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

WORKDIR /app
COPY . /app

RUN groupadd -r grandma && useradd --no-log-init -r -g grandma grandma
RUN chown -R grandma:grandma /app

USER grandma
CMD ["python", "main.py"]
