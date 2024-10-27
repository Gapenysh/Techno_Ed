import psycopg2
import os
from os import getenv

def connection_db():
    dbname = os.getenv("DB_NAME")
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST")
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        return conn

    except:
        return {"message": "can`t establish connection to database"}