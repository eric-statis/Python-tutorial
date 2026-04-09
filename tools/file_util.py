'''
tools.file_util: 用于处理文件的工具模块
'''


def print_file_info(s:str):
    '''
    print_file_info: 接收传入文件的路径，打印文件的全部内容，如果文件不存在捕捉异常，输出提示信息，通过finally关闭文件对象
    
    :param s: 文件地址
    :type s: str
    '''
    try:
        f = open(s,mode='r',encoding='utf-8')
        print(f.read())### 方法返回一个值不修改
    except:
        print("文件异常")


def append_to_file(name:str,data:str):
    '''
    接受传入文件路径，追加内容
    :param name: 文件路径
    :type name: str
    :param data: 传入内容
    :type data: str
    '''
    f = None
    try:
        f = open(name,mode='a',encoding='utf-8')
        f.write(data)
    except Exception as e:
        print(f"文件追加异常报错{e}")
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    print_file_info('txt/bill.txt')
    append_to_file('txt/test_append.txt','hahaha')





if __name__ == '__main__':
    print_file_info('./txt/bill.txt')





