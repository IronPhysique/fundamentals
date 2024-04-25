class Student:
    def __init__(self, name, age, current_class):
        self.name = name
        self.age = age
        self.current_class = current_class

    def get_age(self):
        return self.age
    
    def average_score(self, score1, score2, score3):
        return (score1 + score2 + score3) / 3

student1 = Student("Alice", 20, "Art")
student2 = Student("Bob", 22, "Travel")
student3 = Student("Duncan", 19, "Bricklaying")

print(student1.get_age())
print(student2.get_age())
print(student3.average_score(50, 100, 85))
