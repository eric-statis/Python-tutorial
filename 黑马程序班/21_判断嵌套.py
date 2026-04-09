# 动物园案例
if int(input("您的身高是：？")) >= 120:
    print("您不可以免费游玩。")
    print("但如果您的vip等级大于3则可免费游玩。")
    if int(input("请输入您的vip等级：")) > 3:
        print("您可以免费游玩。")  
    else:
        print("您不可以免费游玩。")
else:
    print("您可以免费游玩。")
         
# 公司发放礼物。
age = 30
if int(input("请输入您的年龄：")) > age:
    if int(input("请输入您的入职时间：")) >2 :
        print("OK")
    elif int(input("请输入您的级别")) >3:
        print("OK")
    else:
        print("虽然您年龄合适，但不能领取。")    
else:
    print("年龄不够，不可领取。")
