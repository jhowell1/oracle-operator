# Back End operations

# Query create method, takes in cx_Oracle cursor and user's SQL command
def create(cursor, sql):
    cursor.execute(sql)
    query = ""
    for row in cursor:
        query += ', '.join(str(x) for x in row) + '\n'
    return query

# Download Query method, takes in query result string, and query count
def download(query, i):
    fileName = "query" + str(i) + ".csv"
    file = open(fileName, "w")
    file.write(query)
    return file
