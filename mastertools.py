import random

def gencode():
	lst = random.sample(range(1, 7), 4)
	
	code = ""
	for x in lst:
		code += str(x)
	
	return code

def goodplace(code, guess):
	ncorrect = 0
	
	for i in range(len(code)):
		if code[i] == guess[i]:
			ncorrect += 1
	
	return ncorrect

def goodcolor(code, guess):
	c = 0
	
	for i in range(1, 7):
		a = code.count(str(i))
		b = guess.count(str(i))

		c += min(a, b)
	c -= goodplace(code, guess)

	return c
