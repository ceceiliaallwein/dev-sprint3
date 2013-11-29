# This is where the answers to Chapter 9 questions go
# Name: Ceceilia Allwein 


# Exercise 9.1 

def more_than_20(filename):
	'''Prints words from a text file only 
	if they are 20 characters are more.'''

	fin = open(filename)
	for line in fin: 
		word = line.strip()
		if len(word) >= 20: 
			print word

print ''
print 'Exercise 9.1'
print more_than_20('words.txt')



# Exercise 9.2

def has_no_e(word):
	'''Returns true if a word does not
	contain the letter e.'''

	fin = open(filename)
	for line in fin: 
		word = line.strip()
		letter = 'e'
		find1(word,letter)

print ''
print 'Exercise 9.2a'
print has_no_e(apple)


def find1(word,letter):
	''' Loops through a string
	and identifies if it contains
	a given character. 

	If found, returns True. 
	If not found, returns False.  
	'''
	index = 0 
	while index < len(word):
		if word[index] !== letter:
			print True
			return True 
		index = index + 1
	return False


print ''
print 'Exercise 9.2b'
print find1('ceceilia','l')



# Exercise 9.3a

def avoids_letters(word,letters):
	'''Determines if a word contains 
	forbidden letters. Returns True if 
	letters do not appear.'''


print ''
print 'Exercise 9.3a'
print avoids_letters('ceceilia','C')


# Exercise 9.3b

def avoids_user_input(word,letters):
	'''Determines if a word contains given 
	forbidden letters, and prompts user to 
	input their own list of letters. Returns 
	True if letters do not appear.'''


print ''
print 'Exercise 9.3b'
print avoids_user_input()
