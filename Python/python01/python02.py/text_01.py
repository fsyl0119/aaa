# x = eval(input())
# if x<= 60:
    # fees = 130
# elif x<= 90:
    # fees = 170
# elif x<= 120:
    # fees = 210
# elif x<= 150:
    # fees = 250
# else:
    # fees = 300
# print('包裝盒:{}公分'.format(x))
# print('費用:{}元'.format(fees))
x = input()
arr = x.split(',')
a = eval(arr[0])
b = eval(arr[1])
c = eval(arr[2])
d =int(b*b-4*a*c)
if a==0:
    solvestr = '一個解'
    if b==0:
        solvestr = '無解'
        if c==0:
            solvestr = '無限多解'
elif d>0:
    solvestr = '二個解'
elif d==0:
    solvestr = '一個解'
else:
    solvestr = '無實數解'
print('係數:{},{},{}'.format(a,b,c))
print('方程式:{}*X^2+{}*X+{}=0'.format(a,b,c))
print('解:{}'.format(solvestr))   
