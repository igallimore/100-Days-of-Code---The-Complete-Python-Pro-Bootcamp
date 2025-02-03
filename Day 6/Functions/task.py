
# user_name = input("What is your name?")
# def test(name):
#     print (f"Good morning, {name}!")
#
# test(user_name)

# def test_1():
#     print("Yes!")
#editors let you modify the tab button so that it equals 4 spaces

counter = 10

while counter > 0:
    print (counter > 0)
    counter -= 1

#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while at_goal() != True:
#     jump()


# The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# How to use a while loop and an if statement.
#
# while wall_in_front == True:
#     turn_left()
#     move()
#     turn_left()



#The hurdles race with variety!

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def wall():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# while at_goal() != True:
#     if wall_in_front() == True:
#         wall()
#     elif front_is_clear() == True:
#         move()
#     if at_goal() == True:
#         print("You made it!")

#With variable wall lengths - that was a bitch of a mission
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def wall():
#     turn_left()
#     while not front_is_clear():
#         turn_right()
#     while wall_on_right():
#         if not front_is_clear():
#             turn_right()
#             turn_left()
#             turn_left()
#         move()
#     turn_right()
#     move()
#     turn_right()
#     # turn_right()
#     while front_is_clear()  and not at_goal():
#         move()
#
#
# while at_goal() != True:
#     if wall_in_front() == True:
#         wall()
#     elif front_is_clear() == True:
#         move()
#         if at_goal() == True:
#             print("You made it!")
#
#     if at_goal() == True:
#         print("You made it!")

#the working code:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def wall():
#     turn_left()
#     while not front_is_clear():
#         turn_right()
#     while wall_on_right():
#         if not front_is_clear():
#             turn_right()
#             turn_left()
#             turn_left()
#         move()
#     turn_right()
#     move()
#     turn_right()
#     # turn_right()
#     while front_is_clear() and not at_goal():
#         if at_goal():
#             print("You made it!")
#             pause()
#         move()
#
#
# while at_goal() != True:
#     if wall_in_front() == True:
#         wall()
#     elif front_is_clear() == True:
#         move()
#         if at_goal() == True:
#             print("You made it!")
#
#     if at_goal() == True:
#         print("You made it!")

# The functions move() and turn_left().
# Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
# How to use a while loop and if/elif/else statements.
# It might be useful to know how to use the negation of a test (not in Python).