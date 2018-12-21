import random

def passwordGenerator():
	listaSlabo = [3,4,5,6,7]
	listaJako = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	signs = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', ';', ':', '"', "'", ',', '<', '.',
			 '>']
	upper_cases = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
				   'U', 'V', 'W', 'X', 'Y', 'Z']
	lower_cases = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
				   'u', 'v', 'w', 'x', 'y', 'z']
	numbers = ['0','1','2','3','4','5','6','7','8','9']

	print("Which password would you like?")
	print("1.weak")
	print("2.strong")
	while True:
		choice = input("Enter your choice: ")

		if choice == "1":
			string = ""
			for i in range(random.choice(listaSlabo)):
				a1 = random.choice(lower_cases)
				string = string + a1
			for i in range(random.choice(listaSlabo)):
				a2 = random.choice(upper_cases)
				string = string + a2



			print("I have generated for you this password: ",string)
			return

		elif choice == "2":
			string = ""
			for i in range(random.choice(listaJako)):
				a1 = random.choice(lower_cases)
				string = string + a1
			for i in range(random.choice(listaJako)):
				a2 = random.choice(upper_cases)
				string = string + a2
			for i in range(random.choice(listaJako)):
				a3 = random.choice(numbers)
				string = string + a3
			for i in range(random.choice(listaJako)):
				a4 = random.choice(signs)
				string = string + a4
			print("I have generated for you this password: ", string)
			return

		elif choice not in ['1','2']:
			print("Enter 1 or 2, dumbass.")

passwordGenerator()