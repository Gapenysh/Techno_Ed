from db_connection import connection_db

class VacansyDAL:

    @staticmethod
    def get_vacansy():
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt="""SELECT * FROM vacansy"""
                cur.execute(stmt)
                result = cur.fetchall()
            return result
        except Exception as e:
            return e
        finally:
            conn.close()
    @staticmethod
    def get_intership():
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """SELECT * FROM intership"""
                cur.execute(stmt)
                result = cur.fetchall()
            return result
        except Exception as e:
            return e
        finally:
            conn.close()

    @staticmethod
    def pick_vacansy(id):
        pass


    