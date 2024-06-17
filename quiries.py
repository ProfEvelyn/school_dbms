import sqlite3


# Connect to the database (create a new one if it doesn't exist)
def createtABLES():
    conn = sqlite3.connect('test3.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS department (
            dept_name VARCHAR(20),
            building VARCHAR(8),
            budget NUMERIC(12,2),
            PRIMARY KEY (dept_name)
                );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS advisor (
            s_ID VARCHAR(5),
            i_ID VARCHAR(5),
            FOREIGN KEY (s_ID) REFERENCES student(ID) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (i_ID) REFERENCES instructor(ID) ON DELETE CASCADE ON UPDATE CASCADE
        );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS classroom (
            building VARCHAR(8),
            room_number NUMERIC(3,0),
            capacity NUMERIC(3,0),
            PRIMARY KEY (building, room_number)
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS course (
            course_id VARCHAR(7),
            title VARCHAR(50),
            dept_name VARCHAR(20),
            credits NUMERIC(2, 0),
            PRIMARY KEY (course_id),
            FOREIGN KEY (dept_name) REFERENCES department(dept_name)
        );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS instructor(
            ID VARCHAR(5),
            name VARCHAR(20),
            dept_name VARCHAR(20),
            salary NUMERIC(8,2),
            PRIMARY KEY (ID),
            FOREIGN KEY (dept_name) REFERENCES department(dept_name) ON DELETE CASCADE ON UPDATE CASCADE
        
        );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prereq (
            course_id VARCHAR(7),
            prereq_id VARCHAR(7),
            PRIMARY KEY (course_id, prereq_id),
            FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (prereq_id) REFERENCES course(course_id) ON DELETE CASCADE ON UPDATE CASCADE
        );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS section (
            course_id VARCHAR(7),
            sec_id VARCHAR(8),
            semester VARCHAR(6),
            year NUMERIC(4,0),
            building VARCHAR(8),
            room_number NUMERIC(3,0),
            time_slot_id VARCHAR(10),
            PRIMARY KEY (course_id, sec_id, semester, year),
            FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (building, room_number) REFERENCES classroom(building, room_number) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (time_slot_id) REFERENCES time_slot(time_slot_id) ON DELETE CASCADE ON UPDATE CASCADE
        );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS student (
            ID VARCHAR(5),
            name VARCHAR(20),
            dept_name VARCHAR(20),
            tot_cred NUMERIC(4,0),
            PRIMARY KEY (ID),
            FOREIGN KEY (dept_name) REFERENCES department(dept_name) ON DELETE CASCADE ON UPDATE CASCADE
        );
        
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS takes (
            ID VARCHAR(5),
            course_id VARCHAR(7),
            sec_id VARCHAR(8),
            semester VARCHAR(6),
            year NUMERIC(4,0),
            grade VARCHAR(15),
            PRIMARY KEY (ID, course_id, sec_id, semester, year),
            FOREIGN KEY (ID) REFERENCES student(ID) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (course_id, sec_id, semester, year) REFERENCES section(course_id, sec_id, semester, year) ON DELETE CASCADE ON UPDATE CASCADE
        );
        
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS teaches (
            ID VARCHAR(5),
            course_id VARCHAR(7),
            sec_id VARCHAR(8),
            semester VARCHAR(6),
            year NUMERIC(4,0),
            PRIMARY KEY (ID, course_id, sec_id, semester, year),
            FOREIGN KEY (ID) REFERENCES instructor(ID) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (course_id, sec_id, semester, year) REFERENCES section(course_id, sec_id, semester, year) ON DELETE CASCADE ON UPDATE CASCADE
        );
        
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS time_slot (
            time_slot_id VARCHAR(10),
            day VARCHAR(10),
            start_time VARCHAR(8),
            end_time VARCHAR(8),
            PRIMARY KEY (time_slot_id)
        );
        ''')
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False

    finally:
        conn.commit()
        conn.close()

createtABLES()