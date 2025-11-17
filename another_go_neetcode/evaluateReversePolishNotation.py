def function(tokens):
    operations = {'+', '-', '/', '*'}

    num1 = 0
    nums = []
    for x in tokens:
        if x in operations:
            if(x == '+'):
                nums.append(nums.pop() + nums.pop())
            elif(x == '-'):
                num1 = nums.pop()
                nums.append(nums.pop() - num1)
            elif(x == '*'):
                nums.append(nums.pop() * nums.pop())
            elif x == '/':
                num1 = nums.pop()
                nums.append(int(nums.pop() / num1))
        else:
            nums.append(int(x))
    return nums.pop()


#s = ["4","13","5","/","+"] # 6
#s = ["1","2","+","3","*","4","-"] # 5
s = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]  #22


print(function(s))