import math
import random
import numpy as np

def generator(samples=1000):
    random.seed(42)

    X = []
    Y = []

    for i in range(samples):
        
        rand = random.uniform(0, 4)
        if(rand == 0):
            random.uniform(0, 4)
        x = rand
        y = (math.sin(math.pi * x)) / (math.pi * x)
        
        X.append(x)
        Y.append(y)
    
    X = np.array(X)
    Y = np.array(Y)
    return  X, Y

