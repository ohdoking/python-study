#const 
#star method
REVERSE = 0
NORMAL = 1
MOUNTAIN = 2

star = "*"
blank = " "

def makeStar(count, method):
	if method == REVERSE:	
		for i in reversed(range(count)):
			print star*i
		
		# same the above method
		#for i in range(count, 0, -1):
		#	print star*i
	elif method == NORMAL:
		for i in range(count):
			print star*i

	elif method == MOUNTAIN:
		for i in range(1,count,2):
			print blank*(((count-i)-1)/2), star*i
