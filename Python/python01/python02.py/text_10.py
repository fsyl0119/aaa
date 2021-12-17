x = input().split(',')
a = int(x[0])
b = int(x[1])
k=''
sum=0
for i in range(1,a+1):
    if i%b==0:
        continue
    sum+=i
    k+=str(i)+','
print(k[:-1])
print('總和:{}'.format(sum))




