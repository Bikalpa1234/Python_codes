from selenium import webdriver
import pandas as pd 
import time
import tkinter as tk
from tkinter import filedialog
from selenium.webdriver.common.keys import Keys

data= pd.read_csv('C:/Users/DELL/OneDrive/Desktop/nmp.csv')
new=pd.DataFrame(columns=['Check'])

browser = webdriver.Chrome(executable_path='C:/Users/DELL/OneDrive/Desktop/Code/chromedriver.exe')
browser.get('file:///C:/Users/DELL/OneDrive/Desktop/International%20Scientific%20Indexing%20(ISI).html')



for i in range(len(data)):
    browser.refresh()
    ans=str(data.ISSN[i])
    #print(len(ans))
    bc=ans
    browser.execute_script("window.scrollTo(0, 800);")
    if len(ans)==7:
        bc=ans.rjust(1+len(ans),'0') 
    if len(ans)==6:
        bc=ans.rjust(2+len(ans),'0')          
    time.sleep(4)
    try:
        inputElement = browser.find_element_by_name("searchbox")
        inputElement.send_keys(bc)
        inputElement.send_keys(Keys.RETURN)
    except:
        browser.refresh() 
        print('Not Found') 
    
    time.sleep(3)
    a=0


    cop = browser.find_elements_by_css_selector('[class*="sorting_1"]')
    if len(cop)!=0: 
        for div in cop:
            text=div.text
            new=new.append({'Check':text},ignore_index=True) 
    else:
        new=new.append({'Check':'-'},ignore_index=True)           

        
        


    






df= new

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






