from tkinter import *
import oracleConnection as oc


class UbuntuConnector (Frame):

    ip = ""
    username = ""
    password = ""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(sticky=W, padx=10, pady=10)
        self.popup()

    def popup(self):
        window = Toplevel()
        window.wm_title("Connect to Ubuntu")

        Label(window, text="IP Address: ").grid(row=0, column=0, sticky=E)

        #self.ip = StringVar()
        self.ip = Entry(window)
        self.ip.grid(row=0, column=1, sticky=W)

        Label(window, text="Username: ").grid(row=1, column=0, sticky=E)

       # self.username = StringVar()
        self.username = Entry(window)
        self.username.grid(row=1, column=1, sticky=W)

        Label(window, text="Password: ").grid(row=2, column=0, sticky=E)

        #self.password = StringVar()
        self.password = Entry(window, show='*')
        self.password.grid(row=2, column=1, sticky=W)

        Button(window, text="Enter",
               command=lambda: self.connect()
               ).grid(row=3, column=0, sticky=S)

    def connect(self):
        # calls the ubuntuConnection.py
        oc.makeConnection(self.username.get(), self.password.get(), self.ip.get())
        self.display()

    def display(self):
        msg = "Connected to ubuntu@" + self.ip.get() + " as " + self.username.get()

        connectMsg = Text(self, height=1, width=150)
        connectMsg.grid()
        connectMsg.insert(END, "Connected to ubuntu@" + self.location)
