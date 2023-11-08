FROM python:3.10
WORKDIR /home/nosql-api/flask_app/
COPY ./flask_app/ .
RUN pip3 install -r requirements.txt
ENV FLASK_APP=app
CMD ["python3","app.py"]