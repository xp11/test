# import pickle
# # a='123'
# # b='456'
# # with open('d:/123.txt',mode='wb')as f:
# #     pickle.dump(a,f)
# #     pickle.dump(b,f)
# #
# #
# # with open('d:/123.txt',mode='rb')as f:
# #     print(pickle.load(f))

import json  # 不能直接序列化二进制
import base64 # 编码成二进制，去除特殊符号
with open('d:/pyt/6.jpg',mode='rb') as f:
    a=f.read()
    print(a)
    b=base64.b64encode(a)   #编码成二进制，去除特殊符号
    print(b)
    c=b.decode('ascii')   #把二进制转换成字符串，因为jason不支持二进制序列化
    d=json.dumps(c)     #jason序列化
    print(d)

    e=json.loads(d)     #jason 反序列化
    print(e)
    f=e.encode('ascii')   #把字符串转换成二进制
    print(f)
    g=base64.b64decode(f)  #base64解码，恢复成原数据
    print(g)
    print(a==g)
with open('d:/pyt/6.jpg','wb') as f:
    f.write(g)