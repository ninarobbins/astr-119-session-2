#import numpy
import numpy as np

#define the main function
def main():
	i = 0
	x = 119.0
	for i in range(120):
		if (i % 2 == 0):
			x = x + 3.0		#or x += 3
		else:
			x = x - 5.0		#or x -= 5
	s = '%3.2e' % x		#make a string that shows x with scientific notation
	print(s)
	
if __name__ == '__main__':
	main()
