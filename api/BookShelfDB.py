#Set your own config
from api.config import HOST, DATABASE, USER, UPASS
import psycopg2
import pandas as pd

### Might change its name
class BookDB:
    def __init__(self):
        self._db = psycopg2.connect(
            host=HOST,
            database=DATABASE,
            user=USER,
            password=UPASS
        )

    def insert(self, author, title):
        status = "LISTA DE ESPERA" 
        try:
            cursor = self._db.cursor()
            sql_statement = f"""INSERT into books values ({author},{title},{status})"""
            cursor.execute(sql_statement)
            self._db.commit()
            return 200
        except:
            return 500
        

    def pull_all_data(self) -> dict:
        try:
            #cursor = self._db.cursor()
            sql_statement = """select * from books"""
            #cursor.execute(sql_statement)
            #data = cursor.fetchall()
            data = pd.read_sql_query(sql_statement, self._db)
            return data.to_json(orient='records')
        except:
            return "Error"
        

    def endConnection(self):
        self._db.close()
