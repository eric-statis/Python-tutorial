def func1():
    print("函数1执行")
    1/0
    

def func2():
    print("函数2执行")
    func1()
    
    
def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常{e}")

main()