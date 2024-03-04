import psycopg2
def get_notes_from_db():
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        user='note',
        password='1234',
        dbname='test'
    )
    with conn.cursor() as cursor:
        cursor.execute("""SELECT * FROM notes""")
        all_records=cursor.fetchall()
        print (str(all_records))
        conn.commit()
    conn.close()
    return str(all_records)

def createdb()-> None:
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        user='note',
        password='1234',
        dbname='test'
    )
    with conn.cursor() as cursor:
        cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
	number integer PRIMARY KEY,
	content varchar(1000) NOT NULL) 
        """)
        conn.commit()
    conn.close()

def save_data(number: int, content: str):
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        user='note',
        password='1234',
        dbname='test'
    )
    with conn.cursor() as cursor:
        cursor.execute("""INSERT INTO notes VALUES ((%s),(%s))""", (number, content))
        conn.commit()
    conn.close()

def delete_data(number: int):
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        user='note',
        password='1234',
        dbname='test'
    )
    with conn.cursor() as cursor:
        cursor.execute("""DELETE FROM notes WHERE notes.number=(%s)""", (number, ))
        conn.commit()
    conn.close()



if __name__=='__main__':
    save_data(2, "что-то")
    delete_data(3)