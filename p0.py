import random
import time

def OneDie(trials):
    c1=time.clock()
    print("====================")
    print("One die with 6 sides")
    print("Number of trials = ", trials)

    sides = 6
    histogram = [0, 0, 0, 0, 0, 0]
    print(histogram)

    j = 0
    r = 0
    while j < trials :
        r = int(random.random()*sides) # Faster
#         r = random.randint(0,5) # Slower. Return random integer in range [a, b], including both end points.
        histogram[r] = histogram[r] + 1
        j = j + 1

    print("s, N_s, N_s-N/6, N_s/N, N_s/N-1/6")
    j = 0
    while j < sides:
        print(j+1, histogram[j], histogram[j]-trials/sides, histogram[j]/trials, histogram[j]/trials-1/6)
        j = j + 1

    c2=time.clock()
    print("Elapsed time =", c2-c1)

def run():
    OneDie(2)
    OneDie(20)
    OneDie(200)
    OneDie(2000)
    OneDie(20000)
    OneDie(200000)
    OneDie(2000000)
run()
