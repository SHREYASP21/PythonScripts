class Parrot:
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("parrot cannot swim")


class penguin:    
    def fly(self):
        print("penguin cannot fly")
    def swim(self):
        print("penguin can swim") 

    
def flying_test(bird):
        bird.fly()
def swim_test(b1):
    b1.swim()
b=Parrot()
p=penguin()
flying_test(p)
swim_test(p)

