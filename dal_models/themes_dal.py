import psycopg2

from db_connection import connection_db


class ThemaDal(object):
    @staticmethod
    def get_methods():
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = f"SELECT * FROM themes;"
                cursor.execute(query)
                data = cursor.fetchall()

                return data

        except Exception as e:
            return e

        finally:
            conn.close()
