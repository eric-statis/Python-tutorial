### 知识点print打印不换行
print("我爱你",end='')
print("qixia",end='')

### 制表符t
print("Hello \tWorld")
print("Hello \tSnake")

### 通过while循环输出99 乘法表
i = 1
j = 1
while j <= 9:
    while i <= j:
        print(f"\t {i}*{j}",end='')
        i = i + 1
    i = 1
    j = j +  1
    print()## 换行
