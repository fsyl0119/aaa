x = input()
y = x.split(' ')
m = int(y[0])
n = int(y[1])
def fac(m,n):
    if m>n:
        smaller = n
    else:
        smaller = m
    for i in range(1,smaller+1):
        if (m%i==0) and (n%i==0):
            fac=i
    return fac
print('{}和{}的最大公因數是:{}'.format(m,n,fac(m,n)))
print('{}和{}的最小公倍數是:{}'.format(m,n,int((m*n)/fac(m,n))))