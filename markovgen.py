"""
What
-----
A Markov Chain is a sequence of values where the next value 
depends only on the current value (and not past values). It's 
basically a really simple state machine, where given the present 
state, the future state is conditionally independent of the past.

Thus we can ask the question: Given the present word, how likely 
is it that this word I've chosen would be the next?

How
-----
1) The last two words are the current state.
2) Next word depends on last two words only, or on present state only.

I've simplified this example down to the core elements of a Markov text generator.

Run the following to generate your own nonsensical strings:
$ python run.py

"""

import random

 # Class for generating markov chain 
class Markov(object):
	
	def __init__(self, open_file):
		# Simple dict cache
		self.cache = {}
		self.open_file = open_file
		# Grabs all the words from the file
		self.words = self.file_to_words()
		# Verifys number of words in corpus
		self.word_size = len(self.words)

		self.database()
		
	# Function that grabs all the words from the given file
	def file_to_words(self):
		self.open_file.seek(0)
		data = self.open_file.read()
		words = data.split()
		return words
	
	def triples(self):
		""" Generates triples from the given data string. So if our string were
				"What a lovely day", we'd generate (What, a, lovely) and then
				(a, lovely, day).
		"""
		
		if len(self.words) < 3:
			# NEED MOAR WORDS
			return
		
		for i in range(len(self.words) - 2):
			yield (self.words[i], self.words[i+1], self.words[i+2])
			


	def database(self):
		for w1, w2, w3 in self.triples():
			# Sets the first 2 words as the key
			key = (w1, w2)

			# If that key exists in cache append the third word to the cache
			if key in self.cache:
				self.cache[key].append(w3)
			else:
				# If the key doesn't exist in the cache set the cache[key] = third word
				self.cache[key] = [w3]
				
	# Size denotes the length of the sentence to be outputted
	def generate_markov_text(self, size=20):

		# set seed to a random integer based on corpus size
		seed = random.randint(0, self.word_size-3)

		# Set next_word 
		seed_word, next_word = self.words[seed], self.words[seed+1]

		w1, w2 = seed_word, next_word

		# Instantiate new list to hold the created sentence
		gen_words = []

		# size refers the number of words in the requested output
		for i in xrange(size):
			#Appends the seed_word to the gen_words list
			gen_words.append(w1)
			# Flips the seed_word to (seed_word + 1)
			# random.choice return a random element from the cachce based on key[seed,seed+1]
			w1, w2 = w2, random.choice(self.cache[(w1, w2)])
		gen_words.append(w2)
		print ' '.join(gen_words)
			
			
		