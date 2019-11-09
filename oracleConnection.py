import cx_Oracle


def makeConnection (username, password, ip):
    conn_str = username + '/' + password + '@' + ip + ':1521'
    connection = cx_Oracle.connect(conn_str)
    c = connection.cursor()
    c.execute('select * from airlines')
    #list = []
    for row in c:
        #list.append(row)
        print(row)
    connection.close()
