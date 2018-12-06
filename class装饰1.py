import time
import datetime
import functools
class Timeit:
    def __init__(self,fn):
        self.fn=fn
        self.__name__=fn.__name__
        self.__doc__=fn.__doc__
        # functools.wraps(fn,self)
    def __call__(self, *args, **kwargs):
        start = datetime.datetime.now()
        result=self.fn(*args,**kwargs)
        end = datetime.datetime.now()
        print((end-start).total_seconds())
        return result
@Timeit   #add = Timeit(add)
def add(x,y):
    '''this add'''
    time.sleep(2)
    print(x+y)
    return x+y
print(add(2,3))
print(add.__doc__)
print(add.__name__)