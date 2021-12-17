# num = 0
# for i in range(5):
#     num += i
#     print(num)
x = int(input())
c=1
n=3
a=-1
print('序列:'+str(4),end='')
while c<x:
    if c%2==0:
        print('+'+str(4)+'/'+str(n),end='')
    else:
        print('-'+str(4)+'/'+str(n),end='')
    n+=2
    c+=1
print()
print()