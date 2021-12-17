x = input()
arr = x.split(',')
x = eval(arr[0])
y = eval(arr[1])
print('座標:({},{})'.format(x,y))
if x==0 and y==0:
    quadrant = '原點'
elif x==0:
    quadrant = 'Y軸'
elif y==0:
    quadrant = 'X軸'
elif x>0 and y>0:
    quadrant = '第一象限'
elif x<0 and y>0:
    quadrant = '第二象限'
elif x<0 and y<0:
    quadrant = '第三象限'
else:
    quadrant = '第四象限'
print('位置:{}'.format(quadrant))
