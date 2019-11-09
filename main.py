from tkinter import *
from tkinter import ttk
import ubuntuConnector as UC

root = Tk()
root.title("Ubuntu Operator - James Howell and Bretton Florek")
connection = UC.UbuntuConnector(root)
nb = ttk.Notebook(root, width=800)
f1 = ttk.Frame(nb)
f2 = ttk.Frame(nb)
#f3 = ttk.Frame(nb)
#f4 = ttk.Frame(nb)
nb.add(f1, text="SQL Access")
nb.add(f2, text="Make Comparisons")
#nb.add(f3, text="Download Raw Data")
#nb.add(f4, text="Add New Data")
nb.grid()

root.mainloop()
