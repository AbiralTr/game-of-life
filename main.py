from bit import Bit
import random
from utils import BitHelper
from map import Map

m = Map(5, 5)
pop = BitHelper.generate_population(5)

m.import_population(pop)
m.fill_matrix()

