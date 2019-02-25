# class Classname:
#     @staticmethod
#     def fun():
#         print('静态方法')
#
#     @classmethod
#     def a(cls):
#         print('类方法')
#
#     # 普通方法
#     def b(self):
#         print('普通方法')
#
#
#
# Classname.fun()
# Classname.a()
#
# C = Classname()
# C.fun()
# C.a()
# C.b()

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     @property #getter方法
#     def name(self):
#         return self._name
#
#     @name.setter  #在setter方法中可以约束属性,非str将捕获一个type错误
#     def name(self,name):
#         if not isinstance(name, str):
#             raise TypeError("Expected a string")
#         self._name = name
#
# p = Person('tom')
# print(p.name)

# class Cat:
#     name='猫'
#     age=1
#     def __init__(self,n,a):
#         self.name=n
#         self.agea=a
#     def shut(self):
#         print('{} {}岁了'.format(self.name,self.age))
#
#
# class Dog(Cat):
#     def __init__(self,n,a,b):
#         Cat.__init__(self,n,a)
#         self.shout=b
#
#
# p=Dog('dd','1','wang')
# print(p.name,p.age,p.shout)
# p.shut()

# class Cat:
#     name='猫'
#     age=1
#     def shut(self):
#         print('{} {}岁了'.format(self.name,self.age))
#
#
# class Dog:
#     def __init__(self,b):
#         self.shout=b
#     def show(self):
#         print(self.shout)
#
#
#
# class Zz(Cat,Dog):
#     def asd(self):
#         print('asd')
# p=Zz('wang')
# print(p.name,p.age,p.shout)
# p.shut()
# p.show()
# p.asd()
# print(Zz.__bases__)

# class Cat:
#     name='猫'
#     age=1
#     def shut(self):
#         print('{} {}岁了'.format(self.name,self.age))
#
#
# class Dog(Cat):
#     def __init__(self,b):
#         self.shout=b
#     def show(self):
#         print('{}{}叫 '.format(self.name,self.shout))
#
# p=Dog('wang')
# print(p.name,p.age,p.shout)
# p.show()
# p.shut()

import math
import json
import pickle
import msgpack

class Shape:
    @property
    def area(self):
        raise NotImplementedError

class Jx(Shape):
    def __init__(self,chang,kuan):
        self.chang=chang
        self.kuan=kuan
    @property
    def area(self):
        return self.chang*self.kuan

class Sjx(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    @property
    def area(self):
        p=(self.a+self.b+self.c)/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
# def wrapper(cls):
#     def wrap(self):
#         dict=json.dumps(self.__dict__)
#
#     return wrap
# @wrapper
def SerializableCircle(cls):
    def dumps(self, t='json'):
        if t == 'json':
            return json.dumps(self.__dict__)
        elif t == 'msgpack':
            return msgpack.packb(self.__dict__)
        elif t == 'pickle':
            with open('dump.txt', 'wb') as f:
                return pickle.dump(self.__dict__, f)
        else:
            raise NotImplementedError('没有实现的序列化')

    cls.dumps = dumps
    return cls
@SerializableCircle
class Yuan(Shape):
    def __init__(self,r):
        self.r=r
    @property
    def area(self):
        return math.pi*self.r**2
p=Yuan(4)
print(p.area)
p=Jx(4,3)
print(p.area)
p=Sjx(5,4,3)
print(p.area)






