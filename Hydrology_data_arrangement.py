import pandas as pd 
import tkinter as tk
from tkinter import filedialog

data= pd.read_csv('C:/Users/DELL/OneDrive/Desktop/New folder/DFL_505.csv')

new=pd.DataFrame(columns=['month','Day','year','Daily flow'])



for i in range(len(data)):
    a=0
    if data.month[i]==1 or data.month[i]==3 or data.month[i]==5 or data.month[i]==7 or data.month[i]==8 or data.month[i]==10 or data.month[i]==12:
        for j in range(31):
            if data.Day[i]!=j:
                new=new.append({'month':data.month[i],'Day':data.Day[i],'year':data.year[i],'Daily flow':data.Dailyflow[i]},ignore_index=True)
                a=a+1
            if data.Day[i]==j:
                new=new.append({'month':data.month[i],'Day':data.Day[i],'year':data.year[i],'Daily flow':data.Dailyflow[i]},ignore_index=True)
        if a >31:
            new=new.append({'month':data.month[i],'Day':data.Day[j],'year':data.year[i],'Daily flow':0},ignore_index=True)

    elif data.month[i]==4 or data.month[i]==6 or data.month[i]==9 or data.month[i]==11:
        for j in range(30):
            if data.Day[i]!=j:
                new=new.append({'month':data.month[i],'Day':data.Day[i],'year':data.year[i],'Daily flow':data.Dailyflow[i]},ignore_index=True)
                a=a+1
            if data.Day[i]==j:
                new=new.append({'month':data.month[i],'Day':data.Day[i],'year':data.year[i],'Daily flow':data.Dailyflow[i]},ignore_index=True)
        if a>30:
            new=new.append({'month':data.month[i],'Day':data.Day[j],'year':data.year[i],'Daily flow':0},ignore_index=True)
    else:
        if data.year[i]%4==0:
            for j in range(29):
                if data.Day[i]!=j:
                    new=new.append({'month':data.month[i],'Day':data.Day[i],'year':data.year[i],'Daily flow':data.Dailyflow[i]},ignore_index=True)
                    a=a+1
                if data.Day[i]==j:
                    new=new.append({'month':data.month[i],'Day':data.Day[i],'year':data.year[i],'Daily flow':data.Dailyflow[i]},ignore_index=True)
            if a>29:
                new=new.append({'month':data.month[i],'Day':data.Day[j],'year':data.year[i],'Daily flow':0},ignore_index=True)
        else:
            for j in range(28):
                if data.Day[i]!=j:
                    new=new.append({'month':data.month[i],'Day':data.Day[i],'year':data.year[i],'Daily flow':data.Dailyflow[i]},ignore_index=True)
                    a=a+1
                if data.Day[i]==j:
                    new=new.append({'month':data.month[i],'Day':data.Day[i],'year':data.year[i],'Daily flow':data.Dailyflow[i]},ignore_index=True)
            if a>28:
                new=new.append({'month':data.month[i],'Day':data.Day[j],'year':data.year[i],'Daily flow':0},ignore_index=True)


        
            
    
    


df =new
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



            

