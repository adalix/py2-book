#ossep deneme

from os import *
def dizinler(test1,test2,test3) :
	makedirs(test1)
	makedirs(sep.join([test1,test2]))
	makedirs(sep.join([test1,test3]))