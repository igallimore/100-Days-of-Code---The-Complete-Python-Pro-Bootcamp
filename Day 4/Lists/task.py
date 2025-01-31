import random


favorite_foods = ["natilla", "paneer", "ice chai tea", "ground turkey bowls", "hot chocolate"]
pick = favorite_foods[random.randint(0, 4)]

if pick == "natilla":
    print("Natilla is the best")
else:
    print ("There are better foods out there!")

#to add to the list -> .append and .extend also

new_item = input("Add another food")
favorite_foods.append(new_item)

for item in favorite_foods:
    print(item)



