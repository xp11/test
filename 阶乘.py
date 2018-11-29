# def jc(n):
#     if  n==1:
#         return 1
#     else:
#         return jc(n-1)*n
# print(jc(5))
def fz(n):                      # 封装函数
    def fn(n,cexi=1):
        if n==1:
            return cexi
        else:
            cexi=cexi*n
            return fn(n-1,cexi)
    return fn(n)                # 封装函数
print(fz(5))