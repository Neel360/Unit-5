class Student:
    grade = 10
    print (f"Hi! I am in grade {grade}. ")

obj = Student()

class Vehichle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehichle(240,18)
print("\n\ndVehichle stats:\n")
print(f"Model X max speed: {modelX.max_speed}")
print(f"Model X mileage: {modelX.mileage}")

        
class Parrots:
    species = "Birds"
    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrots("Blu", 5)
woo = Parrots("Woo", 3)

print("\n\nParrots:\n")
print(f"{blu.name} is {blu.age} years old.")
print(f"{woo.name} is {woo.age} years old.")
print(f"They are both {blu.species}")
    