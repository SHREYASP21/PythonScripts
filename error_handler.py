while True:
    try:
        a=int(input("enter a dividend"))
        b=int(input("enter a divisor"))
    except ValueError:
        print("you've not entered a valid number")
    else:
        try:
            r=a/b
        except ZeroDivisionError:
            print("Division by zero is undefined")
        else:
            print(r)
            break