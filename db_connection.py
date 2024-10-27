import psycopg2


def connection_db():
    dbname = 'telegram_hack'
    user = 'postgres'
    password = 'Ferry2431!'
    host = 'localhost'
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        return conn

    except:
        return {"message": "can`t establish connection to database"}