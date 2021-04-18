'''
自定义模块
'''

def add_cust(a, b):
    return a + b

def div_cust(a, b):
    return a / b

if __name__ == '__main__':
    print(add_cust(100, 20)) #以主程序方式运行， 只有当点击customModule.py时才会被执行运算
