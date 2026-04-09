# 字符串工具
def str_reverse(s:str):
    '''
    str_reverse: 将一个字符串翻转

    :param s: 说明
    :type s: str
    '''
    s_reverse = s[::-1]
    return s_reverse

def substr(s:str,x:int,y:int):
    '''
    substr: 用于对字符串进行切片
    
    :param s: 说明
    :type s: str
    :param x: 说明
    :type x: int
    :param y: 说明
    :type y: int
    '''
    a = s[x:y]
    return a


if __name__ == '__main__':
    print(substr('黑马程序员',1,3))
    print(str_reverse('黑马程序员'))
