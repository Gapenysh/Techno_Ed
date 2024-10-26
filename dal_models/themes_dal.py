import psycopg2

from db_connection import connection_db


class ThemaDal(object):
    @staticmethod
    def get_themes():
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

    @staticmethod
    def get_theme_info(theme_id: int):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = f"SELECT * FROM themes WHERE id = %s;"
                cursor.execute(query, (theme_id,))
                data = cursor.fetchone()

                return data

        except Exception as e:
            return e

        finally:
            conn.close()

    @staticmethod
    def get_courses_by_theme_and_level(theme_id: int, level_id: int):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = f"SELECT id, name FROM course WHERE theme_id = %s and level_id = %s;"
                cursor.execute(query, (theme_id, level_id))
                data = cursor.fetchall()

                return data

        except Exception as e:
            return e

        finally:
            conn.close()
