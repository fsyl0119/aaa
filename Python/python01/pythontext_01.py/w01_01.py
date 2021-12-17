print('123abc123'.strip('123')) #lstrip(left)  #rstrip(right)
print('apple'.startswith('a')) #判斷開頭字母
print('lemon'.endswith('t')) #判斷結尾字母
print('lemon'.find('m')) #找字母位置，沒找到回報-1
print('apple'.index('p')) #找字母位置，沒找到報錯
print('lemon'.replace('m','mmmm')) #替代字符位置
print('abbbcdde'.count('b')) #計算指定字符數
print('apple'.upper()) #大寫
print('LEMON'.lower()) #小寫
print('apple'.center(11,'+')) #補充
print('hello %s,%s' %('lemon','banana')) #插入字符
print('%.2f' %(3.14)) #浮點數(假設指定幾位數，只需在f前添加數字)
