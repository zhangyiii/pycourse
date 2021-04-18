'''class'''
class Strudent: #Strudent类对象——第一个字母大写，其余小写
    var = 10 #直接写在内中的变量称为——类属性（被所有的实例对象共享， 使用Strudent类对象调用修改）
    def __init__(self, name, age): #——实例对象初始化方法
        self.name = name #self.name——实例对象属性
        self.age = age

    def fun(self): #——实例对象方法
        print("方法")

    @staticmethod
    def static_fun(): #——静态方法（使用Strudent类对象调用）
        print("静态方法")

    @classmethod
    def class_fub(cls): #——类方法(使用Strudent类对象调用)
        print("类方法")

print(id(Strudent))
print(type(Strudent))
print(Strudent)

obj = Strudent("zhang", 20) #Strudent类的实例对象
print(id(obj))
print(type(obj))
print(obj)
Strudent.static_fun()
Strudent.class_fub()

'''动态绑定属性和方法
1. python是动态语言，在创建对象后可以动态绑定属性和方法
2. 一个类可以创建N个类的实例对象，每个实例对象的类指针指向类对象， 同时每个实例对象的属性值不同
'''
stu1 = Strudent("zhang", 20)
stu2 = Strudent("wang", 25)
stu1.gender = "female" #动态绑定属性gender
print(stu1.name, stu1.age, stu1.gender)
def fun_dynamic():
    print("fun_dynamic")
stu1.fun_dynamic = fun_dynamic #动态绑定属性方法fun_dynamic
stu1.fun_dynamic()

'''类的3大属性：封装、继承、多态
1. 封装——提高安全性
2. 继承——提高复用性
3. 多态——提高可扩展和可维护性
4. 由于python中没有专门修饰符用于属性的私有，如果不希望属性被类外部被访问则在加__
'''
class TestClass:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #不希望属性被类外部被访问则在加__, 但是可以通过特殊方式访问
t1 = TestClass("zhang", 20)
print(t1.name)
'''继承
1. 如果一个类没有继承任何类，则默认继承object
2. python支持多继承
3. 定义子类时，必须在其构造函数中调用父类的构造函数
'''
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_A(self):
        print("A class: ", self.name, self.age)
    def func(self):
        print("func in class A")

class B:
    def __init__(self, id, type):
        self.id = id
        self.type=type
    def show_B(self):
        print("B class: ", self.id, self.type)

class C(A, B): #多继承
    def __init__(self, name, age, gender, id, type):
        A.__init__(self, name, age) #初始化父类A的构造函数 ——针对多继承
        B.__init__(self, id, type) #初始化父类B的构造函数  ——针对多继承
        self.gender = gender
    def show_C(self):
        print("C class: ", self.gender)

class D(A): #单继承
    def __init__(self, name , age, address):
        super().__init__(name, age) #初始化父类A的构造函数 ——针对单继承
        self.address = address
    def show_D(self):
        print("D class: ", self.address)
    def func(self): #方法重写
        A.func(self) #调用A类的func ——针对多继承
        super().func() #调用A类的func——针对单继承
        print("func in class D")

obj_c = C("zhang", 20, "male", 1992, 10)
obj_c.show_A()
obj_c.show_B()
obj_c.show_C()
objc_d = D("zhang", 20, "xxxx")
objc_d.show_D()
objc_d.func()
'''object类
1. object类是所有类的默认父类，因此所有的类都有object类的属性和方法
2. 使用内置函数dir()可以查看指定对象所有的属性和方法
3. object有一个__str__()方法，用于返回一个对于该对象的描述信息，帮助查看对象的信息，所以我们经常对__str__()方法进行重写
'''
class DefClass:
    pass
obj = DefClass
print(dir(obj))
print(obj) #输出：<class '__main__.DefClass'>
class DefClass_S:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self): #重写，输出对象的描述信息
        return "name = {0}, age = {1}".format(self.name, self.age)
obj = DefClass_S("zhang", 20)
print(obj) #输出：name = zhang, age = 20
'''特殊属性和特殊方法
1. 用于查看相关信息
2. 重写自定义内的操作符及方法，如__add__()、__len()__
3. __new__() ——用于创建对象
4. __init__()——用于对创建的对象进行初始化
'''
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self, name, age):
        self.name = name;
        self.age = age
x = C("zhang", 20)
print(x.__dict__) #返回对象实例的属性字典
print(C.__dict__) #返回实例对象的属性字典

'''赋值、浅拷贝和深拷贝
赋值： 只是形成2个变量，实际上还是指向同一个对象
浅拷贝：使用copy模块中的copy(), python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此源对象与拷贝对象会引用同一个子对象
深拷贝：使用copy模块中的deepcopy()函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同 
'''
