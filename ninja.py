import pet
class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    
    def walk(self):
        pet.Pet.play(self.pet)
        return self
    
    def feed(self):
        if len(self.pet_food) > 0: 
            food = self.pet_food.pop()
            pet.Pet.eat(self.pet)
            print(f'Feeding {self.pet.name} {food}')
            return self
        else:
            print('Buy more food for your pet!')
    
    def bathe(self):
        print(f'Bathing {self.pet.name}')
        pet.Pet.noise(self.pet)

