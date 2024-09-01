import math

def asteroidCollision(asteroids):
    final = []
    for x in asteroids:
        while final and x < 0 and final[-1] > 0: 
            diff = x + final[-1]
            if(diff < 0):
                final.pop()
            elif diff > 0:
                x = 0
            else:
                x = 0
                final.pop()
        if x:
            final.append(x)
    return final


#asteroids = [-2,-1,1,2]
asteroids = [5,10,-5]
#asteroids = [8,-8]

print(asteroidCollision(asteroids))

