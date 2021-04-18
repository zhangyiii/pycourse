'''常用工具'''
'''编码格式
1. ASCII码作为base
2. Unicode：定长编码，2个字节表示1个字符，Python的解释器使用的时Unicode（内存）
3. UTF-8: 变长编码，1--4个字节表示1个字符，英文1个字节，中文3个字节 （外存）
4. GBK:中文字符编码
5. python文件的编码格式（外存上）为UTF-8, 可以通过在python文件上方编写#encoding=[gbk]进行更改
6. with语句——上下文管理器：with语句可以自动管理上下文资源，不论什么原因跳出with块，都能确保文件正确关闭，以此来达到释放资源的目的
'''
file = open("log.txt", 'a+')
file.write("zhangyi")
file.close()

'''with 对象 as 名称：'''
with open("log.txt", 'r') as file: #可以不用写close
    print(file.read())

'''自定义对象具有上下文管理功能'''
class MyContext:
    def __enter__(self): #需要实现
        print("enter方法——进入时调用")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):#需要实现
        print("exit方法——退出时调用")

    def show(self):
        print("show")
with MyContext() as a:
    a.show()

'''os模块
1. os模块与os.path模块用于对目录或文件进行操作
2. 不同的系统上运行可能得到的结果不同
3. os模块中操作目录相关函数
getcwd():           返回当前工作目录
listdir():          返回指定路径下的文件和目录信息
mkdir(path[,mode]): 创建目录
makedirs():         创建多级目录
rmdir():            删除目录
removedirs():       删除多级目录
chdir(path):        将path设置为当前工作目录  
4. os.path模块中操作目录相关函数
abspath(path): 获取文件或目录的绝对路径
exists(path): 用于判断文件或目录是否存在，如果存在返回True
join(path, name): 将目录与目录或者文件名拼接起来
splitext(): 分离文件名和扩展名
basename(path): 从一个目录中提取文件名
dirname(path): 从一个路径中提取文件路径，不包括文件名称
isdir(path): 用于判断是否为路径 
'''
import os
# os.system("notepad.exe") #打开记事本
# os.system("calc.exe") #打开计算器
#直接调用可执行文件
# os.startfile("C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
print(os.getcwd()) #返回当前目录

import os.path as op
print(op.basename("C:\workspace"))
