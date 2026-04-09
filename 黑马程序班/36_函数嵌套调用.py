# 函数的嵌套调用是指 一个函数里又嵌套另一个函数
def func_1():
    print("---1---")

def func_2():
    print("---2---")
    func_1()

func_2()