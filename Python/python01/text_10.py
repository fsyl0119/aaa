# x =int(input())
# if x<= 6:
    # level = '幼兒園'
# elif x<= 12:
    # level = '小學'
# elif x<= 15:
    # level = '國中'
# elif x<= 18:
    # level = '高中'
# else:
    # level = '大學'
# print('年紀:{}歲'.format(x))
# print('就讀:{}'.format(level))    
x = input()
names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
arr = x.split(',')
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
d = int(arr[3])
print(names[:a-1]*c+names[a-1:b]+names[b:]*d)