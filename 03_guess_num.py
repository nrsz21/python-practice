#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{} ={}'.format(i,j,i*j),end=' ')
#     print()
#猜数字
import random
num = random.randint(1,101)
while True:
    a = input('请输入你猜测的数字：')
    if not a.isdigit():#判断是不是数字
        print('请输入数字')
        continue
    if int(a) > num:
        print('大了')
    elif int(a)==num:
        print('猜对了')
        break
    else:
        print('小了')




