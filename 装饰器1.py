import inspect

def check(fn):
    def wrapper(*args,**kwargs):
        # print(args)
        # print(kwargs)
        sig = inspect.signature(fn)
        paramer = sig.parameters
        dictlist=list(paramer.items())
        print(dictlist)
        # print(paramer)
        for index,vlaue in enumerate(args):
            k,v=dictlist[index]
            # print(k,v)
            if not isinstance(vlaue,v.annotation):
                print("{} is not ok".format(k))
        for k,v in kwargs.items():
            if not isinstance(v,paramer[k].annotation):
                print("{} is not ok".format(k))
        return fn(*args,**kwargs)
    return wrapper

@check
def add(x:int,y:str):
    return x+y
print(add(5.5,y=4.5))
