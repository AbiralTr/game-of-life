from bit import Bit
import random

living = []
dead = []

for i in range(15):
    bit = Bit()
    living.append(bit)

def advance_time():
    for entity in living:
        chance = random.randint(0,1)
        if chance == 0:
            entity.deactivate()
            dead.append(entity)
            living.remove(entity)

def print_population(group):
    for entity in group:
        print(str(entity.get_code))

print_population(living)
advance_time()
print_population(living)
print_population(dead)

