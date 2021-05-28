class calculator:
    def __init__(self,num):
        self.number = num
    def square(self):
        print(f"the value of {self.number} square is {self.number **2}")
        pass

    def squareroot(self):
        print(f"the value of {self.number} square is {self.number ** 0.5}")
        pass
    def cube(self):
        print(f"the value of {self.number} square is {self.number ** 3}")
        pass
    @staticmethod
    def greet():
        print("********hello there welcome to the best calculator of the world!***********")
a=calculator(3)
b=calculator(3)
b.cube()
a.square()
a.squareroot()
a.greet()