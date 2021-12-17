# x =input()
# names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# arr = x.split()
# a = int(arr[0])-1
# b = int(arr[1])
# c = int(arr[2])
# print(names[0:a]+names[a:b]*c+names[b:])

x = input()
names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
arr = x.split()
a = int(arr[0])-1
b = int(arr[1])-1
temp = names[a]
names[a] = names[b]
names[b] = temp
print(names)