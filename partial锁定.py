from functools import partial
def add(x,y):
    return x+y
print(add(2,3))
print(partial(add,2,5)())
add=partial(add,2)
print(add(3))