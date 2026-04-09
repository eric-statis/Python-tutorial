f = open(r'./txt/1.txt',mode='r',encoding='utf-8')
### 读取
f.read()
###
a = f.readlines()
a
###
a = f.readline()# 只读一行
a
### 使用for循环读取文件的每一行
for i in open('./txt/bill.txt',mode='r',encoding='utf-8'):
    print(i)

### 文件的关闭
f.close() #解除对于文件的占用

### with open 实现自动关闭文件
with open(r'txt/bill.txt',mode='r',encoding='utf-8') as f:
    print(f.readlines())
    
### 练习题
count = 0
f = open(r'./txt/word.txt',mode='r',encoding='utf-8')

while True:
    word = f.readline().split(' ')
    for i in word:
        if i == 'itheima':
            count += 1
    if word == ' ':
        break
print(count)

count = 0
with open(r'./txt/word.txt', mode='r', encoding='utf-8') as f:  # 使用 with 自动关闭文件
    while True:
        line = f.readline()
        if line == '':  # 正确判断文件结束（空字符串）
            break
        words = line.split(' ')
        for i in words:
            if i.strip() == 'itheima':  # strip() 移除换行符/空格
                count += 1
print(count)

f = open(r'./txt/word.txt',mode='r',encoding='utf-8')
f = f.read()
f.count('itheima')

count = 0
for i in  open(r'./txt/word.txt',mode='r',encoding='utf-8'):
    line = i.strip()
    line = line.split(' ')
    for j in line:
        if j == 'itheima':
            count += 1
print(count)
f.close()
### 还有一种方法
f = open(r'./txt/word.txt',mode='r',encoding='utf-8')
f.read().count('itheima')
    
### 文件写入 w模式源文件存在会清空 不存在会创建

f = open(r'./txt/word_1.txt',mode='w',encoding='utf-8')
f.write('woaini\nniaiwoma')
f.write('nihao')

f.flush()
f.close()
### 文件的追加
f = open(r'./txt/word.txt',mode='a',encoding='utf-8')
f.write('woaini\nniaiwoma\nhahaha')
f.flush()
f.close()