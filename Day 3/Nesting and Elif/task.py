print ("welcome to my roller coaster. It is loads of fun!")

height = int(input("You need to be 120cm + in order to ride. \n Please, tell me your height. And don't lie! "))

if height >= 120:
    age = int(input("How old are you? "))
    if age >= 18:
        print("Please pay $12")
    elif age >= 12 and age < 18:
        print("Please pay $7")
    else:
        print("Kid, pay $5")
else:
    print("Sorry. You are too short to ride! \nTry the churros. They are awesome. ")

