import sqlite3

# UPDATE DATA 
conn = sqlite3.connect('member.db')
cursor_obj = conn.cursor()
sql_update = ''' UPDATE STUDENT SET NAME = 'PHUONG1' WHERE CLASS = 'A'  '''
cursor_obj.execute(sql_update)
conn.commit()
conn.close()