class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

print(student1.get_age())
print(student2.get_age())
