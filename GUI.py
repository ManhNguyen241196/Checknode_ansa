import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
# from creatTxt import readTxt

root = tk.Tk()
root.title("Entry Table")
root.geometry("300x200")

label_intro = tk.Label( root,  text = "Paste node muốn check vào ô dưới đây:")
label_intro.pack()
# Create a frame to hold the entries
entry_frame = tk.Frame(root)
entry_frame.pack(padx=10, pady=10)
entry = tk.Text(entry_frame,height=6)
entry.pack(fill=tk.X)
# Create a list to store the entry widgets
entries = []

var = StringVar()
label = tk.Label( root,  textvariable = var)
var.set("")

def CheckData():
    inp = entry.get(1.0, "end-1c") 
    ListChecked = inp.split("\n")
    print(ListChecked)
    
    
    def readTxt(link,ListChecked):
        var.set("Checking...")
        root.update()
        f = open(link, "r")
        AllText = f.read()
        myList = AllText.split("\n")
        list_error = [val for val in ListChecked if val and val in myList]
        A = set(ListChecked)
        B = set(list_error)
        messagebox.showwarning("Information", f'Các node sai là:\n  {A - B}') 
    readTxt(filedialog.askopenfilename(),ListChecked)
    var.set("Done!!!!")

checkBtn = tk.Button(root, text="Chọn file node để check", command= CheckData)
checkBtn.pack()
label.pack()
root.mainloop()
