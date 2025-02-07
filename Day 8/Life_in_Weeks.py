
age = int(input ("How old are you"))
time = 90 * 52

def life_in_weeks(age):
	current_age = age * 52
	weeks_left = time - current_age
	print (f"You have {weeks_left} weeks left!")

life_in_weeks(age)

