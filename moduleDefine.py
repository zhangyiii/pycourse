'''模块
1. 一个扩展名为.py的文件就是一个模块
2. 一个模块中包含n多个函数及类
3. 模块的好处：方便其它程序和脚本的导入并使用， 避免函数名和变量名称冲突，提高代码的可重用和可维护性
'''
'''导入模块
1. import 模块名称 [as 别名] ——导入所有
2. from 模块名称 import 函数/变量/类 ——导入指定
'''
import math
print(id(math))
print(type(math))
print(math)
print(dir(math))
print(math.pi)
print(math.__doc__) #描述信息

from math import pi
print(pi)

import customModule
print(customModule.add_cust(10, 20))

import customPackage.module_A as cm
from  customPackage.module_A import add_cust
print(cm.add_cust(10, 20))
add_cust(10,200)

'''python中常用的内置模块
1. sys:     与python解释器及其环境操作相关的标准库
2. time:    提供与时间相关的各种函数的标准库
3. os:      提供访问操作系统服务的标准库
4. calendar：提供与日期相关的各种函数的标准库
5. urllib:  用于读取来自网上的数据标准库
7. json：    用于使用JSON序列化和反序列化对象
8. re:      用于在字符串中执行正则表达式匹配和替换
9. math：    提供标准算术运算函数的标准库
10.decimal： 用于进行精确控制运算精度、有效数位和四舍五入操作的十进制运算
11.logging:  提供灵活的记录事件、错误、警告、调试信息等日志信息功能 
'''
import time
print(dir(time))
print(time.time())
print(time.localtime(time.time()))
import urllib.request
print(urllib.request.urlopen("http://www.baidu.com").read())


