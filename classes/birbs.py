class Bird:
    def __init__(self, species):
        self.species = species

    def fly(self):
        return "This bird can fly."

class Owl(Bird):
    def fly(self):
        return "Owls can fly silently."

    def hunt(self):
        return "Owls hunt at night."

class Dodo(Bird):
    def fly(self):
        return "Dodos cannot fly."

    def extinct(self):
        return "Dodos are extinct."

owl = Owl("Barn Owl")
dodo = Dodo("Mauritian Dodo")

print(owl.fly())  
print(dodo.fly()) 
print(owl.hunt())  
print(dodo.extinct())  
