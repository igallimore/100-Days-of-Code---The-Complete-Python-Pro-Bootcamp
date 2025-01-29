#Erased the code to start from scratch and do my own thing - Idanis
print("Welcome to Churro's Pizza Shop!\n Tell me what pizza you want!")

#Questions for the user
size = input("What size do you want my dear? S, M or L? :  ")
extra_cheese = input("Do you want extra cheese? : ")
banana_pepper = input("Do you want me to include a yummy banana pepper? :  ")

total = 0

if size == "S" or size == "s":
    total += 15
    topping = input("do you want pepperoni? : ")
    if topping == "Yes" or topping == "yes":
        total += 2
elif size == "M" or size == "m":
    total += 20
    topping = input("do you want pepperoni? : ")
    if topping == "Yes" or topping == "yes":
        total += 3
elif size == "L" or size == "l":
    total += 25 #assuming large
    topping = input("do you want pepperoni? : ")
    if topping == "Yes" or topping == "yes":
        total += 3
else:
    print("Bro, you typed the wrong thing. Try again for yummy pizza!")

if extra_cheese == "yes" or extra_cheese == "Yes":
    total += 1

if banana_pepper == "yes" or banana_pepper == "Yes":
    total += 0.50

print (f"Here is your total: ${total}")



