from tkinter import *


class UbuntuConnector (Frame):

    server = ""
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

        self.server = StringVar()
        self.server = Entry(window).grid(row=0, column=1, sticky=W)

        Label(window, text="Username: ").grid(row=1, column=0, sticky=E)

        self.username = StringVar()
        self.server = Entry(window).grid(row=1, column=1, sticky=W)

        Label(window, text="Password: ").grid(row=2, column=0, sticky=E)

        self.password = StringVar()
        self.server = Entry(window).grid(row=2, column=1, sticky=W)

        Button(window, text="Enter",
               command=self.connect()).grid(row=3, column=0, sticky=S)

    def connect(self):
        self.display()

    def display(self):
        msg = "Connected to ubuntu@" + self.server

        connectMsg = Text(self, height=1, width=200).grid()
        #connectMsg.insert(END, "Connected to ubuntu@" + self.location)