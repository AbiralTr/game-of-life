import random
from utils import BitHelper

class Map:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.capacity = height * width
        self.dimensions = [height, width]
        self.population = []
        self.matrix = [[0 for _ in range(width)] for _ in range(height)] 

    def import_population(self, pop):
        size = len(pop)
        if size > self.capacity:
            raise ValueError("Too many entities in imported population")
        self.population = pop

    def fill_matrix(self):
        filled = set()
        for entity in self.population:
            success = False
            while not success:
                w = random.randint(0, self.width-1)
                h = random.randint(0, self.height-1)
                if (w, h) not in filled:
                    self.matrix[w][h] = entity
                    entity.set_position(w, h) 
                    filled.add((w,h))
                    success = True

    def add_to_population(self, entity):
        self.population.append(entity)

    def remove_from_population(self, entity):
        self.population.remove(entity)
    
    @property
    def get_population(self):
        return self.population

    @property
    def get_dimensions(self):
        return self.dimensions

    @property
    def get_capacity(self):
        return self.capacity

    @property
    def get_matrix(self):
        return self.matrix

    def randomize_state(self):
        self.matrix = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.fill_matrix()

    def advance_state(self):
        self.matrix = [[0 for _ in range(self.width)] for _ in range(self.height)]
        filled = set()
        for entity in self.population:
            success = False
            while not success:
                choice = list(entity.choose_step())
                new_position = BitHelper.add_vectors(entity.get_position, choice)
                if new_position[0] > self.height-1 or new_position[1] > self.width-1 or new_position[0] < 0 or new_position[1] < 0:
                    print("Chosen position out of bounds - retrying")
                elif (new_position[0], new_position[1]) not in filled:
                    success = True
                    filled.add((new_position[0], new_position[1]))
                    entity.set_position(new_position[0], new_position[1])
                    self.matrix[new_position[0]][new_position[1]] = entity
                else:
                    print("Chosen position is filled - retrying")


                
                








