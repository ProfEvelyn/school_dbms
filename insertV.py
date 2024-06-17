import sqlite3

# Connect to the database

def insert():
    conn = sqlite3.connect('test3.db')
    cursor = conn.cursor()

    # Insert values into the advisor table
    try:
        values_to_insert = [
            ('23121', '32343'),
            ('44553', '33456'),
            ('45678', '83821'),
            ('54321', '10101'),
            ('55739', '15151'),
            ('76543', '10101'),
            ('76653', '98345'),
            ('98765', '83821'),
            ('98988', '98345'),
            ('11111', '55555'),
            ('11112', '66666'),
            ('11113', '77777'),
            ('11114', '88888'),
        ]

        cursor.executemany("INSERT INTO advisor (s_ID, i_ID) VALUES (?, ?)", values_to_insert)

        values_to_insert = [
            ('Taylor', 101, 50),
            ('Taylor', 3128, 30),
            ('Packard', 101, 60),
            ('Watson', 100, 40),
            ('Painter', 514, 70),
        ]
        cursor.executemany("INSERT INTO classroom (building, room_number, capacity) VALUES (?, ?, ?)", values_to_insert)

        # Insert values into the course table
        values_to_insert = [
            ('BIO-101', 'Intro to Biology', 'Biology', 4),
            ('BIO-301', 'Genetics', 'Biology', 4),
            ('BIO-399', 'Computational Biology', 'Biology', 3),
            ('CS-101', 'Intro to Computer Science', 'Comp.Sci', 4),
            ('CS-190', 'Game Design', 'Comp.Sci', 4),
            ('CS-315', 'Robotics', 'Comp.Sci', 3),
            ('CS-319', 'Image Processing', 'Comp.Sci', 3),
            ('CS-347', 'Database System Concepts', 'Comp.Sci', 3),
            ('EE-181', 'Intro to Digital Systems', 'Elec.Eng', 3),
            ('FIN-201', 'Investment Banking', 'Finance', 3),
            ('HIS-351', 'World History', 'History', 3),
            ('MU-199', 'Music Video Production', 'Music', 3),
            ('PHY-101', 'Physical Principles', 'Physics', 4),
            ('COMP217', 'Data Structures', 'Comp.Sci', 3),
            ('COMP124', 'Computer Programming', 'Comp.Sci', 3),
        ]

        cursor.executemany("INSERT INTO course (course_id, title, dept_name, credits) VALUES (?, ?, ?, ?)", values_to_insert)

        # Insert values into the department table
        values_to_insert = [
            ('Comp.Sci', 'Taylor', 100000),
            ('Biology', 'Watson', 90000),
            ('Elec.Eng', 'Taylor', 85000),
            ('Music', 'Packard', 80000),
            ('Finance', 'Painter', 120000),
            ('History', 'Painter', 50000),
            ('Physics', 'Watson', 70000),
        ]

        cursor.executemany("INSERT INTO department (dept_name, building, budget) VALUES (?, ?, ?)", values_to_insert)

        values_to_insert = [
            ('22222', 'Einstein', 'Physics', 95000),
            ('12121', 'Wu', 'Finance', 90000),
            ('32343', 'El Said', 'History', 60000),
            ('45565', 'Soydan Redif', 'Comp.Sci', 75000),
            ('98345', 'Kim', 'Elec.Eng', 80000),
            ('76766', 'Crick', 'Biology', 72000),
            ('10101', 'Srinivasan', 'Comp.Sci', 65000),
            ('58583', 'Califieri', 'History', 62000),
            ('83821', 'Ferhun Yorganciglu', 'Comp.Sci', 92000),
            ('15151', 'Mozart', 'Music', 40000),
            ('33456', 'Gold', 'Physics', 87000),
            ('76543', 'Singh', 'Finance', 80000),
            ('55555', 'Yonal Kirsal', 'Comp.Sci', 95000),
            ('66666', 'Samet Biricik', 'Comp.Sci', 90000),
            ('77777', 'Cem Kalyoncu', 'Comp.Sci', 85000),
            ('88888', 'Zafer Erenel', 'Comp.Sci', 82000),
        ]

        cursor.executemany("INSERT INTO instructor (ID, name, dept_name, salary) VALUES (?, ?, ?, ?)", values_to_insert)

        # Insert values into the prereq table
        values_to_insert = [
            ('BIO-301', 'BIO-101'),
            ('BIO-399', 'BIO-101'),
            ('CS-190', 'CS-101'),
            ('CS-315', 'CS-101'),
            ('CS-319', 'CS-101'),
            ('CS-347', 'CS-101'),
            ('EE-181', 'PHY-101'),
        ]

        cursor.executemany("INSERT INTO prereq (course_id, prereq_id) VALUES (?, ?)", values_to_insert)

        # Insert values into the section table
        values_to_insert = [
            ('BIO-101', 1, 'Summer', 2023, 'Painter', 514, 'B'),
            ('BIO-301', 1, 'Summer', 2023, 'Painter', 514, 'A'),
            ('CS-101', 1, 'Fall', 2023, 'Packard', 101, 'H'),
            ('CS-101', 1, 'Spring', 2023, 'Packard', 101, 'F'),
            ('CS-190', 1, 'Spring', 2023, 'Taylor', 3128, 'E'),
            ('CS-190', 2, 'Spring', 2023, 'Taylor', 3128, 'A'),
            ('CS-315', 1, 'Spring', 2023, 'Watson', 120, 'D'),
            ('CS-319', 1, 'Spring', 2023, 'Watson', 100, 'B'),
            ('CS-319', 2, 'Spring', 2023, 'Taylor', 3128, 'C'),
            ('CS-347', 1, 'Fall', 2023, 'Taylor', 3128, 'A'),
            ('EE-181', 1, 'Spring', 2023, 'Taylor', 3128, 'C'),
            ('FIN-201', 1, 'Spring', 2023, 'Packard', 101, 'B'),
            ('HIS-351', 1, 'Spring', 2023, 'Painter', 514, 'C'),
            ('COMP217', 1, 'Spring', 2023, 'Packard', 101, 'D'),
            ('COMP124', 1, 'Fall', 2023, 'Watson', 100, 'A'),
        ]

        cursor.executemany("INSERT INTO section (course_id, sec_id, semester, year, building, room_number, time_slot_id) VALUES (?, ?, ?, ?, ?, ?, ?)", values_to_insert)

        # Insert values into the student table
        values_to_insert = [
            ('00128', 'Zhang', 'Comp.Sci', 102),
            ('12345', 'Shankar', 'Comp.Sci', 32),
            ('19991', 'Brandt', 'History', 80),
            ('23121', 'Chavez', 'Finance', 110),
            ('44553', 'Peltier', 'Physics', 56),
            ('45678', 'Levy', 'Physics', 46),
            ('54321', 'Williams', 'Comp.Sci', 54),
            ('55739', 'Sanchez', 'Music', 38),
            ('70557', 'Snow', 'Physics', 0),
            ('76543', 'Brown', 'Comp.Sci', 58),
            ('76653', 'Aoi', 'Elec.Eng', 60),
            ('98765', 'Bourikas', 'Elec.Eng', 98),
            ('98988', 'Tanaka', 'Biology', 120),
            ('11111', 'Lee', 'Comp.Sci', 70),
            ('22222', 'Garcia', 'Comp.Sci', 80),
            ('33333', 'Smith', 'Comp.Sci', 90),
            ('44444', 'Jones', 'Comp.Sci', 100),
            ('66666', 'Martinez', 'Finance', 120),
            ('77777', 'Rodriguez', 'Finance', 130),
            ('88888', 'Brown', 'Finance', 140),
            ('99999', 'Hernandez', 'Finance', 150),
            ('10101', 'Johnson', 'Finance', 160),
        ]

        cursor.executemany("INSERT INTO student (ID, name, dept_name, tot_cred) VALUES (?, ?, ?, ?)", values_to_insert)


        # Insert values into the takes table
        values_to_insert = [
            ('00128', 'CS-101', 1, 'Fall', 2023, 'A'),
            ('00128', 'CS-347', 1, 'Fall', 2023, 'A'),
            ('11111', 'COMP217', 1, 'Fall', 2023, 'A'),
            ('00128', 'COMP124', 1, 'Fall', 2023, 'B'),
            ('12345', 'CS-101', 1, 'Fall', 2023, 'C'),
            ('12345', 'CS-190', 2, 'Spring', 2023, 'A'),
            ('12345', 'CS-315', 1, 'Spring', 2023, 'A'),
            ('12345', 'CS-347', 1, 'Fall', 2023, 'A'),
            ('19991', 'HIS-351', 1, 'Spring', 2023, 'B'),
            ('23121', 'FIN-201', 1, 'Spring', 2023, 'C+'),
            ('44553', 'PHY-101', 1, 'Fall', 2023, 'B'),
            ('45678', 'CS-101', 1, 'Fall', 2023, 'F'),
            ('45678', 'CS-101', 1, 'Spring', 2023, 'B+'),
            ('45678', 'CS-319', 1, 'Spring', 2023, 'B'),
            ('54321', 'CS-101', 1, 'Fall', 2023, 'A'),
            ('54321', 'CS-190', 2, 'Spring', 2023, 'B+'),
            ('55739', 'MU-199', 1, 'Spring', 2023, 'A'),
            ('76543', 'CS-101', 1, 'Fall', 2023, 'A'),
            ('76543', 'CS-319', 2, 'Spring', 2023, 'A'),
            ('76653', 'EE-181', 1, 'Spring', 2023, 'C'),
            ('98765', 'CS-101', 1, 'Fall', 2023, 'C'),
            ('98765', 'CS-315', 1, 'Spring', 2023, 'B'),
            ('98988', 'BIO-101', 1, 'Summer', 2023, 'A'),
            ('98988', 'BIO-301', 1, 'Summer', 2023, None),
        ]

        cursor.executemany("INSERT INTO takes (ID, course_id, sec_id, semester, year, grade) VALUES (?, ?, ?, ?, ?, ?)", values_to_insert)


        # Insert values into the teaches table
        values_to_insert = [
            ('10101', 'CS-101', 1, 'Fall', 2023),
            ('10101', 'CS-315', 1, 'Spring', 2023),
            ('10101', 'CS-347', 1, 'Fall', 2023),
            ('12121', 'FIN-201', 1, 'Spring', 2023),
            ('15151', 'MU-199', 1, 'Spring', 2023),
            ('22222', 'PHY-101', 1, 'Fall', 2023),
            ('32343', 'HIS-351', 1, 'Spring', 2023),
            ('45565', 'CS-101', 1, 'Spring', 2023),
            ('45565', 'CS-319', 1, 'Spring', 2023),
            ('76766', 'BIO-101', 1, 'Summer', 2023),
            ('76766', 'BIO-301', 1, 'Summer', 2023),
            ('83821', 'CS-190', 1, 'Spring', 2023),
            ('83821', 'CS-190', 2, 'Spring', 2023),
            ('83821', 'CS-319', 2, 'Spring', 2023),
            ('98345', 'EE-181', 1, 'Spring', 2023),
            ('88888', 'COMP124', 1, 'Fall', 2023),
            ('77777', 'COMP217', 1, 'Fall', 2023),
        ]

        cursor.executemany("INSERT INTO teaches (ID, course_id, sec_id, semester, year) VALUES (?, ?, ?, ?, ?)", values_to_insert)

        # Insert values into the time_slot table
        values_to_insert = [
            ('H', 'Monday', '08:00 AM', '09:15 AM'),
            ('F', 'Monday', '09:30 AM', '10:45 AM'),
            ('E', 'Tuesday', '08:00 AM', '09:15 AM'),
            ('D', 'Tuesday', '09:30 AM', '10:45 AM'),
            ('B', 'Wednesday', '08:00 AM', '09:15 AM'),
            ('A', 'Wednesday', '09:30 AM', '10:45 AM'),
            ('C', 'Thursday', '08:00 AM', '09:15 AM'),
        ]

        cursor.executemany("INSERT INTO time_slot (time_slot_id, day, start_time, end_time) VALUES (?, ?, ?, ?)", values_to_insert)

    except sqlite3.Error as e:
        print(f"SQlite error: {e}")
        return False
    finally:
    # Commit the changes and close the connection
        conn.commit()
        conn.close()
insert()