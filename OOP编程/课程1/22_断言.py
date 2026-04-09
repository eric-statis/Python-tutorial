"""
assert 断言示例：
- 条件为 True：程序继续执行
- 条件为 False：抛出 AssertionError
"""

# 示例1：最基础用法
assert 1 == 1
print("示例1通过：1 == 1")


# 示例2：带错误提示信息
def check_score(score):
    assert 0 <= score <= 100, f"分数必须在 0~100 之间，当前是 {score}"
    return f"合法分数：{score}"


print("示例2通过：", check_score(88))
try:
    check_score(120)
except AssertionError as e:
    print("示例2失败：", e)


# 示例3：函数参数类型校验
def interface(name, age, sex):
    assert isinstance(name, str), "name 必须是字符串"
    assert isinstance(age, int), "age 必须是整数"
    assert isinstance(sex, str), "sex 必须是字符串"
    print("示例3通过：", name, age, sex)


interface("张三", 20, "男")
try:
    interface(20, 20, 20)
except AssertionError as e:
    print("示例3失败：", e)


# 示例4：数据状态校验（列表不能为空）
def first_item(items):
    assert len(items) > 0, "列表不能为空"
    return items[0]


print("示例4通过：", first_item(["a", "b", "c"]))
try:
    first_item([])
except AssertionError as e:
    print("示例4失败：", e)


# 示例5：类中的断言（对象状态合法）
class Account:
    def __init__(self, balance):
        assert balance >= 0, "初始余额不能为负数"
        self.balance = balance

    def withdraw(self, money):
        assert money > 0, "取款金额必须大于0"
        assert self.balance >= money, "余额不足"
        self.balance -= money
        return self.balance


acc = Account(100)
print("示例5通过：取款后余额", acc.withdraw(30))
try:
    acc.withdraw(100)
except AssertionError as e:
    print("示例5失败：", e)
