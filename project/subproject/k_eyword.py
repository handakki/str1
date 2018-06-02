import random
print ('猜数游戏\n')
num = random.randint(1,100)
while True:
    print ('请输入一个1到100的数字：')
    i = int (input())
    if i == num:
        print ('你猜对了\n')
        break
    elif i < num:
        print ('数小了\n')
    elif i > num:
        print ('数大了\n')
