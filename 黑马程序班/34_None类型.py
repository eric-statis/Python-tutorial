### 函数没有return，函数也有返回值None
def say_hello():
    print("Hello")

result = say_hello()
print(f"无返回值值函数，返回的内容是{say_hello()},\n返回的类型是{type(say_hello())}")

### 在if判断时，None相当于False
def check_age(age):
    if age > 18:
        result = 'ok'
        return result
    else:
        return None
result = check_age(20)
if not result:
    print("未成年")