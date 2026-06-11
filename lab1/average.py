class Student:
    def __init__(self,name,grade1,grade2,grade3):
        self.name=name
        self.grades=[grade1,grade2,grade3]
        self.average=sum(self.grades)//len(self.grades)

student1= Student("Rasmita",12,20,15)

print(student1.average)

    

