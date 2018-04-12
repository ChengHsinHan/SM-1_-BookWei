import random
import time
import math

def OneDieS(trials, sides):
    c1 = time.clock()
    mean_t = (1 + sides)/2
    vari_t = (math.pow(sides, 2) - 1)/12
    stde_t = math.sqrt(vari_t)
    print("====================")
    print("Number of sides = ", sides)
    print("Number of trials = ", trials)
    print("Theoretical: ")
    print("\t{:<20} = ".format("Mean value"), mean_t)
    print("\t{:<20} = ".format("Variance"), vari_t)
    print("\t{:<20} = ".format("Standard deviation"), stde_t)

    histogram = []
    for s in range(sides):
        histogram.append(0)

    r = 0
    total = 0
    temp = 0 # calculate total r^2
    for t in range(trials):
        r = int(random.random()*sides) + 1
        histogram[r - 1] = histogram[r - 1] + 1
        total += r
        temp += math.pow(r, 2)
    mean_s = total/trials
    vari_s = temp/trials - math.pow(mean_s, 2)
    stde_s = math.sqrt(vari_s)
    print("Statistical:")
    print("\t{:<20} = ".format("Mean value"), "{:<23}".format(mean_s), "(deviation = {:<23}({:>6}%))".format(mean_t - mean_s, round((mean_t - mean_s)/mean_t*100, 2)))
    print("\t{:<20} = ".format("Variance"), "{:<23}".format(vari_s), "(deviation = {:<23}({:>6}%))".format(vari_t - vari_s, round((vari_t - vari_s)/vari_t*100, 2)))
    print("\t{:<20} = ".format("Standard deviation"), "{:<23}".format(stde_s), "(deviation = {:<23}({:>6}%))".format(stde_t - stde_s, round((stde_t - stde_s)/stde_t*100, 2)))
    print(histogram)

    print("s\t{:<9}".format("N_s") + "{:<23}".format("N_s-N/sides") + "{:<23}".format("N_s/N") + "{}".format("N_s/N-1/sides"))
    for s in range(sides):
        print("{}\t{:<9}{:<23}{:<23}{}".format(s + 1, histogram[s], histogram[s] - trials/sides, histogram[s]/trials, histogram[s]/trials - 1/sides))

    c2 = time.clock()
    print("Elapsed time =", c2 - c1)

def run():
    OneDieS(1, 6)
    OneDieS(1, 12)
    OneDieS(10, 6)
    OneDieS(10, 12)
    OneDieS(100, 6)
    OneDieS(100, 12)
    OneDieS(1000, 6)
    OneDieS(1000, 12)
    OneDieS(5000, 6)
    OneDieS(5000, 12)
    OneDieS(10000, 6)
    OneDieS(10000, 12)
    OneDieS(100000, 6)
    OneDieS(100000, 12)
    OneDieS(1000000, 6)
    OneDieS(1000000, 12)

run()
