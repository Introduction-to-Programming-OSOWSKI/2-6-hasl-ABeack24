#WRITE YOUR CODE IN THIS FILE
def hasL(x):
    numL = 0
    for i in range (0, len(x)):
        if x[i] == "l":
            numL = numL + 1
            if numL >= 1:
             return True
            else:
                return False

print(hasL("alabama"))