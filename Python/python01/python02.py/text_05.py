x = input()
b = len(x)
q = ''
for a in range(1,b+1):
    print(x[a-1]+str(a))
    q +=x[a-1]+str(a)
print(q)

