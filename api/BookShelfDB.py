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

    def insert(self, author, title, tpages):
        status = "LISTA DE ESPERA" 
        try:
            cursor = self._db.cursor()
            sql_statement = rf"""INSERT into books (author, title, status, total_pages) values ('{author}','{title}','{status}', {tpages})"""
            cursor.execute(sql_statement)
            self._db.commit()
            return 200
        except:
            return 500
        

    def update(self, id, field, value):
        try:
            cursor = self._db.cursor()
            sql_statement = """Update books set {0} = %s where b_id = %s""".format(field)
            cursor.execute(sql_statement, (value, id))
            self._db.commit()
            print("Commited")
            if field == "page":
                self.update_status()    
        except:
            print("Nao rolou")

    def delete(self, id):
        try:
            cursor = self._db.cursor()
            sql_statement = rf"""DELETE FROM books WHERE b_id = {id}"""
            cursor.execute(sql_statement)
            self._db.commit()
            print("Commited")   
        except:
            print("Nao rolou")

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

    def pull_filtered_data(self, where) -> dict:
        try:
            #cursor = self._db.cursor()
            sql_statement = rf"""select * from books where status = '{where}'"""
            #cursor.execute(sql_statement)
            #data = cursor.fetchall()
            data = pd.read_sql_query(sql_statement, self._db)
            return data.to_json(orient='records')
        except:
            return "Error"

    def update_status(self):
        cursor = self._db.cursor()
        sql_statement = """select b_id,page, total_pages from books"""
        cursor.execute(sql_statement)
        data = cursor.fetchall()
        for b in data:
            if b[1] != None and b[0] != b[2]:
                self.update(b[0], "status", "ATIVO")
            elif b[0] == b[2]:
                self.update(b[0], "status", "CONCLUSO")
            else:
                pass

    def endConnection(self):
        self._db.close()
