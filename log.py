import logging
print("yes")
FORMATER= '%(module)s-%(funcName)s:%(asctime)s %(message)s'
logging.basicConfig(level=logging.INFO,format=FORMATER,datefmt='%Y/%m/%d:%H-%M-%S')
def add():
    try:
        raise Exception('page not found')
    except Exception as e:
        logging.warning(e)
add()




import logging
import test1
loger = logging.getLogger(__name__)
handler = logging.FileHandler('d:/test2.log')
formater = logging.Formatter('%(asctime)s %(message)s',datefmt='%Y/%m/%d:%H-%M-%S')
handler.setFormatter(formater)
loger.setLevel(logging.INFO)
loger.addHandler(handler)
loger.propagate = False
loger.info('jack sb')