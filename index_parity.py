n=int(input("Enter the number of test cases:"))
for i in range(n):
    p=input("Enter the bits:")
    length=len(p)
    print(length)
    count=0
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
e=p[length-1]
print(e)
i=input("Enter the index at which you have inserted the parity bit:")
d=p[0:length:i]
print(d)
        
          
