def time_seconds(num):
     day1=num //(24*3600)
     d= num % (24*3600)
     hr1=d//3600
    #  min1=num % 3600
    #  sec1=num % 60
     print(day1,hr1)


time_seconds(129600)






""" num1=int(input("Enter the value of num:\n"))
i,j=square_cube(num1)
print(f"The square of the number is {i} and the cube is {j}") """