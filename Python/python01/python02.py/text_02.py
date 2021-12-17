x = int(input())
a=int(x // 12)
b=int(x % 12)
if b==0 and x!=0:
    d = x//a
elif x==0:
    d = x
else:
    d = b
if b>0 and b<12:
    e = a+1
else:
    e = a
print('雞蛋總數:{}'.format(x))
print('盒子至少:{}'.format(e))
print('蛋數最少:{}'.format(d))   

