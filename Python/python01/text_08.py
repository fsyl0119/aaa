# x = input()
# arr = x.split()
# a = int(len(arr[0]))**2
# b = int(len(arr[1]))**2
# print("平方總和:{}".format(a+b))
# c = int(len(arr[0]))**len(arr[1])
# d = int(len(arr[1]))**len(arr[0])
# print("交互次方總和:{}".format(c+d))

x = int(input())
if x<= 50:
    print("工讀時數:{}小時".format(x))
    print("應領薪資:{}元".format(x*150)) 
elif x<= 70:
    print("工讀時數:{}小時".format(x))
    print("應領薪資:{}元".format((x-50)*200+int(50*150)))
else:
    print("工讀時數:{}小時".format(x))
    print("應領薪資:{}元".format((x-70)*250+int(50*150)+int(20*200)))   
