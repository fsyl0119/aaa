a = eval(input())#分
b = eval(input())#秒
c = eval(input())#距離
print('Speed:{:.1f}'.format((c/1.6)/((a+b/60)/60)))#秒換成分/60，再換小時/60
#要求答案為每小時的速度