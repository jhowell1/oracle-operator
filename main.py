from tkinter import *
from tkinter import ttk
import ubuntuConnector as UC
import serverOperations as SO
import comparisonMaker as CM

# Establishes root GUI Frame as Tk() object (a GUI)
root = Tk()
root.title("Oracle Operator")
# Instantiate UbuntuConnector object with root as it's master window
connection = UC.UbuntuConnector(root)
# Instantiate a ttk Notebook object with root as it's master window
nb = ttk.Notebook(root, width=1000)
# Create Tabs in Notebook as new Frames
f1 = ttk.Frame(nb)
f2 = ttk.Frame(nb)
# Add Tabs to Notebook with titles
nb.add(f1, text="SQL Access")
nb.add(f2, text="Make Comparisons")
# Instantiate SQLAccess object with Notebook Tab 1 as it's master window
SO.SQLAccess(f1)
CM.ComparisonMaker(f2)
nb.pack(fill="both", expand=True)
nb.grid()
credit = Label(root, text="James Howell and Brett Florek 2019").grid()
# Loop to keep program running until user closes program
root.geometry("1055x620")
root.mainloop()
