import random

class Father:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
    
    def show_info(self):
        return f"Father: {self.name}, Nationality: {self.nationality}"
    
    def gen(self):
        return random.choice(["Y", "X"]) 
        
class Mother:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        
    def show_info(self):
        return f"Mother: {self.name}, Nationality: {self.nationality}"

    def gen(self):
        return "X"

class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self, name="Diego", nationality="Chilena")
        Mother.__init__(self, name="Anna", nationality="Chilena")
        self.father_gen = Father.gen(self)
        self.mother_gen = Mother.gen(self)
        self.gen = self.define_gen()
    
    def define_gen(self):
        if self.father_gen == "Y":
            return "Male"
        else:
            return "Female"
        
    def gen(self):
        return self.gen
    
    def show_info(self):
        father_info = Father.show_info(self)
        mother_info = Mother.show_info(self)
        return f"{father_info}\n{mother_info}\nChild Gender: {self.gen}"
        
child = Child()
info = child.show_info()
print(info)

        
    
        
        
    