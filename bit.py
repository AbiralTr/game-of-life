import uuid
import random

class Bit:

    def __init__(self):
        self.name = ''
        self.code = uuid.uuid4().hex[:5]
        self.energy = 1.0
        self.active = True
        self.health = 2
        self.power = 2
        self.position = (None, None)

    @property
    def get_code(self):
        return self.code
    
    @property
    def get_energy(self):
        return self.energy

    @property
    def get_health(self):
        return self.health

    @property
    def is_active(self):
        return self.active

    @property
    def get_name(self):
        return self.name
    
    @property
    def get_position(self):
        return self.position

    def set_position(self, x, y):
        self.position = (x, y)

    def set_name(self, n):
        self.name = n

    def deactivate(self):
        self.active = False

    def absorb(self, target):
        if not target.is_active and target.get_energy != 0:
            self.energy += target.get_energy / 2
            target.set_energy(0)
            print(str(self.get_code) + " absorbed " + str(target.get_code))

    def take_damage(self, num):
        self.health = self.health - num

    def evolve(self):
        if self.get_energy >= 2:
            evolution = Nibit(self)
            print("Bit " + str(self.code) + " evolve into a Nibit")
            self.code = None
            return evolution

    def set_energy(self, num):
        self.energy = num
    
    def choose_step(self):
        directions = [(0,0), (1,0), (0,1), (-1,0), (0,-1)]
        choice = random.choice(directions)
        return choice

class Nibit(Bit):

    def __init__(self, bit):
        self.code = bit.get_code
        self.energy = 2.0
        self.active = True
        self.health = 4
        self.power = 4

    def attack(self, target):
        target.take_damage(self.power)

class Byte(Nibit):

    def __init__(self, Nibit):
        self.code = Nibit.get_code
        self.energy = 4.0
        self.active = True
        self.health = 8
        self.power = 8

