from bit import Bit
import random
from utils import BitHelper
from map import Map
import time

m = Map(5, 5)
pop = BitHelper.generate_population(10)

m.import_population(pop)
m.fill_matrix()

while True:
    m.advance_state()
    BitHelper.print_matrix(m.get_matrix)
    time.sleep(1)
