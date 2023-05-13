from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import tkinter as tk
from tkinter import filedialog
#from pynput.keyboard import key, Listener 


data= pd.DataFrame(columns=['ID','Links'])
#browser = webdriver.Chrome(executable_path='C:/Users/DELL/OneDrive/Desktop/Code/chromedriver.exe')
#browser.get('https://www.kickstarter.com/discover/advanced?sort=most_funded&seed=2650150&')
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\DELL\\OneDrive\\Desktop\\User Data")
browser = webdriver.Chrome(executable_path='C:/Users/DELL/OneDrive/Desktop/Code/chromedriver.exe', chrome_options=options)
browser.get("https://www.kickstarter.com/discover/advanced?sort=most_funded&seed=2650150&")
browser.implicitly_wait(3)
linkElem = browser.find_element_by_link_text('Load more')
type(linkElem)
linkElem.click() 
browser.implicitly_wait(3)
for i in range(0,4000):
    print(i)
    #browser.execute_script('window.scrollBy(0, 400)')
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        linkElem = browser.find_element_by_link_text('Load more')
        type(linkElem)
        linkElem.click() 
    except:
        pass 




browser.current_url
try:
    element = WebDriverWait(browser).until(EC.presence_of_element_located((By.XPATH, '//*[@href]')))
except:
    pass
ids= browser.find_elements_by_xpath('//*[@href]')
count=0
for ii in ids:
    add=ii.get_attribute('href')
    string=str(add)[-26:]
    if string in ['?ref=discovery_most_funded']: 
        a=a+1
        data=data.append({'ID':a,'Links':ii.get_attribute('href')},ignore_index=True)
        print(ii.get_attribute('href'))
    else:
        pass
data = data.drop_duplicates('Links')
df=data    









#linkElem = browser.find_element_by_link_text('Load more')
#type(linkElem)
#linkElem.click() 


#for i in range(10):
    #SCROLL_PAUSE_TIME = 2
    #last_height = browser.execute_script("return document.body.scrollHeight")
    #while True:
     #   browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      #  time.sleep(SCROLL_PAUSE_TIME)
       # new_height = browser.execute_script("return document.body.scrollHeight")
        #if new_height == last_height:
         #   break
        #last_height = new_height







#print(data.head())

def exportCSV ():
    
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = False, header=True)




root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 200, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()




saveAsButton_CSV = tk.Button(text='Export CSV', command=exportCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 100, window=saveAsButton_CSV)



root.mainloop()







