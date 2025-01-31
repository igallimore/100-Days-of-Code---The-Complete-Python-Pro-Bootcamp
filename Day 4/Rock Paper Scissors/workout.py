import random

#an empty file to workout my logic

computer_choices = [1, 2, 3]

# human = input("make your pick!")

computer = computer_choices[random.randint(0,2)]

if computer == 1:
    print("this is 1")
elif computer == 2:
    print("this is 2")
else:
    print("this is 3")



