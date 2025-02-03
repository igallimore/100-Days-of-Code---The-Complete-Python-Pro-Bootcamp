import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_list = []
number_list = []
symbol_list = []


for x in range(nr_letters):
    letter_list.append(random.choice(letters))
#print (letter_list)

for x in range(nr_symbols):
    symbol_list.append(random.choice(symbols))
#print (symbol_list)

for x in range(nr_numbers):
    number_list.append(random.choice(numbers))
#print (number_list)

complete_password = letter_list + symbol_list + number_list
random.shuffle(complete_password)
total = "".join(complete_password)
#print (complete_password)
#print (total)

print (f"Here is your new password: {total}")












