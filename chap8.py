# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Ceceilia Allwein 


# Here's the built in python rot_13 function 
# Used this as a control to check my result


def rot13_ctrl_encode(arg):
	import codecs
	encode = codecs.encode(str(arg),'rot_13')
	# print "Your code is: " + encode
	return encode

def rot13_ctrl_decode(arg):
	import codecs
	decode = codecs.decode(str(arg),'rot_13')
	# print "The answer is: " + decode
	return decode


rot13_encode = rot13_ctrl_encode('My name is Ceceilia') 
rot13_decode = rot13_ctrl_decode(rot13_encode)

print "SOLUTION"
print "Your code is: " + rot13_encode
print "The answer is: " + rot13_decode
print ""



# This adaptation feels like cheating... 

def rot_by_int(string, integer):
	import codecs
	integer = 13 - integer
	encode = codecs.encode(string,'rot_13')
	rotate = [(ord(char)+integer) for char in encode]
	# decode = codecs.decode(str(string),'rot_13')
	# print rotate
	return rotate



# print "SOLUTION: Adaptation of built-in rot13 to rotate by a given int"
# print "Your code is: " + rot_by_int('ceceilia',13)




# And here's my attempt at doing this manually
# Returns [Decode error - output not utf-8]
# I created the mod function to try to mitigate this
# No luck... HALP!


def mod(array,integer):
	array = [((ord(char)+integer)%26+ord(char)) for char in array]
	return array
		
print mod('Ceceilia',13)


def rot13_mine(string,integer): 
	'''
	0. Converts string to all lower case 
	1. Converts string to unicode array
	2. Augments array by a given integer
	3. Converts array to ascii characters
	4. Converts array to string 

	'''

	# array1 = [ord(char) for char in lc]
	array = [mod(string,integer) for char in string]
	print array
	code = [chr(num) for num in array]
	# print code
	result = "".join(code)
	# print result
	return 'Your code is: ' + result


# print rot13_mine('My name is Ceceilia',13)







