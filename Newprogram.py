a=input("What is your name:\n").title().strip()
n=input(f"{a} from which course you want to enroll in :\n").title().strip()
k=input(f"{a} which website you are learning {n} from?:\n").upper().strip()
print(f"{a} is learning {n} from {k}")