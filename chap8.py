# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Ceceilia Allwein 

def mod(array):
	index = 0
	while index <= len(array):
		for char in array: 
			if char >= 128:
				char = (char % 13) + 97
		return array
		index = index + 1


def rot13_mine(string,integer): 
	'''
	0. Converts string to all lower case 
	1. Converts string to unicode array
	2. Augments array by a given integer
	3. Converts array to ascii characters
	4. Converts array to string 
	
	array = array of ints
	code = array of ascii
	result = string 
	'''

	lc = string.lower() 
	array1 = [(ord(char) + integer) for char in lc]
	array2 = mod(array1)
	code = [chr(char) for char in array2]
	result = "".join(code)
	return 'Your code is: ' + result


# only runs if second arg is <=5 ... HALP!
print rot13_mine('My name is Ceceilia',5)



def rot13_encode(arg):
	import codecs
	encode = codecs.encode(str(arg),'rot_13')
	return encode

def rot13_decode(arg):
	import codecs
	decode = codecs.decode(str(arg),'rot_13')
	return decode


code = rot13_encode('My name is Ceceilia') 
 
print code
print rot13_decode(code)




