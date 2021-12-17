# x = input()
# y = len(x)
# i=1
# while i<=y:
#     print(x[:i])
#     i+=1
# while i>2:
#     print(x[:i-2])
#     i-=1

x = input().split(',')
y = input().split(',')
n=0
z = len(x)
for i in range(z):
    print(x[i]+':'+y[i])
    # n+=int(i) #0+y[n]=a  a+y[n+1]=b (n=0)
for d in y:
    n+=int(d)
print('成績總和:{}'.format(n))

