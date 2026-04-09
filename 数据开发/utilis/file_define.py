from 数据开发.utilis.data_define import Record
class FileReader:
    path: str = None

    def __init__(self,path: str):
        self.path = path

    def read_data(self)-> list[Record]:
        '''把文件中数据转化为Record类，并放在一个列表内储存'''
        pass

### 抽象类的具体实现
class TxtFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    ### 实现抽象方法
    def read_data(self) -> list[Record]:
        my_list = []
        f = open(self.path, mode= 'r', encoding= 'utf-8')
        for lines in f.readlines():
            lines: str = lines.strip()
            lines = lines.split(',')
            lines = Record(date = lines[0], order_id=lines[1], money=int(lines[2]),province=lines[3])
            my_list.append(lines)
        f.close()    
        return my_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path
    
    def read_data(self) -> list[Record]:
        import json
        my_list = []
        f = open(self.path,mode="r",encoding='utf-8')
        for lines in f.readlines():### 代码提示很有用 输出是list[str]
            lines = json.loads(lines)
            lines = Record(
                date = lines['date'],
                order_id=lines['order_id'],
                money=int(lines['money']),
                province=lines['province'])
            my_list.append(lines)
        f.close()
        return my_list
    
if __name__ == '__main__':
    result = TxtFileReader('data/2011年1月销售数据.txt')
    r = result.read_data()
    for i in r:
        print(str(i))


if __name__ == '__main__':
    a = JsonFileReader('data/2011年2月销售数据JSON.txt')
    a = a.read_data()
    for i in a:
        print(str(i))



