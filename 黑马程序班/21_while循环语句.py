# 循环语句知道条件不满足 结束
### 表白语句

i = 1
while i < 100:# 条件满足true就执行
    print("我爱你！\n") 
    i += 1
### 练习题
'''
求1到100的和
'''
i = 0
s = 1
while s <= 100:
    i = i + s
    s += 1
print(i)
(1+100)*100/2

## 猜数字
import random 
random_num = random.randint(1,10)
num = 0
input_num  = int(input("请您输入您猜测的数字:"))
while input_num != random_num:
    num = num + 1
    if input_num > random_num:
        print("猜大了，您已经猜测%d次，请您再猜一次" % num)
        input_num = int(input("请您输入您猜测的数字:"))
    else:
        print("猜小了，您已经猜测%d次，请您再猜一次" % num)
        input_num = int(input("请您输入您猜测的数字:"))
    print(f"您猜对了，正确答案是{random_num}")