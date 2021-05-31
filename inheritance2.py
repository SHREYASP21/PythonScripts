class calc:
    def sum(self,x,y):
        return x+y

class calc1:
    def multi(self,a,b):
        return a*b

class derive(calc,calc1):
    def divide(self,d,k):
        return d//k
d=derive()
print(d.sum(10,20))
    
