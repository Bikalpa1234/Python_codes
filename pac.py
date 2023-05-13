from selenium import webdriver
import pandas as pd 
import tkinter as tk
import time
from tkinter import filedialog


data= pd.read_csv('C:/Users/DELL/OneDrive/Desktop/Book1.csv')


issn=pd.DataFrame(columns=['ISSN'])


#for m in range(len(data)):

for i in range(5):
    browser = webdriver.Chrome(executable_path='C:/Users/DELL/OneDrive/Desktop/Code/chromedriver.exe')
    name= data.Link[i]
    sp=str(name)
    browser.get(sp)
    time.sleep(7)
    cop = browser.find_elements_by_css_selector('[class*="col-md-5"]') 
    #div=cop[0]
    #text = div.text
    #issn=issn.append({'ISSN':text},ignore_index=True)
       
    for div in cop:
        text = div.text
        mm=text[6:15]
        issn=issn.append({'ISSN':mm},ignore_index=True)
    
    browser.close()

   

#browser.execute_script('window.scrollBy(0, 800)')


df= issn

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










     
    



