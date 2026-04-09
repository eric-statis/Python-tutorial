for i in range(10):
    print(i)

for i in range(5,10):
    print(i,end="")

for i in range(5,10,2):
    print(i)

### 打印99 乘法表
for j in range(1,10):
    for i in range(i,j):
        print(f"{i}*{j}",end=' ')   
    i = 1
    print()

## 练习题：计算偶数的个数
import random as random
num = random.randint(1,1000)
count =  0
for i in range(1,num):
    if i%2 == 0:
        count += 1
print(count,num)




