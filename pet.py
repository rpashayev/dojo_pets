class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
    
    def sleep(self):
        print (f'{self.name} is sleeping')
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 10
        return self
    
    def noise(self):
        print(self.noise)


class Bird(Pet):
    def __init__(self, name, type, tricks, noise):
        super().__init__(name, type, tricks, noise)
    
    def sleep(self):
        print (f'{self.name} is sleeping as a {self.type}')
        self.energy += 1
        return self
