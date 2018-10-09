# dictionaries have key:value for elements

example_dict = {
	'class' : 'Astr 119',
	'prof' : 'Brant',
	'awesomeness' : 10
}
print(type(example_dict))

#get value with key
course = example_dict['class']
print(course)

#change a value via key
example_dict['awesomeness'] += 1 #increase awesomeness

print(example_dict)

for x in example_dict.keys():
	print(x, example_dict[x])
