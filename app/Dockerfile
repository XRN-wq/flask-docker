FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install psycopg2 flask
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3", "flask_app.py"]