def minStairCost(cost):
    cost.append(0)
    index = len(cost) - 3
    while (index > -1):
        cost[index] += min(cost[index + 2], cost[index + 1])
        index -= 1

    return min(cost[0], cost[1])


cost = [0,2,2,1]


print(minStairCost(cost))