def canPlaceFlowers(flowerbed, n):
    streak = 1
    wins = 0
    for x in flowerbed:
        if(x == 1):
            streak = 0
        else:
            streak += 1
            if(streak == 3):
                wins += 1
                streak -= 2
    if(streak == 2):
        wins+=1
    return wins >= n;


flowerbed = [1,0,0,0,0,1]
n = 2

print(canPlaceFlowers(flowerbed, n))