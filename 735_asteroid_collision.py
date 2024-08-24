import math

def asteroidCollision(asteroids):
    final = []
    for x in range(0, len(asteroids)):
        while(True):                
            if(len(final) == 0):
                final.append(asteroids[x])
                break
            #same sign
            elif(math.copysign(1, final[-1]) == math.copysign(1, asteroids[x])):
                final.append(asteroids[x])
                break
            #opposite sign
            elif(math.copysign(1, final[-1]) != math.copysign(1, asteroids[x])):
                if(abs(final[-1]) == abs(asteroids[x])):
                    final.pop()
                    break
                elif(abs(final[-1]) < abs(asteroids[x])):
                    final.pop()
                else:
                    break
    return final


asteroids = [-2,-1,1,2]

print(asteroidCollision(asteroids))

