import sqlite3 
class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute('''CREATE TABALE IF NIO EXISTS shop (id integer PRIMARY KEY,
                         name text , buy text , sell text , number text) ''')
        self.cur.commit()

    def insert(self,name,buy,sell,number):
        self.cur.execute('''INSERT INTO shop VALUES (NULL,?,?,?,?),(name,buy,sell,number) ''')
        self.con.commit()
        print('record inserted')

    def fetch(self):
        self.cur.execute('''SELECT * FROM shop''')
        rows = self.cur.fetchall()
        return rows
    
    def remove(self,id):
        self.cur.execute("DELETE FROM shop WHER ID = ?",[id])

    def update(self.id,name,buy,sell,number):
        self.cur.execute('UPDATE shop SET name = ?,buy = ? ,sell =? ,number =? , where id = ? ', (name,buy,sell,number))
        self.commit()
    

