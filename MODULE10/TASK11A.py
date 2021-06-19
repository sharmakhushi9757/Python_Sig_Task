class circle:
    def __init__(self,radius):
        self.radius=radius
        self.area=0
        self.cir=0
    def getArea(self):
        self.area=3.14*self.radius*self.radius
        return self.area
    def getCircumference(self):
        self.cir=2*3.14*self.radius
        return self.cir
r=float(input("Enter radius to be entered: "))
ob1=circle(r)
print("Area of circle with provided radius : ",ob1.getArea())
print("Circumference with provided radius : ",ob1.getCircumference())