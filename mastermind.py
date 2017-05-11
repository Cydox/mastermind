from mastertools import *

cont = True

while cont:
	code = gencode()
	print code

	for i in range(10):
		guess = raw_input("Your guess: ")
		
		if guess == code:
			print "You won!"
			break
		else:

			print "You have " + str(goodplace(code, guess)) + " colors in the correct position and " + str(goodcolor(code, guess)) + " correct colors in the wrong position."
	
	if not guess == code:
		print "You lost"

		print "Code was " + code

	input = raw_input("Do you wanne play again (Y/n)")
	if input == "n":
		cont = False
