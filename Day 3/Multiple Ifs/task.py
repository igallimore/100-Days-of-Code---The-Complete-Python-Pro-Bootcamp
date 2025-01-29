#using my code and expanding it to reflect the exercise

print ("welcome to my roller coaster. It is loads of fun!")

height = int(input("You need to be 120cm + in order to ride. \n Please, tell me your height. And don't lie! "))
ticket_price = 0
photo_option = 3

if height >= 120:
    age = int(input("How old are you? "))
    if age >= 18:
        ticket_price = 12
        print("Please pay $12")
    elif age >= 12 and age < 18:
        ticket_price = 7
        print("Please pay $7")
    else:
        ticket_price = 5
        print("Kid, pay $5")
    photo = input("Do you want a photo? Yes or No")
    if photo == "Yes" or photo == "yes" or photo == "y" or photo == "Y":
        ticket_price += 3
    print (f"Here is the total: ${ticket_price}.")
else:
    print("Sorry. You are too short to ride! \nTry the churros. They are awesome. ")


