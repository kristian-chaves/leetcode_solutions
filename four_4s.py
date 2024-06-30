
#program to solve depth in 4 4s problem
# problem desc: use exactly four 4s, theoretically every dgit can be created
# because the Paul Bourke solution exists and makes every n > 0 trivial, log is a banned function
# permitted functions: addition, subtraction, div, multiplication, concatentation, sqrt, decimal point (.4), factorial, exponentiation

# note for future: i think this is going to be best represented using a hashtable - optimal solution involces storing individual actions for 1 and 2 operation values and then storing the value:operationCost in the dict

# single unit operations/constants
point4 = 0.4 # 1
sqrt4 = 2 # 1
four = 4 # 1
fact4 = 24 # 1

fourfour = 44

if __name__ == '__main__':
    breakpoint = 20 # using breakpoint instead of for loop to have more flexible break conditions
    x = 0
    while True:
        #perform recurring operations until sol arrived at, print sol
        print(f'{x}: qqqq')