import sqlite3

# UPDATE DATA 
conn = sqlite3.connect('member.db')
cursor_obj = conn.cursor()
sql_delete = ''' DELETE FROM STUDENT WHERE NAME = 'Huu' '''
cursor_obj.execute(sql_delete)
conn.commit()
conn.close()    