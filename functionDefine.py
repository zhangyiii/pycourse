'''函数参数传递
1. 实参和形参按位置顺序传递
2. 实参和形参按关键字传递（可以非顺序）
'''
def cal(a, b):
    c = a + b
    return c
res = cal(10, 20) #实参和形参按位置顺序传递
print(res)
res = cal(b=10, a=20)#实参和形参按关键字传递（可以非顺序）
print(res)

'''个数可变的位置形参、个数可变的关键字参数
个数可变的位置参数：
1. 事先不知道传入的位置参数个数
2. 使用*定义
3. 其为传入的是一个元组
个数可变的关键字参数：
1. 事先不知道传入的关键字参数个数
2. 使用**定义
3. 其传入的是一个字典
'''
def fun(*args):
    print(args, type(args))
def fun1(**kwargs):
    print(kwargs, type(kwargs))
fun(10)
fun(10, 20)
fun(10, 20, 30) #个数可变的位置参数
fun1(a=10, b=[20,30,40])
fun1(a=10, b={"zhang":10, "yi":20}, c=[10, 30,40])#个数可变的关键字参数
# def fun(*args, *args) #error, 只能定义一个位置可变的形式参数
# def fun(**kwargs, **kwargs) #error, 只能定义一个关键字可变的形式参数
# def fun(**kwargs, *args): #error, 如果定义1个可变的位置形参和一个可变的关键字形参，则可变的位置形参需要放前面
def fun2(*args, **kwargs):
    pass

'''函数返回值
1. 没有返回，return省略
2. 有1个返回值，则返回原值
3. 有多个返回值，则返回元组
4. 传递给形式参数是可变对象，如果函数体内对齐修改，则实参也会发生相应修改，否则不会
'''
def func3(a, b, c):
    print(a, b, c)
    a = 100
    c.append(10)
    ret1 = []
    ret2 = []
    for i in b:
        if (i % 2 == 0):
            ret1.append(i)
        else:
            ret2.append(i)
    return ret1, ret2

a = 10;
b = {i for i in range(10)}
c = [1, 2, 3]
print(a, b, c)
ret = func3(a, b, c)
print(a, ret, c)

'''函数参数传递规则'''
def fun4(a, b, c):
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
fun4(10, 20, 30) #位置传递参数
lst = [10, 20, 30]
# fun4(lst) #error
fun4(*lst)#列表对象前加一个*， 列表中的每个元素都转换为位置参数传递
fun4(a=10, b=20, c=30) #关键字传递参数
dst = {"a":10, "b":20, "c":30}
# fun4(dst) #error
fun4(**dst)#字典对象前加2个*， 字典中的每个元素都转换为关键字参数传递
#==========================================================
def fun5(a, b, c, d):
    pass
fun5(10, 20, 30, 40)
fun5(a=10,b=20,c=30,d=40)
fun5(10, 20, c=30, d=40) #前2个采用位置参数传递，后2个采用关键字参数传递
def fun6(a, b, * , c ,d):
    pass
# fun6(10, 20, 30, 40)#error, 函数形式参数中*前面必须是位置参数传递，*后面必须是关键字参数传递
fun6(10, 20, c=30, d=40)
'''参数顺序问题'''
def fun7(a, b, *, d, **kwargs):
    pass
def fun8(a, b=20, *args, **kwargs):
    pass

'''函数的全局和局部变量
1. 函数外部声明的变量为全局变量
2. 函数内部声明的变量为局部变量，如果在函数内局部变量前面添加global，则为全局变量
'''
name = 10 #函数外部声明的变量为全局变量
def fun9():
    global gvar #函数内部声明的变量为局部变量，如果在函数内局部变量前面添加global，则为全局变量
    gvar = 20
    print(name)
fun9()
print(gvar)

'''递归函数
1.优点：简单
2.缺点：消耗内存，需要在栈中压入函数栈帧
'''
def rev_fun(num):
    if num==1:
        return num
    return num * rev_fun(num-1)
print(rev_fun(6))

def fib_fun(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return fib_fun(num-1) + fib_fun(num-2)
print(fib_fun(6))
lst = []
for i in range(1, 7):
    lst.append(fib_fun(i))
print(lst)

#=========================================================================
'''异常处理机制
1. try-except
2. try-except-else
3. try-except-else-finally
4. 常见的异常处理类型：
#： ZeroDivisionError    除0
#： IndexError           序列中没有此索引
#:  KeyError             映射中没有这个key
#:  NameError            没有声明
#： SyntaxError Python   语法错误
#:  valueError           传人无效的值         
'''
#1. try-except
try:
    pass
except ZeroDivisionError: #异常处理类型1：ZeroDivisionError
    pass
except ValueError: #异常处理类型2：ZeroDivisionError
    pass
except BaseException:#异常处理类型3：ZeroDivisionError
    pass
#2. try-except-else
try:
    pass
except ZeroDivisionError: #异常处理类型1：ZeroDivisionError
    pass
except ValueError: #异常处理类型2：ZeroDivisionError
    pass
except BaseException:#异常处理类型3：ZeroDivisionError
    pass
else:
    pass #try中没有错，则执行到else
#3. try-except-else-finally
try:
    pass
except ZeroDivisionError: #异常处理类型1：ZeroDivisionError
    pass
except ValueError: #异常处理类型2：ZeroDivisionError
    pass
except BaseException:#异常处理类型3：ZeroDivisionError
    pass
else:
    pass #try中没有错，则被执行
finally:
    pass #无论是否产生错误都被执行
'''traceback模块'''
import traceback
try:
    a=20
    b=30
    print(a, b)
except:
    traceback.print_exc()

