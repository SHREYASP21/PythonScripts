class Bird:
    i=20
    
    def __init__(self):
        print("Bird is ready")
    def whoisthis(self):
        print("Bird")   
    def swim(self):
        print("Swim faster")
        

class Penguin(Bird):
          def __init__(self):
             # super().__init__()
              print("penguin is ready")
          def whoisthis(self):
              print("Penguin")
          def run(self):
              print("Run faster")  
p1=Penguin()
p1.whoisthis()
p1.swim()
p1.run()
p1.i=100





