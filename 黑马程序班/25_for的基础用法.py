### for循环更像是一种遍历
for i in 'heima':
    print(i,end='')

### 数一数有几个a
name = 'itheima is a brand of itcast'
count = 0
for i in name:
    if i == 'a':
        count += 1
print(count)