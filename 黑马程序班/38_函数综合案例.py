def bank():
    print("周杰伦你好，欢迎您来到黑马银行，请选择您的操作。")
    num = int(input("查询余额 \t[输入1]\n存款 \t\t[输入2]\n取款\t\t[输入3]\n退出\t\t[输入4]\n请输入您的选择："))
    if num == 1:
        print("1")
    elif num == 2:
        print("2")
    elif num == 3:
        print("3")
    else:
        print("4")
    


### 定义全局变量
money = 5000000
name = None

### 客户输入名字
name = input("请输入您的姓名：")

### 定义查询函数
def query(show_head):
    if show_head:
        print("---------查询余额---------")
    print(f"{name}您好，您的存款余额为{money}元。")

### 存款函数
def saving(num):
    global money
    money += num
    print("---------存款---------")
    print(f"{name}您好，您的存款{num}元。")
    query(False)

###  定义取款函数
def get_money(num):
    global money
    money -= num
    print("---------取款---------")
    print(f"{name}您好，您的取款余额为{money}。")

### 主菜单函数
def main():
    print("---------主菜单---------")
    print(f"您好，{name}，欢迎来到黑马atm，请选择操作：")
    print("查询余额\t[请输入1]")
    print("存款\t\t[请输入2]")
    print("取款\t\t[请输入3]")
    print("退出\t\t[请输入4]")
    return input("请输入您的选择：")

while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = int(input("请输入您要存款的金额："))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("请输入您要取款的金额："))
        get_money(num)
        continue
    else:
        break