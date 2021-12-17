x = input().split(',')
a = int(x[0])
b = int(x[1])
y=list()
for year in range(a,b+1):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                y.append(year)
            print('西元{}至{}年間沒有閏年!'.format(a,b))
            break
        elif year%100!=0:
            y.append(year)
    else:
        print('西元{}至{}年間沒有閏年!'.format(a,b))
        break
    year+=1
print('西元{}至{}年間的閏年有:'.format(a,b))
print([y])