# #
# while True:
#     num1 = input("请输入第一个数字：")
#     num2 = input("请输入第二个数字：")
#     try:
#         num1 = int(num1)
#         num2 = int(num2)
#         result = num1 + num2
#         print(result)
#
#     except ValueError:
#         print("值错误")
#     except SyntaxError:
#         print("2231ji ")
#     except Exception as e:
#         print("出现异常：")
#         print(e)

### try...else用法 类似for else和while else 循环结束执行
#这里是没发生异常执行 可以做代码检查 如果没发生异常就会走这里
#
# while True:
#     num1 = input("请输入第一个数字：")
#     num2 = input("请输入第二个数字：")
#     try:
#         num1 = int(num1)
#         num2 = int(num2)
#         result = num1 + num2
#         print(result)
#
#     except ValueError:
#         print("值错误")
#     except SyntaxError:
#         print("2231ji ")
#     except Exception as e:
#         print("出现异常：")
#         print(e)
#     else:
#         print("你真棒")
### finally
## 无论是否出错一定会走这里

### raise主动触发异常
while True:
    num1 = input("请输入第一个数字：")
    num2 = input("请输入第二个数字：")
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
        print(result)
        raise ImportError ### 运行到这里 主动报错

    except ValueError:
        print("值错误")
    except SyntaxError:
        print("2231ji ")
    except Exception as e:
        print("出现异常：")
        print(e)
    else:
        print("你真棒")
