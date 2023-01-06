import random

def coin_toss() :
    result = random.randint(0, 1)

    if (result == 0) :
        print("\nHeads.\n")
    else :
        print("\nTails.\n")