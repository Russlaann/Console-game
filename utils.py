import random as rn

def rand(x, y):
    rnx = rn.randint(0, x - 1)
    rny = rn.randint(0, y - 1)
    return rnx, rny

def rand_next():
    return rn.choice([(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)])

