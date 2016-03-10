import random

sec ="ABCDEFGHIJKLMNOPRSTUVYZabcdefghijklmnoprstuvyz1234567890"

passlen = 8

pas ="".join(random.sample(sec,passlen))
print "parolaniz %s" %pas 
