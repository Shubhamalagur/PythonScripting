#! /usr/bin/python3

'''
Naming variable:-
A variable name must start with a letter or the underscore character
A variable name cannot start with a number and cannnot contain space
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''
#no need to declare data type
x=4

#dont use variable in '' to print but to use as it is
print(x)
#with use ''
print('x')
#you can find type of variable
y=3.4
print(type(y))
#no need to say change variable value
print("changine x value")
x=10
print(x)
#Delete variable using del x
##print("deleting variable x")
##del x
##print(x)

'''
Data types and variables:data is stored in memory.
every valuein Python has Data type
Since everything is an Object in Python programming, data types are actually classes and variables are
instance(Object) of these classes.

Data Types in Python:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''
#memory location of x can be found by id(x)
print("Memory location for var x:")
print(id(x))