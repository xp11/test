import datetime
import time
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