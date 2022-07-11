import sqlite3
# # select all data use fechall
connection_obj = sqlite3.connect('geek.db')
cursor_obj = connection_obj.cursor()
statement = '''SELECT * FROM GEEK'''
cursor_obj.execute(statement)
print("All the data")
output = cursor_obj.fetchall()
for row in output:
    print(row)
connection_obj.commit()
connection_obj.close()

# # select not all use fetchmany()
connection_obj = sqlite3.connect('geek.db')
cursor_obj = connection_obj.cursor()
statement = '''SELECT * FROM GEEK'''
cursor_obj.execute(statement)
print("Not all the data")
output = cursor_obj.fetchmany(2)
for row in output:
    print(row)
connection_obj.commit()
connection_obj.close()

# # select only one rows use fetchone()
connection_obj = sqlite3.connect('geek.db')
cursor_obj = connection_obj.cursor()
statement = '''SELECT * FROM GEEK'''
cursor_obj.execute(statement)
print("Only one rows")
output = cursor_obj.fetchone()
print(output)
connection_obj.commit()
connection_obj.close()
# select use where 
connection_obj = sqlite3.connect('member.db')
cursor_obj = connection_obj.cursor()
statement = '''SELECT *FROM STUDENT WHERE NAME = 'Raju' '''
cursor_obj.execute(statement)
output = cursor_obj.fetchall()
print(output)
connection_obj.commit()
connection_obj.close()

