def generateprime():
	for x in xrange(1,n):
		if x == 1:
			return "One cannot be a prime number."
		elif x < 1:
			print("Not possible to generate prime numbers for ")
		elif (x%1) == 0:
			print(x, 'is not a prime Number')
		else:
			print(x, 'is a prime Number')