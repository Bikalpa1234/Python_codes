a=34

def allowed(m):
    #while m!=0
    if(m-1)>=0:
        x=m-1
        if x==0:
            return 1
        elif allowed(x)==1:
            return 1
    elif(m-4)>=0:
        x=m-4
        if x==0:
            return 1
        elif allowed(x)==1:
            return 1
    elif(m-9)>=0:
        x=m-9
        if x==0:
            return 1
        elif allowed(x)==1:
            return 1                
    elif(m-16)>=0:
        x=m-16
        if x==0:
            return 1
        elif allowed(x)==1:
            return 1 
    elif(m-25)>=0:
        x=m-25
        if x==0:
            return 1
        elif allowed(x)==1:
            return 1  
    else:
        return 0        


moves=[1,4,9,16,25]
while a!=0:
    for i in range(len(moves)):
        if allowed(int(moves[i]))==1 and a-int(moves[i])>=0 :
            a=a-int(moves[i])
            print(a)
            print("First" + str(moves[i]))
            for j in range(len(moves)):
                if allowed(a-int(moves[j]))==1 and a-int(moves[j])>=0:
                    a=a-int(moves[j])
                    print(a)
                    print("Second" + str(moves[j]))




