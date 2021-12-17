a = eval(input())
b = eval(input())
c = input()
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':#保留小數
    print(a/b)
elif c=='//':#去小數
    print(a//b)
elif c=='%':
    print(a%b)