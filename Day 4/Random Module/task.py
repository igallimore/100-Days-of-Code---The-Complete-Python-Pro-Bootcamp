#Copmuters are not random - mersenne twister?
#random must be imported
import random
import My_Module


test = random.randint(10, 108)
#you need to include the module name of the library in the function!
print(test)

#modules are responsible for different parts of your program - break up
# you import them

#test with my module
my_name = input ("What is your name?")
My_Module.greeting(my_name)

print (random.random())
#the random function generates a random number from 0 to 1 - you can expand it

print (random.random() * 300)

#random.uniform includes the numbers in the upper and lower limits
random_luck = random.uniform(1, 100)
print(random_luck)
if random_luck >= 50:
    print("tails")
else:
    print("heads")

#other option
luck_generator = random.randint(0, 1)
print(luck_generator)
if luck_generator == 1:
    print("You are lucky!")
else:
    print ("You are not lucky now but you will be. Dont' worry!")

