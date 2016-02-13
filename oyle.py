from time import *

while True:
	for i in range(21):
		sleep(1)
		print str(i).zfill(2)
		while i > 20:
			continue
				