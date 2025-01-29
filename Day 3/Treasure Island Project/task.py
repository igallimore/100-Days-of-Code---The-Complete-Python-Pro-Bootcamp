print(r'''
*******************************************************************************
............(¯`'•.
..............(¯'•(¯'•............_/)/)
...............(¯'•.(¯'•.......((.....((
................(¯`'•(¯'•...((.)..(. ‘ /)
.................(¯`'•.(¯'((.)....|\_/
.....,,,~”¯¯¯`'¯(_¸´(_.)......|
...(((./...........................)__
..((((.\......),,...........(...../__`\
..))))..\ . .//...¯¯¯¯¯¯¯' \.../... / /
.(((...../ .// .............. | ./.....\/
.))).....| ||.................| |...........♥♥♥
((........) \\.................) \...........\|/
.^^^^.""'"'.^^^^^^^..""".^^^^.""""
*******************************************************************************
''')
print("Welcome to Luxury  Land!")
print("Your mission is to find the platinum 1ct diamond studs.")

direction = input ("right or left?")

if direction == "left":
    print ("Awesome! You get to keep going!\n Here is an iced chai latte to keep you on your journey")
    location = input ("Continue going to Rodeo Drive. Do you want to walk there or take this Uber?")
    if location == "uber" or location == "Uber":
        print ("Yes! You made it to Rodeo Drive.\n You really are enjoying that life of luxury.")
        designer = input ("Final choice. What do you pick\n Chanel, The Row or Loewe? ")
        if designer == "Loewe" or designer == "loewe":
            print("""Yes! You won!!! You get platinum diamond earrings! Enjoy!\n
        ᐢ⑅ᐢ
    ꒰ ˶• ༝ •˶꒱
    ./づ~ ♡
            
            """
                  )
        elif designer == "The Row" or designer == "the row" or designer == "the Row":
            print ("Girl, Mary Kate and Ashley don't want you in there. Better luck next time!\n Try again!")
        elif designer == "Chanel" or designer == "chanel":
            print ("Oh no! You chose Chanel? Now you are in a store full of poorly made overpriced bags! \n Better luck next time!!!")
        else:
            print("Gorl, learn how to spell your designers! Better luck next time.")
    else:
        print("Oh no! You decided to walk and a kid threw his icecream at you. \n Look at that ice cream all over your Loro Piana outfit. \n Better luck next time. Try again!")
else:
    print("Oof! You fell into a hole of cheap Louis Vuitton bags. Sorry! Better luck next time!")