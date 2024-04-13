# # task1 
# def grams_to_ounces(grams):
#     ounces = 28.349 * grams
#     print(ounces)

# grams_to_ounces(20)

# #task2
# def far_to_cel(F):
#     cel = (5 / 9) * (F - 32)
#     print(cel)

# far_to_cel(100)


# #task 3

# def solve(numheads, numlegs):
#     for num_chickens in range(numheads + 1):
#         num_rabbits = numheads - num_chickens
#         total_legs = 2 * num_chickens + 4 * num_rabbits
#         if total_legs == numlegs:
#            return num_chickens, num_rabbits

    
# # Example usage:
# numheads = 35
# numlegs = 94
# chickens, rabbits = solve(numheads, numlegs)
# print("Number of chickens:", chickens)
# print("Number of rabbits:", rabbits)

#task 4

# def prime_numbers():
#     for i in range:
#         c = 0
#         for j in range(1, i):
#             if 1 % j == 0:
#                 c = c + 1
        
#             break
#         if c == 1:
#             pnum.append(i)
        
#         print(pnum)

# pnum = []

# def strPermut():
#     word = input()
#     perm = permutations(word)
#     for i in list(perm):
#         print(i)
# strPermut()

def wordRev():
    word = input()
    a = word.split()
    a = list(a)
    a.reverse()
    x = ' '.join(a)
    print(x)

wordRev()

