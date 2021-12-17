# year = int(input())
# if year%4==0 and year%100!=0:
    # type = '是閏年'
# elif year%4==0 and year%100==0 and year%400==0:
    # type = '是閏年'
# else:
    # type = '不是閏年'
# print('西元{}年{}'.format(year,type))

x = input()
y = x[::-1]
str = ''
for a in y:
    print(a+'*')
    str+=a+'*'
print(str)