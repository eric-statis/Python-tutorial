'''
def test_return():
return 1, 2
x, y = test_return()
print (x)
＃ 结果1
print (y)
＃ 结果2
'''
def print_my():
    return 1,2,'hello'
print_my()
x,y,z = print_my()
print(x,y,z,end=' ')
