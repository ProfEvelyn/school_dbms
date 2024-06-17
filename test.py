import sqlite3


# Connect to the database (create a new one if it doesn't exist)
def insert():
    conn = sqlite3.connect('t.db')
    cursor = conn.cursor()
    try:

        cursor.execute('''
            CREATE TABLE advisor (
            s_ID VARCHAR(5),
            i_ID VARCHAR(5),
            FOREIGN KEY (s_ID) REFERENCES student(ID) ON DELETE CASCADE ON  UPDATE CASCADE ,
            FOREIGN KEY (i_ID) REFERENCES instructor(ID) ON DELETE CASCADE ON UPDATE CASCADE
        );
        ''')

    except sqlite3.Error as e:

        print(f"SQLITE error: {e}")

    finally:

        cursor.close()
        conn.close()

insert()