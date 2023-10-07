p=input("Enter the bits:")
length=len(p)
print(length)
for i in range(length):
    count=0
    """
    for j in range(length-1):
       if(p[j]=='1'):
           count=count+1
    print(count)
    if(count%2==0 and p[length-1]=='0'):
       print("It is not corrupted")
    elif(count%2!=0 and p[length-1]=='1'):
        print("It is not corrupted")
    else:
        print("It is corrupted")
        """
e=int(input("Enter the index of paraty bit:"))
countafterparatybit=0
countbeforeparatybit=0
totalcount=0
for i in range(length):
    for j in range(0,e-1):
        print(p[j])
    for j in range(e+1,length):
        print(p[j])
    for j in range(0,e-1):
        if(p[j]=='1'):
            countbeforeparatybit+=1
    for j in range(e+1,length):
        if(p[j]=='1'):
            countafterparatybit+=1
    totalcount=countbeforeparatybit+countafterparatybit
    if(totalcount%2==0 and p[e]=='0'):
       print("It is not corrupted")
    elif(totalcount%2!=0 and p[e]=='1'):
        print("It is not corrupted")
    else:
        print("It is corrupted")
