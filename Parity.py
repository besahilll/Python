p=input("Enter the bits:")
length=len(p)
print(length)
e=int(input("Enter the index at which you have inserted the parity bit:"))
c_b_p=0 #count before removing parity
c_a_p=0 #count after  removing parity
total_count=0
for i in range(0,e):
    print(p[i])
for j in range(e+1,length):
    print(p[j])
for i in range(0,e):
    if(p[i]=='1'):
        c_b_p+=1
for j in range(e+1,length):
    if(p[j]=='1'):
        c_a_p+=1
total_count=c_b_p+c_a_p
print(total_count)

if(total_count%2==0 and p[e]=='0'):
    print("It is not corrupted")
elif(total_count%2!=0 and p[e]=='1'):
    print("It is not corrupted")
else:
    print("It is corrupted")
