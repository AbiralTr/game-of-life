from bit import Bit
import random
from utils import BitHelper
from map import Map

population = BitHelper.generate_population(5)
m = Map(5, 5)
m.import_population(population)

m.fill_matrix()

BitHelper.print_matrix(m.get_matrix)
