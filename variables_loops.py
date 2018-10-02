import numpy as np

def main():
	i = 0
	n = 10
	x = 119.0
	
	y = np.zeros(n,dtype=float)		#declares 10 zeros
	
	#we can use for loops to iterate through a variable
	for i in range(n):
		y[i] = 2.0 * float(i) + 1.0		#set y = 2i+1
		
	#we can iterate through the y elements one by one
	for y_element in y:
		print(y_element)
		
if __name__ == '__main__':
	main()