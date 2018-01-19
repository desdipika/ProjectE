#Project Euler Problem 1

n = int(input("Give a number : "))
if n%3 == 0:
	if n%5 == 0:
		print("It is a mutilple of 3 and 5")
	else:
		print("It is a multiple of 3")
elif n%5 == 0:
	print("It is a mutilple of 5")	
else:
	print("Not a mutiple of 3 and 5")