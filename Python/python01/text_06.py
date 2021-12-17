# x = input()
# b = eval(x)
# print("前一個數字是:{}".format(int(b)-1))
# print("後一個數字是:{}".format(int(b)+1))
# A = int(b)-1
# B = int(b)+1
# c = (3*A)+(5*B)
# print("3A+5B的值:{}".format(c))

x = input()
y = input()
arr = y.split(',')
b = int(arr[0])
c = int(arr[2])
d = int(arr[1])
e = int(arr[3])
print(x[0:b-1]+(x[b-1:b]*d)+x[b:c-1]+x[c-1:c]*e+x[c:])
# c = int(arr[2])
# print(x[c-1:c])