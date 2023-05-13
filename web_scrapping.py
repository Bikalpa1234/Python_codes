from selenium import webdriver
import pandas as pd 
import tkinter as tk
import time
from tkinter import filedialog
browser = webdriver.Chrome(executable_path='C:/Users/DELL/OneDrive/Desktop/Code/chromedriver.exe')
browser.get('https://www.housingnepal.com/search/professionals/contractors?fbclid=IwAR1QkvF16rlhRNHMLCNqzXztXLn8RbNkG1KmfPAmL9u84Ztz5PlrhkpJohw')


company= pd.DataFrame(columns=['Company'])
address= pd.DataFrame(columns=['Index','Address'])
adrre=pd.DataFrame()
phone=pd.DataFrame(columns=['Phone'])
#test=pd.DataFrame(columns=['index','District'])
abc=pd.DataFrame(columns=['Links'])


for k in range(50):

    time.sleep(7)
    cop = browser.find_elements_by_css_selector('[class*="float-left padding-top-5 padding-bottom-5  font-bold font-size-12 color-dark-orange"]')

    for div in cop:
        text = div.text
        company=company.append({'Company':text},ignore_index=True)
        print(text)

    ares= browser.find_elements_by_css_selector('[class*="float-left small padding-left-10"]')

    var1=0
    for add in ares:
        if add.text in ['Contractors']:
            pass
        else:
            var1=var1+1
            address=address.append({'Index':var1,'Address':add.text},ignore_index=True)
            print(add.text)


    #for i in range(var1):
    #    address.loc[i] = address[:i].apply(lambda x: ' , '.join(x.astype(str)))


    adrre=address.iloc[::2]
    
    #adrre=adrre.dropna(['Address'])
    #print(adrre[1])

    district= address[address['Index'] %2== 0] 
    



    #for i in range(0,var1,2):
    #   district=district.append({'District':address.Address[i]},ignore_index=True)


    phn= browser.find_elements_by_css_selector('[class*="float-left padding-top-2 padding-left-10"]')

    for ph in phn:
        phone=phone.append({'Phone':ph.text},ignore_index=True)
        print(ph.text)


    #get= browser.find_element_by_xpath("//div[@class='float-left color-06c padding-top-2 padding-right-20   padding-left-5']/a").get_attribute('href')
    elems = browser.find_elements_by_css_selector('[class*="link-06c"]')
    get = [elem.get_attribute('href') for elem in elems]


    for ln in get:
        if str(ln)[:5] in ['https']:
            pass
        else:
            abc=abc.append({'Links':str(ln)},ignore_index=True)

     

    time.sleep(7)
    browser.execute_script('window.scrollBy(0, 800)')
    #linkElem = browser.find_element_by_link_text('»')
    #ac = ActionChains(browser)
    time.sleep(2.5)
    #ac.move_to_element(linkElem).move_by_offset(696, 446).click().perform()

    linkElem = browser.find_element_by_link_text('»')
    type(linkElem)
    linkElem.click()
    #browser.current_url
    #browser.get(path)   
    data=pd.concat([company,adrre,district,phone,abc], axis=1)



df= data

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









     
    



