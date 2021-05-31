#name=input("enter your name:")
name='Floccinauciniloare'
new_name =''
vowels='aeiou' 
for i in name:

    if i not in vowels:
        new_name += i 
print(new_name)
    