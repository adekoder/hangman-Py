import random
# hangman main function
def mainHangman():
	print("Want to test your guessability!!!! ?????")
	print("enter the coressponding code to choose an option")
	print("-" * 50)
	print("1 : Start Game")
	print("2 : exit Game\n")
	user_option = input(">>")
	game_length = len(gameData())    #making the game continue based on the gameData
	game_count = 0
	overall_point = 0
	if user_option == "1":
		# continue the game based on the number of word in the database 
		while game_count <= game_length:

			overall_point += gamePlay()
			print("current game point is " , overall_point)
			game_count += 1
			if game_count == game_length:
				print("Thanks for playing your over all score is : %d\n" %(overall_point) )
				break
	else:
		print("bye bye bye !!!!!! :)")
		exit()

def gamePlay():
	print("-" * 100)
	game_point = 0 
	word = wordGenerator().rstrip()
	guess_limit = 8
	user_input_list = ["-"] * len(word) # creatng a fixed list lenght based on the word length
	correct = False
	temp_word= list(word)
	while not correct:
		user_input = interface(word,user_input_list).lower()
		
		if checker(user_input , temp_word):
			user_input_list[temp_word.index(user_input)] = user_input
			temp_word[temp_word.index(user_input)] = "*"
			#print(temp_word)
			print("".join(user_input_list))
			print("guessed right :_/)\n")
			#"".join(user_input_list) == word
			if temp_word.count("*") == len(word) :  # checking if the temp_word list is filled up of "*" 
				game_point += 5 
				print("you are great correct %s is %s"  %("".join(user_input_list),word) )
				print("your game point is " ,game_point )
				correct = True
				break
		else:
			guess_limit -= 1 
			print("You have %d guess limit\n " % guess_limit)
			print("wrong\n")
			if guess_limit == 0: 
				print(":) Oooops!!! 2 point had been decuted from your game point \n")
				game_point -= 2
				break

	return game_point


def interface(word,input_list):
	"""this funtion print the interface to the user """
	#print(word)
	print("-" * 100)
	print("The word is %d charcter long \n" % len(input_list) )
	print("word space  : " , "".join(input_list ),"\n") 
	print("guess a letter") 
	user_input = input(">>")
	if user_input == "stop":exit()
	return user_input

def wordGenerator():
	word_list = gameData()
	random_number = random.choice(range(len(word_list)))
	return word_list[random_number] # selecting word form the list using random index

def checker(value, word):
	if value in word:
		return True
	return False

def gameData():
	file  = open("gameData.txt","r")
	word_list = file.readlines()
	file.close()
	return word_list

mainHangman()

