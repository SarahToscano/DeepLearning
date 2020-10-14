import math
import random
import numpy as np
random.seed(0) #incializa semente para garantir que sempre sejam obtidos os mesmo conjuntos de dados


samples=400
file_input = open('./input_x.txt', 'w')

for i in range(samples):
    x = random.uniform(0, 4)
    print(x)
    y = math.sin(math.pi * x) / (math.pi * x)
    file_input.write(str(y))
    if(i!=samples-1):
        file_input.write('\n')
