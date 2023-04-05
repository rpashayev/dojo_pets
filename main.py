class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    
    def walk(self):
        Pet.play(self.pet)
    
    def feed(self):
        Pet.eat(self.pet)
        print(f'Feeding {self.pet.name} {self.pet_food}')
    
    def bathe(self):
        print(f'Bathing {self.pet.name}')
        Pet.noise(self.pet)
    
    
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


dog_jessy = Pet('Jessy', 'poodle', 'scratching')
rpas_ninja = Ninja('Ruslan', 'Pasha', dog_jessy, 'excellent', 'ice cream')

rpas_ninja.feed()
rpas_ninja.walk()
rpas_ninja.bathe()
print(f'{dog_jessy.name} energy: {dog_jessy.energy} and health: {dog_jessy.health}')

dog_jessy.sleep()
print(f'{dog_jessy.name} energy: {dog_jessy.energy} and health: {dog_jessy.health}')