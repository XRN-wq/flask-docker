FROM python:3.9
WORKDIR /parser
COPY . .
RUN pip install requests psycopg2
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "parser.py"]