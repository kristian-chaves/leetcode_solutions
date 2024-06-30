# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    occurances = {'B': 0, 'A': 0, 'N': 0}
    for char in S:
        if char in occurances:
            occurances[char] +=1
    moves = min(occurances['B'], occurances['A']//3, occurances['N']//2)
    return moves

#S = "NAABXXAN"
S = "QABAAAWOBL"
print(solution(S))