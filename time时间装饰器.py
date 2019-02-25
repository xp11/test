import datetime
import time
def wrapping(t,fuc = lambda : print("")):
    def wrapper(fn):
        # @resrc(fn)
        def wrap(*args,**kwargs):
            """
            this is wrapper function
            """
            start=datetime.datetime.now()
            print(start)
            result=fn(*args,**kwargs)
            end=datetime.datetime.now()
            print(end)
            deltatime=(end - start).total_seconds()
            print("this func use {}s".format(deltatime))
            if int(deltatime) > t:
                fuc()
            # resrc(wrap,fn)
            return result
        return wrap
    return wrapper
def mysql():
    print("mysql")
@wrapping(1,mysql)
def add(x,y,z = 5):
    """
    this is add function
    """
    time.sleep(2)
    result=x + y + z
    return result
print(add(1,2))
# print(add.__doc__)
# print(add.__name__)