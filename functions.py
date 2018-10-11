import numpy as np
import sys

#define function that returns a value
def expo(x):
	return np.exp(x) #returns e^x function

#define subroutine that does not return a value
def show_expo(n):
	for i in range(n):	
        print(expo(float(i))) # call expo function

#define a main fcn

def main():
	n = 10 #default value of n
	#check if there is a command line argument provided
	if (len(sys.argv)>1):
		n = int(sys.argv[1]) #if an argument is provided use it for n
	show_expo(n) 	#call subroutine
	
if __name__ == '__main__':
	main()