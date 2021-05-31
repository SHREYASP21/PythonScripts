#calorie count for food
a=int(input("How many grams of protien?: \n").title().strip())
b=int(input("How many grams of carbohydrates: \n").title().strip())
c=int(input("How many grams of Fats: \n").title().strip())
#To calculate the calorie value
print(f" total calories from of protiens: {a*4}")
print(f" total calories from carbohydrates: {b*4}")
print(f" total calories from fats: {c*9}")
print(f" total calories from {a} grams of protiens, {b} grams of carbohydrates and {c} grams of fats: { (a*4) + (b*4) + (c*9) }")