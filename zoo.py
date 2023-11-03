class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name, age):
        self.animals.append( Lion(name, age) )
    def add_tiger(self, name, age):
        self.animals.append( Tiger(name, age) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

class Animal:
    def __init__(self, name, age, health=10, happiness=10):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
    
    def feed(self,amount):
        if self.age <= 5:
            self.happiness += (amount*10)
            self.health += (amount*10)
        else:
            self.happiness += (amount*5)
            self.health += (amount*5)
    
    def display_info(self):
        print(type(self))
        print("it is called",self.name,", its age :",self.age,", and has a level of health :",self.health,", and a level of happiness :",self.happiness)


class Lion(Animal):
    def __init__(self, name, age, color = "Golden", health=6, happiness=7):
        super().__init__(name, age, health, happiness)
        self.color = color
    def feed(self, amount):
        if amount < 2:
            self.health += 1
            print(self.name,"is Angry, need more food")
        else:
            return super().feed(amount)
        
    def display_info(self):
        print("this is a",self.color,"Lion")
        return super().display_info()


class Bear(Animal):
    def __init__(self, name, age, Type1 = "Russian", health=10, happiness=10):
        super().__init__(name, age, health, happiness)
        self.type = Type1
    def feed(self, amount):
        if amount < 4:
            self.health += 0.5
            print(self.name,"is Angry, need more food")
        else:
            return super().feed(amount)
        
    def display_info(self):
        print("this is a",self.type,"bear")
        return super().display_info()
    
class Tiger(Animal):
    def __init__(self, name, age, size = "large", health=14, happiness=15):
        super().__init__(name, age, health, happiness)
        self.size= size
    def feed(self, amount):
        if amount < 3:
            self.health += 1.5
            print(self.name,"is Angry, need more food")
        else:
            return super().feed(amount)
        
    def display_info(self):
        print("this is a",self.size,"Tiger")
        return super().display_info()



dojo = Bear("dojo",3)
simba = Lion("Simba",6)
micha = Tiger("Micha",2)

dojo.feed(1)
dojo.display_info()

simba.feed(1)
simba.display_info()

micha.feed(1)
micha.display_info()


zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala",10)
zoo1.add_lion("Simba",10)
zoo1.add_tiger("Rajah",10)
zoo1.add_tiger("Shere Khan",10)
zoo1.print_all_info()