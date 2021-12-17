x = input()
arr = x.split(',')
arr.sort()
a = eval(arr[0])
b = eval(arr[1])
c = eval(arr[2])
if a+b<=c or a+c<=b or b+c<=a:
    print('數字:{}'.format(x))
    print('形狀:{}'.format('不是三角形'))
    quit()
elif a==b==c:
    type = '正三角形'
elif a==b or b==c or a==c:
    type = '等腰三角形'
elif c**2==a**2+b**2 or a**2==c**2+b**2 or b**2==a**2+c**2:
    type = '直角三角形'
else:
    type = '一般三角形'
s = (a+b+c)/2
import math
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print('數字:{}'.format(x))
print('形狀:{}'.format(type))
print('面積:{}'.format(round(area,1)))