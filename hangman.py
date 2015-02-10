import random
import time
HANGMAN_PICS = ['''     
			
			
			|
		________|__''',
		'''
		        |
			|
			|
			|
			|
		________|__''',
		'''
		  ________
			|
			|
			|
			|
			|
		________|__''',
		'''
		  ________
	            |	|
	            	|
			|
			|
			|
		________|__''',
		'''
		  ________
	            |	|
	            O	|
			|
			|
			|
		________|__''',
		'''
		  ________
		    |	|
		    O	|
		   /|\	|
			|
			|
		________|__''',
		'''
		  _________
		    |	|
		    O	|
		   /|\  |
		   / \  |
			|
		________|___''']
word_list=["apple","cat","ball","dog","elephant","fish","girl","hat","ink","jug","king","lion","man" ,"net","owl","pink","queen","rat","sun", "tits", "umbrella", "van", "wood", "xmas", "yummy" , "zebra"]

def clear_board():
	for i in range(50):
		print ("\n")

def get_random_word(words):
	secret_word = word_list[random.randint(0, len(word_list)-1)]
	return (secret_word)

def display_board(HANGMAN_PICS,missed_letter, correct_letter, secret_word):
	print(HANGMAN_PICS[len(missed_letter)])
	print "missed letters"
	for letter in missed_letter:
		print letter,
	print "\n"	
	blank = '_' * len(secret_word)
	for i in range (len(secret_word)):
		if secret_word[i] in correct_letter:
			blank = blank[:i] + secret_word[i] + blank[i+1:]
	for letter in blank:
		print letter,
	print "\n"
def get_guess(already_guessed):
	while True:
		print ("Guess a letter")
		guess =raw_input()
	
		if(len(guess)) != 1:
			print ("Please input a letter")
		elif guess in already_guessed:
			print("You have already guessed that letter. Choose another one")
		elif guess not in "abcdefghijklmnopqrstuvwxyz":
			print ("Plese enter a valid letter")
		else:
			return (guess.lower())
			

def play_again():
	print ("Game is over")
	time.sleep(3)
	print ("Do you want to play again?, yes/no")
	return (raw_input().lower().startswith('y'))

print "H A N G M A N"
missed_letter = ''
correct_letter = ''
secret_word = get_random_word(word_list)
game_is_over = False
while True:
	clear_board()
	display_board(HANGMAN_PICS,missed_letter, correct_letter, secret_word)
	guess = get_guess(missed_letter + correct_letter)

	if guess in secret_word:
		correct_letter = correct_letter + guess

		found_all_letter = True
		for i in range (len(secret_word)):
			if secret_word[i] not in correct_letter:
				found_all_letter = False
				break
		if found_all_letter:
			clear_board()
			print ("Yes! The secret word is' " + secret_word +  "'! You have won!")
			game_is_over = True
	else:
		missed_letter = missed_letter + guess
		if len(missed_letter) == len(HANGMAN_PICS) - 1:
			clear_board()
			print ("You have ran out of guesses")
			time.sleep(1)
			print ("You lost")
			print (HANGMAN_PICS[len(missed_letter)])
			time.sleep(1)
			print ("The secret word is'" + secret_word +"'")
			game_is_over = True
	if game_is_over:
		if play_again():
			missed_letter = ''
			correct_letter = ''
			game_is_over = False
			secret_word = get_random_word(word_list)
		else:
			break
	
