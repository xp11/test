import pymysql
from pymysql.cursors import DictCursor
conn=pymysql.Connect(host='192.168.20.2',port = 3306, user='root',password='123456',database='test',charset="bbb")
cursor=conn.cursor(cursor=DictCursor)
sql='inset into bbb values(2,"jack")'
result=cursor.execute(sql)
print(cursor.fetchall())
cursor.close()
conn.commit()