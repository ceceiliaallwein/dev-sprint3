# This is where the answers to Chapter 9 questions go
# Name: Ceceilia Allwein 


# Exercise 9.1 

print ''
print 'Exercise 9.1'

def more_than_20(filename):
	'''Prints words from a text file only 
	if they are 20 characters are more.'''

	fin = open(filename)
	for line in fin: 
		word = line.strip()
		if len(word) >= 20: 
			print word
			# return word 
	return 

print more_than_20('words.txt')


# Exercise 9.2

print ''
print 'Exercise 9.2'

def find1(word,letter):
	''' Loops through a string
	and identifies if it contains
	a given character. 

	If found, returns the word. 
	If not found, returns False.  
	'''
	if word.find(letter) >= 0:
		return word
	else: 
		return False

print 'find1:' + find1('ceceilia','l')


def has_no_e(letter,filename):
	'''Returns true if a given word 
	within a given text file does 
	not contain the letter e.'''
	fin = open(filename)
	line = fin.readline()
	output = []
	while line: 
		word = line.strip()
		no_e_words = find1(word,letter)
		if no_e_words == False:
			output.append(word)
		line = fin.readline()
	return '\n'.join(output)
	#print no_e_words

print 'has_no_e:' + has_no_e('e','words.txt')



# Exercise 9.3a

def avoids_letters(word,letters):
	'''Determines if a word contains 
	forbidden letters. Returns True if 
	letters do not appear.'''


print ''
print 'Exercise 9.3a'
# print avoids_letters('ceceilia','C')


# Exercise 9.3b

def avoids_user_input(word,letters):
	'''Determines if a word contains given 
	forbidden letters, and prompts user to 
	input their own list of letters. Returns 
	True if letters do not appear.'''


print ''
print 'Exercise 9.3b'
# print avoids_user_input()
