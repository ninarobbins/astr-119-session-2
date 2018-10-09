import numpy as np

i = 10
print(type(i))

# integers
a_i = np.zeros(i, dtype = int) #declare an array of i number of ints
print(type(a_i))
print(type(a_i[0]))

#floats
x = 119.0
print(type(x))

y = 1.19e2 #float 119.0 i scientific notation
print(type(y))

z = np.zeros(i,dtype = float) #declare array of floats
print(type(y))
print(type(z[0]))