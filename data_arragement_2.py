import pandas as pd 
import tkinter as tk
from tkinter import filedialog

data= pd.read_csv('C:/Users/DELL/OneDrive/Desktop/New folder/DFL_550.csv')

new=pd.DataFrame(columns=['month','Day','year','Daily flow'])



for i in range(1966,1982,1):

    #for p in range(len(data)):
     #   if (data.year[p]==i):
      #      if (data.month[p]==1):
       #         if (data.day[p]==1):
        #            a=p
         #       else:
          #          a=0



    for j in range(1,13,1):
        if j==1 or j==3 or j==5 or j==7 or j==8 or j==10 or j==12:
            for k in range(1,32,1):
                b=0
                c=0
                for p in range(0,len(data),1):
                    if (data.year[p]==i):
                        if (data.month[p]==j):
                            if (data.day[p]==k):
                                b=p
                                break
                if  b!=c:
                    new=new.append({'month':j,'Day':k,'year':i,'Daily flow':data.discharge[b]},ignore_index=True)
                else:
                    new=new.append({'month':j,'Day':k,'year':i,'Daily flow':0},ignore_index=True)




                            
        elif j==4 or j==6 or j==9 or j==11:
            for k in range(1,31,1):
                b=0
                c=0
                for p in range(0,len(data),1):
                    if (data.year[p]==i):
                        if (data.month[p]==j):
                            if (data.day[p]==k):
                                b=p
                                break
                if  b!=c:
                    new=new.append({'month':j,'Day':k,'year':i,'Daily flow':data.discharge[b]},ignore_index=True)
                else:
                    new=new.append({'month':j,'Day':k,'year':i,'Daily flow':0},ignore_index=True)
        else:
            if i % 4 ==0:
                for k in range(1,30,1):
                    b=0
                    c=0
                    for p in range(0,len(data),1):
                        if (data.year[p]==i):
                            if (data.month[p]==j):
                                if (data.day[p]==k):
                                    b=p
                                    break
                    if  b!=c:
                        new=new.append({'month':j,'Day':k,'year':i,'Daily flow':data.discharge[b]},ignore_index=True)
                    else:
                        new=new.append({'month':j,'Day':k,'year':i,'Daily flow':0},ignore_index=True)
            else:
                for k in range(1,29,1):
                    b=0
                    c=0
                    for p in range(0,len(data),1):
                        if (data.year[p]==i):
                            if (data.month[p]==j):
                                if (data.day[p]==k):
                                    b=p
                                    break
                    if  b!=c:
                        new=new.append({'month':j,'Day':k,'year':i,'Daily flow':data.discharge[b]},ignore_index=True)
                    else:
                        new=new.append({'month':j,'Day':k,'year':i,'Daily flow':0},ignore_index=True)
    print(i)
                    

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





