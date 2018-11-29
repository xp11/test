import logging
print("yes")
FORMATER= '%(module)s-%(funcName)s:%(asctime)s %(message)s'
logging.basicConfig(level=logging.INFO,format=FORMATER,datefmt='%Y/%m/%d:%H-%M-%S',filename='d: ')
def add():
    try:
        raise Exception('page not found')
    except Exception as e:
        logging.warning(e)
add()