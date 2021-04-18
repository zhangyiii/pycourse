###### print
print(520) #数字
print("hello, world！")
print(3+1)#表达式
#文件操作
'''
fp = open("C:\workspace\pywork\log.txt", "a+")
print("hello, world", file=fp)
fp.close()
'''
#一行输出
print("zhangyi", 520)

###### 转义字符
print("hello\nworld")
print("hello\tworld")
print(r"hello\tworld") #原字符

###### 变量——（标识（即地址）， 类型， 值）
name = "zhangyi"
print(id(name)) #标识
print(type(name))#类型
print(name)#值
boolvalue = True
print(type(boolvalue))

###### 数据类型转换——将不同的数据类型拼接在一起
'''
str()
int() ： 文字类以及带有小数类的字符串无法转换
float() ：文字类字符串无法转换
'''
a = 5
strValue = "string"
print(strValue + str(a))

###### input 函数
# a = input("输入a：")
# b = input("输入b：")
# print("a + b = " + str(int(a) + int(b)))

###### 运算符优先级
'''
0th: （）括号
1th: 算术运算，先幂运算，后乘除，再加减
2th: 位运算
3th: 比较运算
4th: bool运算
5th: 赋值运算
'''
###### 算术运算
print(11 / 3)
print(11 // 3) #取整
print(-9//2)   #取整：一正一负向下取整
print(11 % 3)  #取余
print(11 % -3) #取余：一正一负要公式——余数=被除数-除数*商
print(2**10)  #幂运算
###### 位运算
'''
& 按位与
| 按位或
>>  << 移位
'''
print(1 << 2)
print(8 >> 1)
###### 比较运算
a = 10
b = 10
print(a==b)         #比较的是值
print(a is b)       #比较的是标识
print(a is not b)   #比较的是标识
###### bool运算 —— and, or, not, in
a, b = 10, 5
print(a == 10 and b == 5)
print(not(a==10))
s = "hello"
print("h" in s)
print("k" not in s)
###### 赋值运算
a = 3 + 4 #从右到左赋值
a = b = c = 10 #链式赋值
a,b,c = a+b, 50, 60 #解包赋值
a, b = b, a #解包赋值——交换
print(a, b , c)

######  python 一切皆对象，bool内建函数
print(bool(""))     #空字符串
print(bool([]))     #空列表
print(bool(list())) #空列表
print(bool(()))     #空元组
print(bool(tuple()))#空元组
print(bool({}))     #空字典
print(bool(dict())) #空字典
print(bool(set()))  #空集合

###### 分支结构
a = 10
if a > 10:
    print("true")
else:
    print("false")

if a >= 5:
    print("true")
elif a <= 10:
    print("true")
else:
    print("error")
print("true" if a == 10 else "false") #条件表达式

###### pass语句——什么都不做，占位符
'''
用在：
if语句的执行体
for-in语句循环体
定义函数的函数体
'''
if a > 10:
    pass #没想好需要做什么，先占位
else:
    pass

###### 循环结构 rang， while， for-in
r = range(10) #rang(stop)
print(list(r))
r = range(1, 10) #rang(start, stop)
print(list(r))
r = range(1, 10, 2)#rang(start, stop, step)
print(list(r))

#循环结构 while for-in中的break， continue
a = 1
sum = 0
while a <= 100:
    if (a%2==0):
        sum += a
        break
    a += 1
print(sum)

for x in range(100): #in后面是可迭代对象，如字符串，序列
    if x%2 == 0:
        sum += x
        continue
print(sum)

for i in range(1, 10):
    for j in range(1, i+1):
        print(i, "*", j, "=", i*j, "\t", end="") #不换行输出 end=""
    print() #换行输出

###### 列表list， 元组tuple， 字典dict, 集合set
'''
不可变序列：字符串，元组， 其没有增、删，改操作，因为对象地址会发生更改
可变序列：列表，字典， 对序列执行增、删，改操作后对象地址不变
'''
''' 列表list '''
l = ["hello", "world", 98, "hello"] #python一切皆引用， list对象存储的是其他对象的引用
l = list(["hello", "world", 98, "hello"])#list内建函数
print(l[0], l[-1])#索引正序0，N-1；索引逆序：-N， -1
print(l.index("hello")) #list的index方法查找指定元素的索引，如果有相同的元素，返回第一个
print(l.index("hello", 0, 3))#查找指定索引范围内的元素的索引
l1 = l[1:3]#切片[start:stop:step], 切片后依然是list对象，step默认是1
l2 = l[::1]#step为正数开始，正序开始
l3 = l[::-1]#step为负数，逆序开始
print("hello" in l)#判断元素是否在列表in, not in
for i in l: #遍历
    pass
l.append(100)#列表尾添加一个元素，元素可以是任何对象
l.append(l1)#列表尾添加一个list对象元素
l.extend(l1)#列表尾添加至少一个元素
l.insert(1, 90)#列表中指定位置添加一个元素
l[1:] = l1#在任意位置添加至少一个元素（切片）,产生新的list对象
l.remove("hello")#删除指定元素，如果重复只删除第一个
l = [1, 2, 3, 4 ,5, 6]
l.pop()#删除最后一个
l.pop(1)#删除指定索引元素
new_list = l[1:3] #切片删除，产生新列表
l[1:3]=[]#切片删除，不产生新列表，用空列表替代
l.clear()#删除列表所有的元素
del l #直接删除列表对象
l1 = [1, 2, 3, 4 ,5, 6]
l1.sort(reverse=True)#默认reverse=False是升序，原列上进行
new_list1 = sorted(l1, reverse=True) #内建sort函数，产生new列表
print(new_list1)
new_list3 = [i*i for i in range(10)] #列表产生式，生成有某种规则的数据
print(new_list3)

''' 字典dict —— key, value, 计算方法：哈希（key）--> value
key是不可变对象，不能用list作为key
'''
dct = {"zhang":10, "wang":100, "li":1000} #创建
dct1 = dict(zhang=10, wang=100, li=1000)#创建
print(dct)
print(dct1)
print(dct["zhang"])
print(dct1["zhang"])
print(dct.get("zhang"))
print(dct.get("yi", 1)) #如果查找不存在则给默认值1
print("zhang" in dct) #判断key是否存在, in, not in
del dct["zhang"] #删除指定的key-value
print(dct)
dct.clear()#删除所有的key-value
print(dct)
dct["yi"] = 1 #新增key-value
print(dct)
dct["yi"] = 100000#修改key-value
print(dct)
print(list(dct1.keys())) #获取所有的key
print(list(dct1.values()))#获取所有的value
print(list(dct1.items()))#获取所有的key-value（构成元组）
for i in dct1: #遍历i是获取字典的key
    print(i, end="\t")
    print(dct1[i], end="\t")
    print()
#字典生成式
a = ["zhang", "li", "wang"]
b = [10,20,30]
new_dict = {i:j for i, j in zip(a, b)}
print(new_dict)
new_dict1 = {i.upper():j for i, j in zip(a, b)} #key变大写
print(new_dict1)

''' 元组tuple 
为什么要设计为不可变序列（没有增、删，改）——多线程下同时操作对象时不需要加锁
【元组中存储的是对象的引用】：
1 如果元组中的对象本身是不可变对象，则不能再引用其他对象
2 如果元组中的对象本身是可变对象，则可变对象的引用不可以改变，但其数据可以改变
'''
t = ("zhang", "yi", 10)
print(t)
t1 = tuple(("zhang", "yi", 10))
print(t1)
t3 = ("zhang", ) #当元组中只有一个元素时，需要在末尾添加逗号
print(t3)
t4 = (10, "zhang", [20,40])
print(t4)
t4[2].append(100)#如果元组中的对象本身是可变对象，则可变对象的引用不可以改变，但其数据可以改变
print(t4)
for itm in t4: #遍历元组
    print(itm)

''' 集合set
集合是可变对象，类似于没有value的字典，也是通过hash找位置, key是不可变对象
集合里面的元素跟dict中元素一样，没有重复的key， 同时元素无序
'''
s = set() #创建空集合
s = {"zhang", 10, "zhang"}
print(s)
s = set([1, 20, 30, 20]) #将列表转为set， 去掉重复元素
print(s)
s = set((1, 20, 30, 20)) #将元组转为set， 去掉重复元素
print(s)
s = set("zhang") #将字符串转为set，去掉重复元素
print(s)
print("zhang" in s) #判断是否再集合中
s.add(10) #添加一个元素
print(s)
s.update({10, 20})#至少添加一个元素
s.update([10, 20])
s.update((10, 20))
print(s)
s.remove(20) #一次删除一个元素，如果元素不存在则报错
s.discard(20) #一次删除一个元素，如果元素不存在不报错
print(s)
s.pop()#一次删除一个任意元素
print(s)
s.clear()#清空集合
print(s)
'''集合关系'''
s1 = {10, 20, 30, 40}
s2 = {1, 2, 10}
print(s2.issubset(s1)) #s2是s1的子集
print(s1.issuperset(s2))#s1是s2的超级
print(s1.isdisjoint(s2))#s1与s2是否相交
'''集合数学运算'''
print(s1.intersection(s2))#s1与s2的交集
print(s1 & s2)
print(s1.union(s2)) #s1与s2的并集
print(s1 | s2)
print(s1.difference(s2)) #s1与s2的差集
print(s1-s2)
print(s1.symmetric_difference(s2))#s1与s2的对称差集
new_set = {i*i for i in range(10)}
print(new_set)

'''字符串
1. 不可变序列
2. 字符串驻留机制——相同字符串只保留一份拷贝，将其字符串地址赋值给不同的变量对象，提升效率节省内存
3. 
'''
a = "python"
b = "python"
print(id(a))
print(id(b)) #字符串驻留机制——相同字符串只保留一份拷贝，将其字符串地址赋值给不同的变量对象

s = "hello, hello"
print(s.index("lo"))
print(s.find("lo")) #查找第一次出现位置
print(s.rindex("lo"))
print(s.rfind("lo"))#查找最后一次出现位置， find/rfind找不到返回-1

print(s.upper()) #所有的字符转大写
print(s.lower()) #所有的字符转小写
print(s.swapcase())#大写变小写，小写变大写
print(s.capitalize())#首字母转大写
print(s.title())#把每一个单词的首字母转换为大写

'''字符串劈分'''
s = "hello|world|python"
print(s.split(sep="|")) #正向按|进行劈分，如果不指定sep则按空格划分，分割后返回list
print(s.split(sep="|", maxsplit=1)) #正向劈分，最大劈分此为为1
print(s.rsplit(sep="|", maxsplit=1))#反向劈分，最大劈分次数为1

'''字符串对齐'''
s = "hello,world"
print(s.center(20, '*')) #字符串占20个空格居中，两边用*填充， 默认以空格填充
print(s.ljust(20, '*'))  #左对齐
print(s.rjust(20, '*'))  #右对齐
print(s.zfill(20))#右对齐，0填充

'''判断字符串操作的方法'''
s = "hello,"
print(s.isidentifier()) #是否是合法的标识符号（标识符由——数字，字母，下划线组成）
print(s.isalpha()) #是否字符串全部由字母组成
print(s.isnumeric())#是否字符串全部由数字组成
print(s.isalnum())#是否字符串全部由字母和数字组成
print(s.isspace())#判断字符串是否全部由空白字符组成（回车，换行，制表符）
'''replace/join'''
s = "hello, world, world, world"
print(s.replace("world", "python")) #将字符串中的world全部替换为python
print(s.replace("world", "python", 2))#将字符串中的2个world替换为python
'''join——将列表或元组中的字符串合成一个字符串'''
lst = ["hello", "world"]
print('|'.join(lst))#链接list采用|
print(' '.join(lst))
print(''.join(lst))
tpl = ("hello", "world")
print('|'.join(tpl))#链接list采用|
print('*'.join("python"))
'''' 字符串比较 == 与 is区别'''
a = "python"
b = "python"
print(a == b) #比较的是对象的值
print(a is b) #比较的是对象的标识id
print(ord("张")) #ord输出b对应的assic值
print(chr(ord("张")))#chr与ord相反
'''字符串切片
1. 字符串是不可变类型，不具有增，删除，改操作
2. 切片操作将产生新的对象
'''
s = "hello, python"
s1 = s[:5] #[start:stop:step]由于没有指定起始地址，默认0开始, 步长默认为1，如果步长为-1，则反方向开始
s2 = s[6:]#由于没有指定结束故一直到末尾
s3 = '!'
print(s1+s3+s2)

'''格式化输出'''
name = "zhangsan"
age = 10
print("我是%s, 今年%d岁" %(name, age)) #使用%占位符跟c++类似
print("我是{0}, 今年{1}岁" .format(name, age)) #使用{}占位
print(f"我是{name}, 今年{age}岁") #使用f-string
print("%10d" %99) #10表示宽度
print("%.3f" %3.1415926) #.3表示精度
print("%10.3f" %3.1415926) #即表示宽度也表示精度
print("{:.3f}" .format(3.1415926))
print("{:10.3f}".format(3.1415926))

'''字符串编码、解码传输
1 编码：字符串到二进制数据
2 解码：二进制到字符串
'''
s = "咋了"
print(s.encode(encoding='GBK')) #采用GBK编码一个中文占2个字节
byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))#解码
print(s.encode(encoding='UTF-8')) #采用UTF-8编码一个中文占3个字节
byte = s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))#解码


