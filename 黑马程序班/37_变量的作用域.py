def test():
    num = 100
    print(num)

print(num)


### global and local
num = 100 # global
def change_num():
    num = 200 # local 和外面没关系
change_num()
print(num)

### 通过global关键字声明是全局变量
num = 100
def change_num():
    global num
    num = 200
    print(f"现在是{num}。")
change_num()
print(num)





