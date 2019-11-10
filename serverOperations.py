import cx_Oracle
from tkinter import *
import queryOperations as q

# Global Vars for serverOperations, yes global vars are bad
cursor = None
m = ""   # string carrying query result
c = 0  # query count

# Method connecting user to the server
def makeConnection (username, password, ip):
    conn_str = username + '/' + password + '@' + ip + ':1521'
    connection = cx_Oracle.connect(conn_str)
    c = connection.cursor()
    global cursor
    cursor = c

'''
SQLResult object to present query results
New instances of SQLResult are instantiated for each new query
Creates a tkinter LabelFrame labeled after the query count c, with scrollbars to
    traverse query
SQLResult object extends tkinter Frame object passed as parameter
'''
class SQLResult (Frame):
    # Contructor method
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(row=1, column=0, sticky="se")
        self.message = m
        self.count = c
        # tkinter LabelFrame
        self.lf = LabelFrame(self, text="Query " + str(self.count))
        # tkinter Scrollbars, with LabelFrame as it's master window
        self.xScroll = Scrollbar(self.lf)
        self.xScroll.pack(side=BOTTOM, fill=X)
        self.yScroll = Scrollbar(self.lf)
        self.yScroll.pack(side=RIGHT, fill=Y)
        # tkinter Text box, with LabelFrame as it's master window
        self.text = Text(self.lf, height=20, width=100, wrap=NONE)
        self.text.pack(side=LEFT, fill=Y)
        self.yScroll.config(command=self.text.yview)
        self.xScroll.config(command=self.text.xview)
        self.text.config(xscrollcommand=self.xScroll.set, yscrollcommand=self.yScroll.set)
        self.insertMsg()  # insert query result into LabelFrame window
        self.lf.grid(column=0)

    # Insert Message m into LabelFrame Text box
    def insertMsg (self):
        self.text.insert(END, m)

'''
SQLAccess object to collect SQL command from user, submit to server, and generate queries
SQLAcces object extends tkinter Frame object passed as parameter
'''
class SQLAccess (Frame):
    # Public members
    sql = ""
    count = 0
    query = None

    # Constructor method
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(sticky=W)
        # SQL Label and Entry
        Label(self, text="SQL>").grid(row=0, column=0, sticky=E)
        self.sql = Entry(self)
        self.sql.grid(row=0, column=1, sticky=W)
        # Button to submit SQL command to server
        Button(self, text="Enter",
               command=lambda: self.execute()
               ).grid(row=0, column=2, sticky=W)

    # SQL Command Execute method
    def execute(self):
        self.count += 1  # iterate query count
        self.query = q.create(cursor, self.sql.get())  # Uses query create method to create query
        self.display(self.query)  # Display query result
        # Button to allow user to download csv file of new query
        Button(self, text="Download",
               command=lambda: q.download(self.query, self.count)
               ).grid(row=1, column=1, sticky="ne")

    # Display method that makes query result and query count global, creates new SQLResult instances
    def display(self, query):
        global m
        m = self.query
        global c
        c = self.count
        # New Frame for SQLResult to inhabit
        newFrame = Frame(self)
        newFrame.grid(row=1,column=2)
        # New instance of SQLResult, with newFrame as it's master window
        SQLResult(newFrame)
