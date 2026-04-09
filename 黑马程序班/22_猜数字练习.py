###
import random
num  = random.randint(1,10)
guess_num = int(input("请输入您要猜测的数字："))
if guess_num == num:
    print("恭喜您才对了")    
else:
    if  guess_num > num  :
        print("很抱歉，猜的太大")
    else:
        print("很抱歉，猜的太小")
    guess_num = int(input("请输入您要猜测的数字："))
    if  guess_num == num:
        print("恭喜您才对了")
    else:
        if guess_num > num :
            print("很抱歉，猜的太大")
        else:
            print("很抱歉，猜的太小")
        guess_num = guess_num = int(input("请输入您要猜测的数字："))

        if guess_num == num :
            print("恭喜您才对了")
        else:
            print(f"机会用完了，答案是{num}")
