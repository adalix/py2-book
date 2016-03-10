import random

sec ="ABCDEFGHIJKLMNOPRSTUVYZabcdefghijklmnoprstuvyz1234567890"

passlen = 8

pas ="".join(random.sample(sec,passlen))
print "parolaniz %s" %pas 

'''
def tanimla():
	a = raw_input("bir sey yazin:")
	print "girdigininz sey:%s" %a

tanimla()
'''