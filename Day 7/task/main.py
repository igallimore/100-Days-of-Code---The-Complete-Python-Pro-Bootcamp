import random

word_list = ["candy", "car", "mother", "pasta", "doggie", "perspective"]

chosen_word = random.choice(word_list)

counter = len(chosen_word)

print(chosen_word)
print (counter)

guess = input ("Pick a letter").lower()
print(guess)

placeholder = []

for x in range(counter):
	placeholder.append("_")

places = " ".join(placeholder)

print(places)

display = []



# for letter in chosen_word:
# 	if guess == letter:
# 		print ("Right!")
# 		display.append(letter)
# 	else:
# 		print ("Wrong!")
# 		display.append("_")
# display = " ".join(display)
# print (display)



while counter > 0:
	for letter in chosen_word:
		if guess != letter:
			counter -= 1
	if counter == 0:
		print ("You lost!")
	guess = input ("pick a letter")
