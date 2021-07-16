import random

def game(comp,you):
	
	if comp==you:
		return None

	if comp=='r':

		if you=='p':
			return True
		elif you=='s':
			return False

	if comp=='p':

		if you=='r':
			return False

		elif you=='s':
			return True

	if comp=='s':

		if you=='p':
			return False

		elif you=='r':
			return True

print("Computers Turn- rock(r) , paper(p) , scissor(s)")

print("Okay , the computer has choosen. Now its your turn")

random_number=random.randint(1,3)

if random_number==1:
	comp='r'

elif random_number==2:
	comp='p'

elif random_number==3:
	comp='s'

you=input("Your Turn - rock(r) , paper(p) , scissor(s): ")

a=game(comp,you)

print(f"The computer chose {comp}")

print(f"You chose {you}")

if a==None:

	print("The game is a tie")

elif a:

	print("Congrats! You won")

else:

	print("Oh! The computer won this time")

