import cx_Oracle
from tkinter import *
import queryOperations as q
import tkinterScrollbar as tkS

# Global Vars for serverOperations, yes global vars are bad
cursor = None
m = ""   # string carrying query result
c = 0  # query count

# Method connecting user to the server
def makeConnection (username, password, ip):
    connStr = username + '/' + password + '@' + ip + ':1521'
    connection = cx_Oracle.connect(connStr)
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
        self.lf = LabelFrame(self, text="Query " + str(self.count), background="spring green")
        # tkinter Scrollbars, with LabelFrame as it's master window
        self.xScroll = Scrollbar(self.lf, orient=HORIZONTAL, background="spring green")
        self.xScroll.pack(side=BOTTOM, fill=X)
        self.yScroll = Scrollbar(self.lf, orient=VERTICAL)
        self.yScroll.pack(side=RIGHT, fill=Y)
        # tkinter Text box, with LabelFrame as it's master window
        self.text = Text(self.lf, height=27, width=102, wrap=NONE, background="salmon")
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
    count = 1
    queries = []
    dRow = 1
    qRow = 1

    # Constructor method
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(sticky=W)
        lf = LabelFrame(master, background="azure")
        lf.grid()
        scrollFrame = tkS.VerticalScrolledFrame(lf)
        scrollFrame.grid(sticky="we")
        SQLInteraction(master=scrollFrame.interior)


class SQLInteraction (Frame):
    # Public members
    sql = ""
    count = 1
    queries = []
    dRow = 1
    qRow = 1

    # Constructor method
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(sticky=W)
        self.config(width=1000)
        self.grid_columnconfigure(2, minsize=745)
        # SQL Label and Entry
        Label(self, text="SQL>", background="azure").grid(row=0, column=0, sticky=E)
        self.sql = Entry(self)
        self.sql.grid(row=0, column=1, sticky=W)
        # Button to submit SQL command to server
        Button(self, text="Enter", background="azure",
               command=lambda: self.execute()
               ).grid(row=0, column=2, sticky=W)

    # SQL Command Execute method
    def execute(self):
        i = self.count
        query = q.create(cursor, self.sql.get())  # Uses query create method to create query
        self.queries.append(query)
        self.display()  # Display query result
        # Button to allow user to download csv file of new query
        Button(self, text="Download", background="azure",
               command=lambda: q.download(self.queries[i], i)
               ).grid(row=self.dRow, column=1, sticky="ne")
        self.dRow += 1
        self.count += 1  # iterate query count

    # Display method that makes query result and query count global, creates new SQLResult instances
    def display(self):
        global m
        m = self.queries[-1]
        global c
        c = self.count
        # New Frame for SQLResult to inhabit
        newFrame = Frame(self)
        newFrame.grid(row=self.qRow, column=2, sticky=W)
        self.qRow += 1
        # New instance of SQLResult, with newFrame as it's master window
        SQLResult(newFrame)
