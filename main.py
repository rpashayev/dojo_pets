import ninja
import pet

dog_jessy = pet.Pet('Jessy', 'dog', 'scratching', 'Ay caramba!')
rpas_food = ['ice cream', 'Burger', 'Pizza']
rpas_ninja = ninja.Ninja('Ruslan', 'Pasha', dog_jessy, 'excellent', rpas_food)

rpas_food = ['ice cream', 'Burger', 'Pizza']
parrot_alex = pet.Bird('Alex', 'bird', 'talking', 'Hello, world!')
gg_ninja = ninja.Ninja('Gunay', 'Ali', parrot_alex, 'excellent', rpas_food)

rpas_ninja.feed()
rpas_ninja.walk()
rpas_ninja.bathe()
print(f'{dog_jessy.name} energy: {dog_jessy.energy} and health: {dog_jessy.health}')

rpas_ninja.feed()
print(f'{dog_jessy.name} energy: {dog_jessy.energy} and health: {dog_jessy.health}')

dog_jessy.sleep()
print(f'{dog_jessy.name} energy: {dog_jessy.energy} and health: {dog_jessy.health}')

gg_ninja.feed()
print(f'{parrot_alex.name} energy: {parrot_alex.energy} and health: {parrot_alex.health}')
