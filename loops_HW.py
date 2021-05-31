import random
score=0
round_number=1
number=random.randint(1,5)
print(number)
print("*"*30)
while True:
    your_number=int(input("What is your guess?\n"))
    print("*"*30)
        if number==your_number:
            print("That's correct! you guessed the right number")
            score += score
         else:
            print("in-correct, try again")
            score -= score
if round_number==6:
    break
print(f"final score is: {score}")