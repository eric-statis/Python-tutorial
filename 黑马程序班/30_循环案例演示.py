'''
某公司账户有1w元，给20名员工发工资。
员工编号1-20，从编号1开始，依次领取工资，每个人可领取1000元。
领工资时，财务会判断员工的绩效等级，如果绩效等级低于5，不发工资，换下一位
如果工资发完了，结束发工资
'''
import random
deposit = 10000
member = 20
count = 0 
for count in range(1,21):
    print(f"第{count}位员工开始发工资，开始判断绩效等级。")
    if deposit > 0:
        if random.randint(1,10) < 5 :
            print("等级低于5，不发绩效。")
            continue
        else:
            deposit = deposit -1000
            print(f"等级高于5，发绩效1000元，账户余额为{deposit}元。")
    else:
        print(f"工资余额不足，共发放了{count}人，余额为{deposit}元。")
        break