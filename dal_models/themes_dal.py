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

    @staticmethod
    def create_answer(question_id, user_id, answer):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = f"INSERT INTO answers (question_id, answer, user_id) values (%s, %s, %s) returning id"
                cursor.execute(query, (question_id, answer, user_id))
                data = cursor.fetchone()
                conn.commit()

                return data

        except Exception as e:
            return e

        finally:
            conn.close()

    @staticmethod
    def get_all_questions_theme():
        conn = connection_db()

        try:
            with conn.cursor() as cur:
                stmt = f"""SELECT * FROM questions WHERE flag = 'themes' """
                cur.execute(stmt)
                result = cur.fetchall()
            return result
        except Exception as e:
            return e
        finally:
            conn.close()

    @staticmethod
    def get_quest_and_answer(user_id: int):
        conn = connection_db()

        try:
            with conn.cursor() as cur:
                stmt = f"""SELECT quest, answer FROM answers
                           INNER JOIN questions ON answers.question_id = questions.id
                           WHERE user_id = %s """
                cur.execute(stmt, (user_id,))

                result = cur.fetchall()
            return result

        except Exception as e:
            return e
        finally:
            conn.close()