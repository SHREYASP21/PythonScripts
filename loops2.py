atm_pin=8765
user_pin=int(input("enter your pin:"))
while(atm_pin != user_pin):
   user_pin=int(input("sorry incorrect pin, please reenter\n"))

print("*"*30)
print("welcome to your account")