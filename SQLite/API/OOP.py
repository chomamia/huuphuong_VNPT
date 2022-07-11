import sqlite3
from this import s
from Student import STUDENT

conn = sqlite3.connect('member.db')
# student1 = STUDENT('Quan', 'A', 'AA')
cursor_obj = conn.cursor()
sql_insert = f''' INSERT INTO STUDENT VALUES ('{student1.name}', '{student1.CLASS}', '{student1.section}')'''
cursor_obj.execute(sql_insert)
student2 = STUDENT('Chau', 'B', 'A')
sql_insert1= f''' INSERT INTO STUDENT VALUES (?, ?, ?)'''
cursor_obj.execute(sql_insert1, (student2.name, student2.CLASS, student2.section))
# insert use key 
student3 = STUDENT('Huy', 'A', 'BB')
sql_insert2 = f''' INSERT INTO STUDENT VALUES (:NAME , :CLASS, :SECTION)'''
cursor_obj.execute(sql_insert2, ({'NAME': student3.name, 'CLASS': student3.CLASS, 'SECTION': student3.section}))
conn.commit()
conn.close()
