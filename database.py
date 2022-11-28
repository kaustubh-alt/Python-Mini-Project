import sqlite3
connection = sqlite3.connect("newdba")
csr = connection.cursor()


csr.execute("""CREATE TABLE tablea(NAME VARCHAR(255),ID INT(2),AGE INT(2));""")
#if we have already created table then make sure to comment out above line

def dele():

    b = int(input("ID number"))
    csr.execute('''DELETE FROM tablea WHERE ID = :b''',{'b':b})
    display()
2
def insert():
    a = input("Your name")
    b = int(input("your ID"))
    c = int(input("Your age"))
    csr.execute('''INSERT INTO tablea(NAME,ID,AGE) VALUES (:a,:b,:c)''', {'a': a , 'b':b , 'c':c})
    csr.execute('SELECT * FROM tablea WHERE NAME = :a', {'a': a})

def display():
    print("  Name      ID       Age")
    for row in csr.execute('SELECT * FROM tablea;'):
        print(row)


a = int(input("1 for data insert , 2 for delete data , 3 for display data"))
if(a == 1):
    insert()
elif (a == 2):
    dele()
elif ( a == 3):
    display()
else:
    print("Enter an appropriate number")

connection.commit()
connection.close()
