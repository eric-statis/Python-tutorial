#
from calendar import c
import imp


num = 1 + 1 
str = '面板数据的特点是，有%.2f维度' % num
print(str)

print("1+1的运算结果是：%d" % 2)
print("5+1的运算结果是: %.2f" %1.2)
print("字符串在python中的类型是：%s" % type('字符串'))

a,b,c = '传智播客','003032','19.99'
print(f"公司：{a}，股票代码{b}，当前股价{c}")

print("每日的增长系数：%.1f，经过%d天的增长后，估计达到了：%4.2f" % (1.2,7,71.63))

