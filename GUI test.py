import tkinter as tk
from tkinter import filedialog
from tkinter import *
root= tk.Tk()

####Window
canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()


###name
name = tk.Entry (root) 
canvas1.create_window(150, 70, window=name)

dname= name.get()

##gender
gender= tk.Entry(root)
variable = StringVar(gender)
variable.set("Gender") # default value

w = OptionMenu(gender, variable, "male", "femlae", "other")
canvas1.create_window(150, 250, window=gender)
w.pack()





def exportCSV ():
    global df
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = False, header=True)

saveAsButton_CSV = tk.Button(text='Export CSV', command=exportCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=saveAsButton_CSV)

root.mainloop()
