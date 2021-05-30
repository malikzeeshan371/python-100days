logo = '''

  /$$$$$$                                                 /$$     /$$                                                         /$$                          
 /$$__  $$                                               | $$    | $$                                                        | $$                          
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$       /$$$$$$  | $$$$$$$   /$$$$$$        /$$$$$$$  /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/      |_  $$_/  | $$__  $$ /$$__  $$      | $$__  $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$         | $$    | $$  \ $$| $$$$$$$$      | $$  \ $$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$        | $$ /$$| $$  | $$| $$_____/      | $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/        |  $$$$/| $$  | $$|  $$$$$$$      | $$  | $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
 \______/  \______/  \_______/|_______/|_______/          \___/  |__/  |__/ \_______/      |__/  |__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/      
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           

'''

from random import randint
print(logo)

# global variables
EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5

# function to compare answer with user's guess
def check_answer(guess, answer, turns):
	"""Checks answer against guess. Returns the number of turns remaining."""
	if guess > answer:
		print("Too high.")
		return turns - 1
	elif guess < answer:
		print("Too low.")
		return turns - 1
	else:
		print(f"You got it. the actual answer is {answer}, You won!")


# setting the dificulty as per user's choice
def set_dificulty():
	game_level = input("Chose a dificulty, type 'easy' or 'hard': ")
	if game_level == "easy":
		return EASY_LEVEL_TURN
	else:
		return HARD_LEVEL_TURN
		

def game():
	print("Welcome to the number guessing game.")
	print("I'm thinking of a number between 1 to 100")
	# generating a random number for the game between 1 to 100
	answer = randint(1, 100)
	# print(f"The actual answer is {answer} ")


	# showing the number of attemps user gets based on the dificulty level they chose to play with
	turns = set_dificulty()
	

	# reapeat the guessing untill the user gets it right or their numbers of attemps goes to 0
	guess = 0
	while guess != answer:
		print(f"You have {turns} attempts remaining to guess the number.")
		guess = int(input("make a guess: "))
		# checking if the guess is high or low
		turns = check_answer(guess, answer, turns)
		if turns == 0:
			print("You run out of guesses, You lose.")
            # print(f"The actual number was {answer}")
			return
		elif guess != answer:
			print("Guess again.")

# initiating the game
game()