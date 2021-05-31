a='Hyderabad is the capital of Telangana'
Search=input("Enter a string you want to search:").lower()
if Search in a.lower():
    print(f"{Search} is found in {a}")
else:
    print("It is not found")