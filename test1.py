import pandas as pd 


data= pd.read_csv('C:/Users/DELL/OneDrive/Desktop/New folder/DFL_505.csv')

new=pd.DataFrame(columns=['month','Day','year','Daily flow'])

for p in range(len(data)):
    if (data.year[p]==1963):
        if (data.month[p]==1):
            if (data.Day[p]==15):
                print(p)

#if data[(data['year'].astype(int)==int(1963)).bool() & (data['month'].astype(int)==int(1)).bool() & (data['Day'].astype(int)==int(15)).bool()]:
 #   a=data[(data['year'].astype(int)==int(1963)).bool() & (data['month'].astype(int)==int(1)).bool() & (data['Day'].astype(int)==int(15)).bool()].index



