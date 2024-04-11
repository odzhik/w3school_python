# task1 
def grams_to_ounces(grams):
    ounces = 28.349 * grams
    print(ounces)

grams_to_ounces(20)

#task2
def far_to_cel(F):
    cel = (5 / 9) * (F - 32)
    print(cel)

far_to_cel(100)


#task 3

def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        total_legs = 2 * num_chickens + 4 * num_rabbits
        if total_legs == numlegs:
           return num_chickens, num_rabbits

    
# Example usage:
numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print("Number of chickens:", chickens)
print("Number of rabbits:", rabbits)

#task 4



    