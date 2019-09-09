import random
def winProb(numTrails, winCond):
    myWin = youWin = 0
    for trail in range(numTrails):
        # I roll first, then you
        myNum = 0
        yourNum = 0

        while True:
            myNum = random.randint(1,6)
            if myNum == winCond:
                myWin += 1
                break
            yourNum = random.randint(1,6)
            if yourNum == winCond:
                youWin += 1
                break
            

    return myWin / numTrails, youWin / numTrails

print (winProb(100000, 4)) # the result is about 0.548 / 0.452; the exact answer would be 6/11
    
