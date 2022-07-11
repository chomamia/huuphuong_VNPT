import sqlite3

conn = sqlite3.connect('member.db')
cursor_obj = conn.cursor()

sql_select_all = '''SELECT rowid, *FROM STUDENT'''
# sap xep du lieu bang order by theo tang dan 
sql_select_order = '''SELECT rowid, *FROM STUDENT ORDER BY NAME'''
# sap xep du lieu bang order by theo giam dan
sql_select_order_desc = '''SELECT rowid, *FROM STUDENT ORDER BY NAME DESC'''
sql_select= '''SELECT rowid, *FROM STUDENT WHERE NAME = 'PHUONG1' AND CLASS= 'A' '''
def get_all_student():
    with conn:
        cursor_obj.execute(sql_select)
        return cursor_obj.fetchall()

students = get_all_student()
for student in students:
    print(student)