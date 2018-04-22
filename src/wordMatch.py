ENGLISH_FREQ = "Dictionaries/EnglishFreq.txt"
ENGLISH = "Dictionaries/English.txt"

linesFreq = list(open(ENGLISH_FREQ))
wordsFreq = [word.strip() for word in linesFreq]

lines = list(open(ENGLISH))
words = [word.strip() for word in lines]

# Returns true if all characters in the str1 are contained in the str2, in order.
# For example, "pen" is embeddable in "protein", but "pit" is not, because the 'i' in protein comes after the 't'.
def isEmbeddable(str1, str2):
	index1 = 0
	index2 = 0

	while True:
		if index2 >= len(str2):
			return False

		if str1[index1] == str2[index2]:
			index1 += 1
			if index1 >= len(str1):
				return True
		else:
			index2 += 1


# Returns the longest element in a list, according to the len function.
def longest(lst):
	if len(lst) == 0:
		return None
	return max(lst, key=len)

def findMatch(trace, srcWords):
	possibleResults = []
	for word in srcWords:
		if len(word) > 2 and ("a" in word or "e" in word or "i" in word or "o" in word or "u" in word or "y" in word):	# 1-2 letter words and vowelless words should not be swiped
			if word[0] == trace[0] and word[-1] == trace[-1]:
				if isEmbeddable(word, trace):
					possibleResults.append(word)
	possibleResults.sort(key=len, reverse=True)
	#return possibleResults
	return str(longest(possibleResults))# + " " + str(len(possibleResults))

print(len(words))

while True:
	trace = input()
	match = findMatch(trace, wordsFreq)
	if match is None:
		print("not frequent!")
		print(findMatch(trace, words))
	else:
		match2 = findMatch(trace, words)
		if len(match2) - len(match) >= 2:
			print(match2)
		else:
			print(match)
