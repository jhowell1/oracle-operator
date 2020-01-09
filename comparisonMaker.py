from tkinter import *
import plotly as p

t = ""
c = 0

class Chart (Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(row=1, column=0, sticky="se")
        self.type = t
        self.count = c
        # tkinter LabelFrame
        self.lf = LabelFrame(self, text=self.type + " " + str(self.count))
        Label(self.lf, text="Variable 1: ").grid()
        self.var1 = StringVar()
        self.var1.set("")
        OptionMenu(self.lf, self.var1, )
        # tkinter Scrollbars, with LabelFrame as it's master window
        '''
        self.xScroll = Scrollbar(self.lf)
        self.xScroll.pack(side=BOTTOM, fill=X)
        self.yScroll = Scrollbar(self.lf)
        self.yScroll.pack(side=RIGHT, fill=Y)
        # tkinter Text box, with LabelFrame as it's master window
        # self.text = Text(self.lf, height=20, width=100, wrap=NONE)
        self.text.pack(side=LEFT, fill=Y)
        self.yScroll.config(command=self.text.yview)
        self.xScroll.config(command=self.text.xview)
        self.text.config(xscrollcommand=self.xScroll.set, yscrollcommand=self.yScroll.set)
        self.insertMsg()  # insert query result into LabelFrame window
        '''
        self.lf.grid(column=0)

class ComparisonMaker(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(sticky=W)
        Label(self, text="Chart Type:").grid(row=0, column=0, sticky=E)
        self.chart = StringVar()
        self.chart.set("Bar")
        OptionMenu(self, self.chart, "Bar", "ScatterPlot", "Pie"
                   ).grid(row=0, column=1, sticky=W)
        Button(self, text="Enter",
               command=lambda: self.execute()
               ).grid(row=0, column=2, sticky=W)

    def execute(self):
        global t
        t = self.chart.get()
        global c
        c += 1
        newFrame = Frame(self)
        newFrame.grid(row=0, column=1)
        Chart(newFrame)