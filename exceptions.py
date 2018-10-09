#python exceptions let you deal with unexpected results

try:
	print(a)
except:
	print('a is not defined!')

#there are specific errors to help with cases

try:
	print(a)
except NameError:
	print('a is still not defined!')
except:
	print('Something else went wrong')
	
print(a) #break program bc a is not defined