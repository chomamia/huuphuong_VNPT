import sqlite3
from Student import STUDENT


conn = sqlite3.connect('member.db')
cursor_obj = conn.cursor()
student1 = STUDENT('QUYNH', 'A', 'A1')
sql_insert = f'''INSERT INTO STUDENT VALUES (:NAME, :CLASS, :SECTION)'''

def insert_student(student):
    # with replace of commit() and close()
    with conn:
        cursor_obj.execute(sql_insert, {'NAME':student.name, 'CLASS': student.CLASS, 'SECTION':student.section})
    print("Student inserted!")

sql_select = f'''SELECT *FROM STUDENT WHERE NAME = :NAME'''
def get_student_by_name(name):
    with conn:
        cursor_obj.execute(sql_select, {'NAME': name})
    return cursor_obj.fetchall()
# insert_student(student1)
print(get_student_by_name('Raju')[-1])