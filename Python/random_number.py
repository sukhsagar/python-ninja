import random
number = random.randint(10,20)
turns = 3
while turns>0:
	choice = int(input("Guess the number"))
	if choice == number:
		print("Congratulations. You have guessed the right number")
		break
	else:
		turns-=1
if turns == 0:
	print("Sorry. You could not guess the number. It was ",number)

