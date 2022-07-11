import sqlite3

conn = sqlite3.connect('member.db')
# create a cursor object using the cursor method
cursor = conn.cursor()
# create table 
# table = """CREATE TABLE STUDENT (NAME VARCHAR(255), CLASS VARCHAR(255), SECTION VARCHAR(255));"""
# cursor.execute(table)
# 1
# cursor.execute('''INSERT INTO STUDENT VALUES ('Raju', '7th', 'A')''')
# cursor.execute('''INSERT INTO STUDENT VALUES ('Shyam', '8th', 'B')''')
# cursor.execute('''INSERT INTO STUDENT VALUES ('Raju', '9th', 'C')''')
cursor.execute('''INSERT INTO STUDENT (CLASS, SECTION, NAME) VALUES ('A', '8th', 'Phuong')''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION) VALUES ('Huu', 'B', '7th')''')
print("Data Inserted in the table:")
data = cursor.execute('''SELECT *FROM STUDENT''')
for row in data:
    print(row)
conn.commit()
conn.close()


connection_obj = sqlite3.connect('geek.db')
cursor_obj = connection_obj.cursor()
# create table
connection_obj.execute(""" CREATE TABLE GEEK (EMAIL VARCHAR (255), NAME VARCHAR(255), SCORE INT);""")
connection_obj.execute("""INSERT INTO GEEK (EMAIL, NAME, SCORE) VALUES ('Huuphuongtp@gmail.com', 'Phuong', 15)""")
connection_obj.execute("""INSERT INTO GEEK (EMAIL, NAME, SCORE) VALUES ('Huuphuongtp1@gmail.com', 'Phuong1', 16)""")
connection_obj.execute("""INSERT INTO GEEK (EMAIL, NAME, SCORE) VALUES ('Huuphuongtp2@gmail.com', 'Phuong2', 17)""")
connection_obj.commit()
connection_obj.close()