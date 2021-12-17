x = input()
y = x.split(' ')
for i in range(int(y[0]),int(y[1])+1):
    sum=0
    n=len(str(i))#字串長度
    k=i#每個字串
    while k>0:
        digit=k%10#除於10計算每個位數
        sum+=digit**n#每位數乘以(字串長度)次方
        k//=10
    if i==sum:
        print(i)


    