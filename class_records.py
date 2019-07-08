import _sqlite3
from gradecalculator import Student


conn = _sqlite3.connect(':memory:')
conn.execute('PRAGMA foreign_keys=1')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS students 
(sid INTEGER PRIMARY KEY,
first text,
last text,
year text,
gender text,
average integer )""")



c.execute("""CREATE TABLE IF NOT EXISTS grades
(sid integer PRIMARY KEY,
homework int,
project int,
quiz int,
test int,
FOREIGN KEY (sid) REFERENCES students(sid))""")
conn.commit()

def insert_stu (stu):
    with conn:
        c.execute ("INSERT INTO students VALUES(:sid, :first, :last, :year, :gender, :average)",
                   {'sid': stu.id, 'first':stu.first_N, 'last': stu.last_N, 'average': stu.average, 'year': stu.year,
                    'gender':stu.gender})

def get_stu_by_name(lastname):
    c.execute("SELECT * FROM students WHERE last = :last_N",{'last_N': lastname})
    return c.fetchall()

def update_average(stu,average):
    with conn:
        c.execute("""UPDATE students SET average = :average
                     Where first = :first And last = :last""",
                    {'first':stu.first_N, 'last': stu.last_N, 'average': average})

def insert_grades(stu):
    with conn:
        c.execute("INSERT INTO grades VALUES(:sid, :homework, :project, :quiz, :test)",
                  {'sid':stu.id,'homework':stu.homework_avg,'project':stu.project_avg,'quiz':stu.quiz_avg,
                   'test':stu.test_avg})


def update_grades(stu,section,grade):
    with conn:
        if section == 'homework':
            c.execute("""UPDATE grades SET homework = :grade
            WHERE sid IN (SELECT sid FROM students 
                         WHERE first = :first and last = :last)
                          """,{'grade':grade, 'first':stu.first_N, 'last':stu.last_N})

        if section == 'project':
            c.execute("""UPDATE grades SET project = :grade
            WHERE sid IN (SELECT sid FROM students 
                         WHERE first = :first and last = :last)
                          """,{'grade':grade, 'first':stu.first_N, 'last':stu.last_N})


        if section == 'quiz':
            c.execute("""UPDATE grades SET quiz = :grade
            WHERE sid IN (SELECT sid FROM students 
                         WHERE first = :first and last = :last)
                          """,{'grade':grade, 'first':stu.first_N, 'last':stu.last_N})

        if section == 'test':
            c.execute("""UPDATE grades SET test = :grade
            WHERE sid IN (SELECT sid FROM students 
                         WHERE first = :first and last = :last)
                          """,{'grade':grade, 'first':stu.first_N, 'last':stu.last_N})


def remove_stu(stu):
    with conn:
        c.execute("DELETE from students WHERE first = :first AND last = :last ",{'first':stu.first_N,'last': stu.last_N})
