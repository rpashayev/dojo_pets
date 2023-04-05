class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
    
    def sleep(self):
        print (f'{self.name} is sleeping')
        self.energy += 25
    
    def eat(self):
        self.energy += 5
        self.health += 10
    
    def play(self):
        self.health += 10
    
    def noise(self):
        print('Ay caramba!')


