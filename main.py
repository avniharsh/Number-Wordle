#function setup
from random import randint
def playWordle():	
	

	#Welcome code
	print("Welcome to Wordle 2.0, aka...\nNumber Wonder!")
	print("""\nIf you don't know how to play, 
I highly suggest you search it up.
Lets go!\n""")
	
	#program settup
	x=0
	tries=0
	yellow=[]
	green=[]
	
	#getting the number
	for i in range(6):
		x+=(randint(0,9)*10**i)
	x=str(x)
	if len(x)==5:
		x="0"+x	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	#Guess code in loop until correct or run out.
	while True:
	
	
		#check if run out of tries
		if tries==7:
			print("\nOops! Looks like you ran out of tries!")
			break
		
		#setup for g/y detection code
		guess=input("\nGuess: ")
		tries+=1
		xlist=([*str(x)])
		guesslist=([*guess])
		yellow=[]
		green=[]

		#make sure guess is 6-digit, not "blah blah blah"
		if not guess.isdigit() or not len(guess)==6:
			print("Please enter a valid guess")			
		else: #literally just do it normally

			#check if number fully guessed
			if guess==str(x):
				print("\nYay! You got it!")
				break
			
			#green detection code
			for i,j in zip(guesslist, xlist):
				if i == j:
					green.append(i)
				else:
					green.append("_")
			
			#yellow detection code
			for i,j in zip(guesslist, xlist):
				if i != j:
					if i in xlist: 
						if x.count(i) > (green.count(i)+yellow.count(i)):
							yellow.append(i)
						else:
							yellow.append("_")
					else:
						yellow.append("_")
				else:
					yellow.append("_")
		
			#output for user
			print(f"""\nCorrectly guessed numbers: {''.join(green)}\nRight numbers but wrong place: {''.join(yellow)}""")
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	#Game over	
	print("Game over.")
	
	#Play again? code
	play_again = input("\nDo you want to play again? [YES/NO]\n")
	play_again = play_again.upper()
	if "Y" in play_again:
		playWordle()
	elif "N" in play_again:
		print("Ok.")
	else:
		print("Not a valid response. Terminating game.")


#Yay! Finally done!
playWordle()