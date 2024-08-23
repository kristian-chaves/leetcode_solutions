def tribonacciNum(n):
    q = [0, 1, 1]
    for x in range(3, n+1):
        q[x % 3] = sum(q)
    return q[n % 3]


n = 3


print(tribonacciNum(n))