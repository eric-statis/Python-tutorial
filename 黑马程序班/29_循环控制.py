## break and continue 循环中断语句
for i in range(4):
    print("语句1")
    continue
    print("语句2") # 跳过本次循环 

for i in range(100):
    print("bbb")
    for j in range(5):
        print("good")
        continue
        print("bad")

for i in range(100):
    print("bbb")
    for j in range(5):
        print("good",end=" ")
        break
        print("bad")

for i in range(1,100):
    print(1)
    for j in range(1,5):
        print(2)
        break