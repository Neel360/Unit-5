class Student:
    grade = 10
    print (f"Hi! I am in grade {grade}. ")

obj = Student()

class Vehichle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehichle(240,18)

print(f"Model X max speed: {modelX.max_speed}")
print(f"Model X mileage: {modelX.mileage}")

        