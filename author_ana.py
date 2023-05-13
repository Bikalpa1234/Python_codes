import pandas as pd 
import tkinter as tk
from tkinter import filedialog

data= pd.read_csv('C:/Users/DELL/OneDrive/Desktop/a3.csv')

first= pd.DataFrame(columns=['Author','Number','Citation'])


for m in range(len(data)):
    name= data.Aaaa[m]
    sp=str(name)
    b=0
    for n in range(len(data)):
        namee= data.Aaaa[n]
        spc=str(namee)
        if sp==spc:
            b=b+1
        
    first=first.append({'Author':sp,'Number':b,'Citation':data.Citation[m]},ignore_index=True)



df =first


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

def exportCSV ():
    global df
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = False, header=True)

saveAsButton_CSV = tk.Button(text='Export CSV', command=exportCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=saveAsButton_CSV)

root.mainloop()
