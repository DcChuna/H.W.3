import logging
sumnumbers=0
try:
    nn = int(input('1 Numaber '))
    nn1 = int(input('2 Numaber '))
    nn2 = int(input('3 Numaber '))
    nn3 = int(input('4 Numaber '))
    nn4 = int(input('5 Numaber '))
    print((nn+nn1+nn2+nn3+nn4)/5)
except (ImportError,TypeError,NameError,ValueError):
    print('Only number 1|not text')
infologging=input("Веддіть свій логін: ")
password=input("Веддіть свій пароль: ")
logging.basicConfig(
    level=logging.INFO,
    filename = 'logs.log',
    filemode='a',
    format=f'[%(asctime)s] %(message)s'
)
logging.info(infologging)
logging.info(password)
logging.debug("antivirus!")
logging.warning("WARNING!")
logging.error("Antivirus activate!")
logging.critical("All ok virus not find")