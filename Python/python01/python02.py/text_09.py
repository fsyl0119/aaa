x = input()
y = input()
c=1
a=0
for i in range(c-1,len(x)):
    if c%2!=0:
        print(x[a]+y[0],end='')
    else:
        print(x[a]+y[1],end='')
    a+=1
    c+=1
print()
    

