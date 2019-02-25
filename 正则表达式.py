# class MyClass:
#     """一个简单的类实例"""
#     i = 12345
#
#     def f(self):
#         return 'hello world'
#
#
# # 实例化类
# x = MyClass()
#
# # 访问类的属性和方法
# print("MyClass 类的属性 i 为：", x.i)
# print("MyClass 类的方法 f 输出为：", x.f())


# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
# x = Complex(3.0, -4.5)
# print(x.r, x.i)   # 输出结果：3.0 -4.5

# 类定义
# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
#
# # 实例化类
# p = people('runoob', 10, 30)
# p.speak()

# import random
# class Sj:
#     count = 10
#     start = 0
#     end = 100
#     def __init__(self,count,start,end):
#         self.count = count
#         self.start = start
#         self.end = end
#     def show(self):
#         a = list()
#         for i in range(self.count):
#             a.append(str(random.randint(self.start,self.end)))
#         a = ' '.join(a)
#         print(a)
# x=Sj(5,4,14)
# x.show()

import uuid
import pickle
class Car():
    def __init__(self,id,mark,color,owner):
        self.id = uuid.uuid4().hex
        self.mark = mark
        self.color=color
        self.owner=owner


class CarInfo:
    cars={}
    def __init__(self):
        pass

    def add_car(self,car:Car):
        self.cars[car.id]=car.mark,car.color,car.owner

    def query_by_mark(self,mark):
        showlist=[]
        for k,v in self.cars.items():
            if mark == v[0]:
                showlist.append(k,v[1],v[2])

c1=Car('BMW','red','xy')
carinfo=CarInfo( )






