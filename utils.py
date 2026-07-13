from bit import Bit

class BitHelper:

    def print_matrix(mat):
        for i in mat:
            for j in i:
                if j != 0:
                    print(j.get_name + " ", end="")
                else:
                    print("0 ", end="")
            print("")
   
    def print_population(population):
        for entity in population:
            print(entity.get_code)

    def generate_population(amount):
        population = []
        for i in range(amount):
            b = Bit()
            b.set_name(str(i+1)) 
            population.append(b)

        return population
