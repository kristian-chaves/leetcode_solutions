from collections import defaultdict

def function(s):
    dict = defaultdict(int)
    dict[')'] = '('
    dict['}'] = '{'
    dict[']'] = '['
    stack = []
    for x in s:
        stack.append(x)
        #need to implement chaining stacks - i think use a while loop of length big enough and previous != head
        while len(stack) > 1 and dict[stack[-1]] == stack[-2]:
            stack.pop()
            stack.pop()
    return len(stack) == 0


s = "([{}])"

print(function(s))