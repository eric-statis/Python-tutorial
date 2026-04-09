'''
1．設计一个类，可以完成数据的封装
2. 設计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3．读取文件，生产数据对象
4. 进行数据需求的逻辑计算（计算每一天的销售额）
5.通过PyEcharts进行图形绘制
'''

# with open("数据开发/data/2011年1月销售数据.txt",mode='r',encoding="utf-8") as f:
#     f.readlines()

# with open("数据开发/data/2011年2月销售数据JSON.txt",mode='r',encoding="utf-8") as f:
#     f.read()

from utilis.file_define import TxtFileReader,JsonFileReader
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.options import *
'''
# from 第一层.第二层.文件名 import 类名
from utilis.file_define import TxtFileReader, JsonFileReader

'''
txt_file = TxtFileReader('data/2011年1月销售数据.txt')
json_file = JsonFileReader('data/2011年2月销售数据JSON.txt')
jan_data = txt_file.read_data()
feb_data = json_file.read_data()
all_data = jan_data + feb_data

### 读数据
my_dict = {}
for record in all_data:
    if record.date in my_dict.keys():
        my_dict[f'{record.date}'] += record.money
    else:
        my_dict[f'{record.date}'] = record.money

### 可视化
bar = Bar(init_opts=InitOpts(theme = ThemeType.WHITE))## 内部可以填写构造方法 其中还有注解：
bar.add_xaxis(list(my_dict.keys()))
bar.add_yaxis("销售额",list(my_dict.values()))
bar.set_global_opts(
    title_opts=TitleOpts(title = "每日销售额"),

)
bar.render()

