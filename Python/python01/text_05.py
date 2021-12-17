# x = input() #取字串長度
# s = len(x)
# print(s)

# x = input() #保留小數
# s = eval(x)
# print(s)

# a1 = input()
# a2 = input()
# s1 = len(a1)
# s2 = len(a2)
# print("A"*s1, end="")
# print("A"*s1+"B"*s2) #此方法同樣可行
# print("B"*s2)

# a = input()
# print("原始字串:{}".format(a)) 
# b = (a[-2:])
# c = (a[:2])
# print("重組輸出:{}".format(b), end="") #此方法同樣可行
# print(c)
# print("重組輸出:{}{}".format(b,c)) #abcdef  efab

# a = input()
# print("原始數字:{}".format(a))
# b = (a[-2:])
# c = ("0"+a[:2]+"0")
# d = (a[2:4]+"0")
# print("重組輸出:{}{}{}".format(b,c,d))

a1 = input()
a2 = input()
a3 = input()
b3 = (a1[int(a2)-1:int(a2)])
print(a1[:int(a2)-1]+a1[int(a2):]+b3*int(a3))