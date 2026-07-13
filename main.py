from bit import Bit
import random
from utils import BitHelper
from map import Map

running = True

m = None
p = None

while running:
    print("--------------- MENU ---------------")
    print("1: Generate Map")
    print("2: Generate Population")
    print("3: Load Population")
    print("4: Load Matrix")
    print("5: Change Matrix State")

    choice = input("Choose (1-5): ")

    switch(choice):
        case '1':
            width = input("Choose Width: ")
            height = input("Choose Height: ")
            m = Map(width, height)
            break
        case '2':
            num = input("Choose Count: ")
            p = BitHelper.generate_population(num)
            break
        case '3':
            if m == None:
                print("No valid map exists yet, try option 1")
                continue
            m.import_population(p)
            break
        case '4':
            if m == None:
                print("No valid map exists yet, try option 1")
                continue
            elif m.get_population == []:
                print("No valid population loaded yet, try option 3")
                continue
            m.fill_matrix()
            break
        case '5':
            m.change_state()
            break
        case _:
            break
