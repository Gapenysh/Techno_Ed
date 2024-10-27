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
                stmt_select = """SELECT id FROM themes WHERE name = %s"""
                cursor.execute(stmt_select, name)
                id = cursor.fetchone()
                query = f"UPDATE users SET theme_id = %s"
                cursor.execute(query, (id,))

                conn.commit()

                return True

        except Exception as e:
            print(str(e))

            return False

        finally:
            conn.close()

    @staticmethod
    def add_resume(pdf_file):
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """UPDATE users SET resume = %s"""
                cur.execute(stmt, (pdf_file,))
                conn.commit()
            return True
        except Exception as e:
            print(str(e))
            return False
        finally:
            conn.close()