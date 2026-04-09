import pyecharts
### 文件夹functions就是一个库 

### 
from pyecharts.charts import Line
from pyecharts.options import TitleOpts
line = Line()### 创建对象类似于 open
line.add_xaxis(['中国','美国','英国'])
line.add_yaxis("GDP",[30,20,10])
line.render()
###
from pyecharts.charts import Line
line = Line()### 创建对象类似于 open
line.add_xaxis(['中国','美国','英国'])
line.add_yaxis("GDP",[30,20,10])
line.set_global_opts(
    title_opts = TitleOpts(title = 'GDP'))





line.render()
