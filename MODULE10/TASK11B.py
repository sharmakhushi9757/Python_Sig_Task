class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.age=int()
        self.marks=int()
    def display(self):
        print("Name -",self.name)
        print("ROll no -",self.roll)
        print("Age -",self.age)
        print("Marks -",self.marks)
    def setAge(self,age):
        self.age=age

    def setMarks(self,mark):
        self.marks=mark
ob1=student("kanak",105)
ob1.setAge(18)
ob1.setMarks(90)
print("Detail of student - ")
ob1.display()