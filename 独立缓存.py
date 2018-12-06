import inspect
cache_dict={}
def cache(fn):
    def wrapper(*args,**kwargs):
        paras=list(inspect.signature(fn).parameters)
        args_t=[(paras[k],v) for k,v in enumerate(args)]
        kwargs_t=[item for item in kwargs.items()]
        key=tuple(sorted(args_t+kwargs_t))
        print(key)
        print(cache_dict)
        if key not in cache_dict:
            result = fn(*args, **kwargs)
            cache_dict[key]=result
        return cache_dict[key]
    return wrapper
@cache
def add(x,y):
    return x+y
print(add(x=1,y=2))
print(add(1,2))
