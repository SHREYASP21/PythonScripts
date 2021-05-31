import math
def fib(n):
   
    a,b =0,1
    while a<n:
        print(a,end='')
        a,b=b,a+b
        print()

def fact1(n1):
    i=math.factorial(n1)
    print(i)      