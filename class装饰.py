import datetime
import time
import functools

# def asd(fn):
#     def wrap(*args,**kwargs):
#         start = datetime.datetime.now()
#         result = fn(*args,**kwargs)
#         end = datetime.datetime.now()
#         delatime = (end - start).total_seconds()
#         print('{} use {}'.format(fn.__name__,delatime))
#         return result
#     return wrap
# @asd
# def add(x,y):
#     time.sleep(2)
#     return x + y
# print(add(1,2))



# class Time:
#     def __init__(self,fn):
#         self.fn = fn
#
#     def __enter__(self):
#         self.__start = datetime.datetime.now()
#         print('enter')
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         end = datetime.datetime.now()
#         print((end - self.__start).total_seconds())
#         print('exit')
#     def __call__(self, *args, **kwargs):
#         return self.fn(*args,**kwargs)
#
#
# def add(x,y):
#     time.sleep(2)
#     return x + y
# with Time(add) as a:
#     print(a(1,2))


class Time:
    def __init__(self,fn):
        self.fn = fn
        #functiontools.wraps(fn.self)
        self.__doc__ = fn.__doc__
        self.__name__ = fn.__name__
    def __call__(self, *args, **kwargs):
        start = datetime.datetime.now()
        result = self.fn(*args, **kwargs)
        end = datetime.datetime.now()
        delatime = (end - start).total_seconds()
        print('{} use {}'.format(self.fn.__name__, delatime))
        return result

@Time
def add(x,y):
    """this is add"""
    time.sleep(2)
    result = x + y
    return result

print(add(2,3))
print(add.__doc__)
print(add.__name__)



