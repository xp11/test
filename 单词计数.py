
# f=open('路径',mode='r')
# print(f.read())
#
#
# f=open('路径',mode='r',encoding='编码方式')
# print(f.read())
#
# f=open('D:/pyt/5.txt',mode='w')
# f.close()
# print(f.readable())
# print(f.closed)
# #
#
# with open('D:/pyt/5.txt',mode='r')as f:
#     print(f.readlines())
#     print(f.closed)

# import base64
# f=open('D:/pyt/2.jpg',mode='rb')
# img=f.read()
# f.close()
# base_img=base64.b64encode(img)
# print(type(img),type(base_img))
#
# f=open('D:/pyt/6.jpg',mode='wb')
# real_img=base64.b64decode(base_img)
# f.write(real_img)
# f.close()
# import re
# word_dict = {}
# n=[]
# with open('D:/pyt/sample.txt',mode='r',encoding='utf-8')as f:
#     a = f.read()
#     s = re.sub('\W',' ',a)
#     words = s.split()
#     for k in words:
#         if k not in word_dict:
#             word_dict[k] = 1
#         else:
#             word_dict[k] = word_dict[k] + 1
#     print(word_dict)
#     for k,v in word_dict.items():
#         n.append((v,k))
#     n=sorted(n,reverse=True)
#     print(n)
#     for i in range(10):
#         print(n[i])




import re
with open ('d:/pyt/sample.txt',mode='r',encoding='utf-8')as f:
    a=f.read()
    dc=re.sub("\W"," ",a).split()
    x=[]
    print(dc)
    for i in dc:
        kv = (dc.count(i), i)
        if kv not in x:
            x.append(kv)
    print(x)
    px=sorted(x,reverse=True)
    print(px)
    for n in range(10):
        print(px[n])

# import re
# # with open('d:/pyt/sample.txt',mode='r',encoding='utf-8') as f:
# #     a=f.read()
# #     b=re.sub('\W',' ',a).split()
# #     c={}
# #     for i in b:
# #         if i not in c:
# #             c[i]=1
# #         else:
# #             c[i]+=1
# # d=sorted(c.items(),key=lambda x:x[1],reverse=True)
# # print(d)
# # e=[]
# # for j in range(10):
# #     e.append(d[j])
# # print(e)

# import re
# d={}
# with open("d:/pyt/sample.txt","r" , encoding="utf-8") as  f:
#     s=str(f.read())
#     s = re.sub("\W"," ", s)
#     s = s.split()
#     print(s)
#     for i in s:
#         d[i] = s.count(i)
#     print(d)
# e=[]
# for k,v in d.items():
#     e.append((v,k))
# n=sorted(e,reverse=True)
# print(n)
# for i in range(4):
#     print(n[i])

# chars="\r\n)(;][}{|\'\"\\?,.@#$!%©>:-''./~"
# word_dict={}
# with open("d:/pyt/sample.txt","r" , encoding="utf-8") as  f:
#     for line in f:
#         words=line.split(" ")
#         for word in words:
#             word=word.strip(chars)
#             if len(word) == 0:
#                 continue
#             word_dict[word]=word_dict.get(word,0)+1
#         # nlist=sorted(list(word_dict.items()),key=lambda x : x[1],reverse=True)
#         # for
# print(word_dict)
