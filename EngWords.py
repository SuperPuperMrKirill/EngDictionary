class Word(): 

	def __init__(self, name, meaning, translation, parent, description, score = 0, topic = ''):
		self.name = name
		self.meaning = meaning
		self.translation = translation 
		self.parent = parent 
		self.description = description
		self.score = score 
		self.topic = topic
		
	def __str__(self):
		# rep = F"{self.name} - {self.meaning} / {self.translation}\n"
		rep = self.name + ' - '
		rep += self.meaning
		if self.meaning and self.translation:
			rep += '/ '
		rep += self.translation + ' '
		if self.parent: 
			rep += F"\n   parent: {self.parent}"
		if self.topic: 
			rep += F"\n   topic: {self.topic}" 
		rep += '\n'
		return rep 

	def components(self): 
		rep = []
		rep.append(self.name)
		rep.append(self.meaning)
		rep.append(self.translation)
		rep.append(self.parent)
		rep.append(self.description)
		rep.append(str(self.score))
		rep.append(self.topic)
		return rep

class Dictionary(): 

	def __init__(self, directory): 
		# creates dictionary
		self.directory = directory
		file = open(self.directory, 'r')

		self.words = []
		for word in file: 
			w = Word(*(word.split(';')))
			self.words.append(w)
		file.close()

	def __str__(self): 
		rep = F"Dictionary with {len(self.words)} words"
		return rep

	def print_words(self):
		for i in self.words:
			print(i)

	def add(self, word): 
		# is word already exist? 
		for i in self.words: 
			if i.name == word.name: 
				print(F"Word '{word.name}' already exists.")
				print(i)
		else: 
			self.words.append(word)
			file = open(self.directory, 'a')
			file.write(';'.join(word.components())+'\n')
			file.close()

	def check(self, word_name):
		for i in self.words:
			if i.name == word_name: 
				print(i)
				break
		else:
			print('no such word')

	def test_eng_ru(self, amount = 10):
		import random
		
		score = 0
		for i in range(amount):
			word = random.choice(self.words)
			while not word.translation:
				word = random.choice(self.words)

			answer = input(F"Translate {word.name}: ")
			if answer == word.translation:
				score += 1 
				print("You're right!")
			else:
				print(F"You're wrong. It's {word.translation}")
			print()

		print(F"That's all. Your score is {score} / {amount}")

################ Main 
dictionary = Dictionary("dictionary1.txt")

print("English words manager v1.0:")
print(dictionary)

while 1: 
	#ask options
	print("""
What are you gonna do?: 
	0 - exit
	1 - add new word 
	2 - check the word 
	3 - print words
	4 - change word (in progress)
	5 - test (eng-ru)
		  """)
	#execute option
	option = int(input("Enter option: "))
	if option == 0:
		break
	elif option == 1: 
		name = input("Name: ")
		meaning = input("Meaning: ")
		translation = input("Translation: ")
		parent = input("Parent: ")
		description = input("Description: ")
		word = Word(name, meaning, translation, parent, description)
		dictionary.add(word)
	elif option == 2:
		word_name = input("Word: ")
		dictionary.check(word_name)
	elif option == 3: 
		dictionary.print_words()
	elif option == 4:
		pass 
	elif option == 5:
		amount = int(input("How much word?: "))
		dictionary.test_eng_ru(amount)
	else: 
		print('no such option')

	input("Press enter to continue...")
