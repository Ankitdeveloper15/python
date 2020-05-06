import sqlite3

conn = sqlite3.connect('mydatabase.db')
curr = conn.cursor()

##curr.execute("""create table quotes_tb(
##                title text,
##                author text,
##                tag text)""")

curr.execute("""insert into quotes_tb values('ankit','gupta','great')""")

conn.commit()
conn.close()
