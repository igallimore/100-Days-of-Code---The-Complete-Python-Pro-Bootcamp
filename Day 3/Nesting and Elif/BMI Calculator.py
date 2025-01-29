#weight = 85
#height = 1.85
print("Welcome to my grumpy BMI calculator. \n Life is short. Don't take it personal\n")
weight = float(input("What is your weight (in kg)? "))
height = float(input("What is your height (in meters)? "))
#bmi = weight / (height ** 2)
bmi = weight/ (height **2)

#I commented the course's code and added the input to make it more interactive
#This is a grumpy BMI calculator. Maybe not for American audiences that are sensitive about weight.
print (f"Hi, this is your current BMI: {round(bmi)}.")
if bmi >= 40:
    print(f"Holy shit! How are you still alive? Your bmi is {bmi}! Go to Dr. Now asap!")
elif bmi > 25:
    print("Look, you are overweight. No amount of body positivity is going to save your organs. \n Diabetes is a thing. Start to eat like an adult and not a kid.")
elif bmi < 18.5:
    print("You are underweight and it is not good. You need to eat more and you will be in a much better mood. \n Your cat will appreciate it. It's tired of you yelling at it.")
elif bmi >= 18.5 and bmi < 25:
    print("Your weight is good. Keep up the good work. Maintain it by eating actual adult food and exercising at least 20 minutes per day.")
