# try:
#     with open("g:/xy")as f:
#         print("open")
# except:
#     pass
# print("ok")



# try:
#     with open("g:/xy")as f:
#         print("open")
# except BaseException as e:
#     raise
# print("ok")


import threading
import time





def foo1():
	return 1/0

def foo2():
	time.sleep(3)
	print('foo2 start')
	foo1()
	print('foo2 stop')

t = threading.Thread(target=foo2)
t.start()


while True :
	time.sleep(1)
	print('1 ok')
	if t.is_alive():
		print('alive')
	else:
		print('dead')