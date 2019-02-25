# import re
# import datetime
# import time
# parent="""(?P<ip>[\d.]+) - - \[(?P<datetime>.*)\] "(?P<method>\w+) (?P<url>\S+) [\w/\.]+" (?P<status>\d+) (?P<size>[\d-]+) ".*" "(?P<browser>.*)"""
# regix=re.compile(parent)
# new_dict={'size':lambda x:int(x),'datetime':lambda x:datetime.datetime.strptime(x)}
#
# with open("D:/pyt/rz.txt","r")as f:
#     for line in f:
#         result = regix.match(line)
#         ord_dict=result.groupdict()



import datetime
import re
import random
import time
from queue import  Queue
import threading

s='''192.168.13.1 - - [14/Sep/2018:23:39:37 -0400] "GET /zabbix HTTP/1.1" 301 - "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/56.0.3051.36"'''
pattern = '(?P<ip>[\d\.]{7,}) - - \[(?P<datetime>.*)\] "(?P<method>\w+) (?P<url>\S+) [\w/\.]+" (?P<status>\d+) (?P<size>[\d-]+) ".+" "(?P<useragent>.+)"'
regex=re.compile(pattern)
options = {'datetime': lambda x: datetime.datetime.strptime(x, '%d/%b/%Y:%H:%M:%S %z'),'size':lambda x : int(x) if x.isdigit() else 0}

def extract(line):
    matcher = regex.match(line)
    if matcher:
        mathdict = matcher.groupdict()
        for k,v in options.items():
            mathdict[k]=v(mathdict[k])
        return mathdict

# def load(path:str):
#     with open(path) as f :
#         for line in f :
#             result=extract(line)
#             if result:
#                 yield result
#             else:
#                 continue

def src():
    numdict={}
    while True :
        numdict['value']=random.randint(1,100)
        numdict['datetime']=datetime.datetime.now()
        time.sleep(1)
        yield numdict

srclist=[]
for i in range(10):
    srclist.append(next(src()))

print(srclist)

def hanlder_test(src:list):
    l=len(src)
    d=src[-1]['datetime']
    s=0
    if l == 0 :
        print(0)
        return
    else:
        for item in src :
            s=s+item['value']
        print(round(s/l),d,l)





def windows(src:Queue,hand,interval):
    start=datetime.datetime.fromtimestamp(0)
    point = datetime.datetime.fromtimestamp(1000)
    buffter = []
    while True:
        item=src.get()
        buffter.append(item)
        point = item['datetime']
        if (point - start).total_seconds() >= interval:
            hand(buffter)
            start=point
            buffter=[]




def dispacher(src):
    masks=[]
    qlist=[]

    def reg(handler,interval):
        q=Queue()
        qlist.append(q)
        task=threading.Thread(target=windows,args=(q,handler,interval))
        masks.append(task)

    def run():
        for t in masks:
            t.start()
        for item  in src :
            for q in qlist:
                q.put(item)


    return reg,run


reg,run = dispacher(srclist)
reg(hanlder_test,3)
reg(hanlder_test,2)
run()




