FROM python:3.8-alpine

RUN apk update
COPY . .
COPY requirements.txt .
WORKDIR .

RUN pip install -r requirements.txt

RUN pwd
RUN ls
EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["run.py"]