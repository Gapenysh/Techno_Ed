import psycopg2

from db_connection import connection_db


class UserDal(object):
    @staticmethod
    def get_user_info(telegram_id):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = f"SELECT * FROM users WHERE telegram_id = %s::text;"
                cursor.execute(query, (telegram_id,))
                user_info = cursor.fetchone()

                return user_info

        except Exception as e:
            return e

        finally:
            conn.close()

    @staticmethod
    def edit_user_theme(name):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = f"SELECT * FROM users WHERE telegram_id = %s::text;"
                cursor.execute(query, (telegram_id,))
                user_info = cursor.fetchone()

                return user_info

        except Exception as e:
            return e

        finally:
            conn.close()