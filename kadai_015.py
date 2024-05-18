class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printinfo(self):
        print(self.name)
        print(self.age)

sr = Human("kadai", 15)

sr.printinfo()
