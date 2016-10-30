# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

import nltk
import random
from nltk.book import *

print("START*******\n\n")

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

text2 = text2[:150]

original_words = []

for word in text2:
	original_words.append(spaced(word))

# Printing original text - first 150 tokens
print (''.join(original_words)) 

# POS tagging first 150 tokens of text2
tagged_tokens = nltk.pos_tag(text2)

# Creating dictionary for different POS
tagmap = {
	"NN":"a noun",
	"NNS":"a plural noun",
	"VB":"a verb",
	"JJ":"an adjective",
	'RB':'an adverb',
	'DT':'a determiner'
}
substitution_probabilities = {"NN":.15,"NNS":.15,"VB":.1,"JJ":.1,'RB':.1,'DT':.1}

final_words = []

for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		# User inputting string with newline
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print (''.join(final_words))

print("\n\nEND*******")
