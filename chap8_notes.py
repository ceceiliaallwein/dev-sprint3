# Chapter 8 notes
# Action item: label exercises / notes



# Section 8.3 - Traversal 

def count(fruit):
	''' Prints each letter as 
	index increments.'''
	index = 0
	while index < len(fruit):
		letter = fruit[index]
		print letter
		index = index + 1

#count('banana')


def find1(word,letter):
	''' Loops through a string
	and identifies if it contains
	a given character. 

	If found, returns the index. 
	If not found, returns -1.  
	'''
	index = 0 
	while index < len(word):
		if word[index] == letter:
			print index
			return index 
		index = index + 1
	print -1
	return -1
	

def find2(word,letter,index):
	''' Variation on find1 function, 
	where the index parameter sets 
	the loop's starting position. '''
	while index < len(word):
		if word[index] == letter: 
			print index 
			return index
		index = index + 1
	print 'Not found'
	return -1

#find1('banana','a')

#find2('banana','a',7)


def quantity():
	''' Determines quantity of 
	a specific character contained
	within a string.  
	'''
	word = 'banana'
	count = 0
	for letter in word: 
		if letter == 'a':
			count = count + 1
	print count

#quantity()



# Section 8.9 - The in operator
# Section 8.10 - String comparison

def in_both(word1,word2):
	''' Identifies characters 
	shared by given strings.'''
	for letter in word1:
		if letter in word2:
			print letter 

#in_both('apples','oranges')



# Section 8.11 - Debugging

def is_reverse(word1,word2):
	''' Returns True if one word 
	is the reverse of the other. 

	Errors: 
	1. j>0 changed to j>=0
	2. j=len(word2) changed 
	to j = len(word2)-1
	'''
	
	if len(word1) != len(word2):
		print False
		return False

	i = 0
#	j = len(word2) ERROR
	j = len(word2)-1

#	while j>0 ERROR
	while j >=0: 
		print i,j
		if word1[i] != word2[j]:
			print False
			return False
		i = i+1
		j = j-1 

	print True
	return True 

#is_reverse('pots','stop')



# Exercise 8.11

def any_lowercase1(s):
	''' Determines if the first letter
	is lower case, not the entire word.'''
	for c in s:
		if c.islower():
			print True
			return True
		else: 
			print False
			return False


def any_lowercase2(s):
	''' Incorrect syntax for str method. 
	Remove apostrophes around c '''
	for c in s:
		if 'c'.islower():
			return 'True'


def any_lowercase3(s):
	'''The function reassigns flag 
	each time through. If the last
	letter is caps, it doesn't matter
	what came before. '''
	for c in s:
		flag = c.islower()
	print flag
	return flag

#any_lowercase3('ceceiliA')


def any_lowercase4(s):
	''' This is correct. Returns False 
	if any of the characters are UC.'''
	flag = False 
	for c in s: 
		flag = flag or c.islower()
		print flag
		return flag 

#any_lowercase4('ceceilia')


def any_lowercase5(s):
	''' The not is a gatekeeper. If 
	there are any UC characters it 
	will return False and quit. '''
	for c in s:
		if not c.islower():
			print False
			return False
	print True
	return True 

any_lowercase5('ceceilia')

