from selenium import webdriver
import pandas as pd
import os
import re
import tkinter as tk
from tkinter import filedialog
browser = webdriver.Chrome(executable_path='C:/Users/DELL/OneDrive/Desktop/Code/chromedriver.exe')
browser.get('file:///C:/Users/DELL/OneDrive/Desktop/test.html')
try:
    elem = browser.find_element_by_class_name("locale-en")
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
#linkElem = browser.find_element_by_link_text('SHOW MORE')
#type(linkElem)
#linkElem.click() 

#for i in range(500):
    #browser.current_url
    #linkElem = browser.find_element_by_link_text('SHOW MORE')
    #type(linkElem)
    #print(i)
    #linkElem.click() 

browser.current_url
data= pd.DataFrame(columns=['ID','Links'])
ids= browser.find_elements_by_xpath('//*[@href]')

count=0
a=0
for ii in ids:
    add=ii.get_attribute('href')
    string=os.path.basename(str(add))
    if string in ['pica']: 
        a=a+1
        data=data.append({'ID':a,'Links':ii.get_attribute('href')},ignore_index=True)
        print(ii.get_attribute('href'))
       
    



print(data.head())
print(a)

df =data


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
