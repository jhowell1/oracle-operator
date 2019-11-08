import cx_Oracle

conn_str = u'user101/pass101@54.70.62.21:1521'
connection = cx_Oracle.connect(conn_str)
c = connection.cursor()
c.execute('select * from airlines')
for row in c:
    print(row)
connection.close()