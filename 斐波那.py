# def fb(n):
#     if n<2:
#         return 1
#     else:
#         return fb(n-1)+fb(n-2)
# print(fb(4))
def fb(n):
    pre=0
    cur=1
    for i in range(n):
        pre,cur=cur,pre+cur
    return cur
print(fb(5))
