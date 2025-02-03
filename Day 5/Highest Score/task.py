student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

print (sum(student_scores))

total = 0

for i in student_scores:
    total += i

print(total)

numbers = [1, 2, 3, 4]

the_number = 250000

for x in numbers:
    the_number -= x

print (the_number)

the_store = 0
for x in numbers:
    if x > the_store:
        the_store = x
print (the_store)

container = 0
for x in student_scores:
    if x > container:
        container = x
print(container)



