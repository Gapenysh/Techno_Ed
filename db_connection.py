import psycopg2


def connection_db():
    dbname = ''
    user = ''
    password = ''
    host = ''
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        return conn
    except:
        return {"message": "can`t establish connection to database"}