import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["candy", "car", "mother", "pasta", "doggie", "perspective"]

chosen_word = random.choice(word_list)

counter =  len(chosen_word)

print(chosen_word)
print (counter)

placeholder = ""

for x in range(counter):
	placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

lives = 6

while not game_over:
    display = " "
    guess = input("Pick a letter: ")

    # Test
    if guess not in chosen_word:
        print(stages[lives])
        lives -= 1
        # print("This is the lives guess")

    for letter in chosen_word:
        if lives == 0:
            print ("You lost!")
            print (stages[0])
            exit()
        if guess == letter:
            # print("Right!")
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            # print("Wrong!")
            display += "_"

    if "_" not in display:
        game_over = True
        print ("You win!")
    print(display)



