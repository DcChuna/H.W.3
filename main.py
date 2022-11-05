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