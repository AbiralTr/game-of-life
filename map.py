import random

class Map:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.capacity = height * width
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
                    filled.add((w,h))
                    success = True
                else:
                    print("Spot [" + str(w) + "," + str(h) + "] is filled, retrying")

    def add_to_population(self, entity):
        self.population.append(entity)

    def remove_from_population(self, entity):
        self.population.remove(entity)
    
    @property
    def get_population(self):
        return self.population

    @property
    def get_dimensions(self):
        return (self.height, self.width)

    @property
    def get_capacity(self):
        return self.capacit

    @property
    def get_matrix(self):
        return self.matrix

    def change_state(self):
        self.matrix = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.fill_matrix()











