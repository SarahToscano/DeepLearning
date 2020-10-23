import math
import random
import numpy as np
random.seed(0) #incializa semente para garantir que sempre sejam obtidos os mesmo conjuntos de dados

samples=100
file_input = open('./data/data_x_a.txt', 'w')
file_output = open('./data/data_y_a.txt', 'w')

for i in range(samples):
    x = random.randint(0, 3)
    
    if(x == 0):
        file_input.write(str("0,0"))
        file_output.write(str("0"))
    
    if(x == 1):
        file_input.write(str("0,1"))
        file_output.write(str("1"))
    
    if(x == 2):
        file_input.write(str("1,0"))
        file_output.write(str("1"))
    
    if(x == 3):
        file_input.write(str("1,1"))
        file_output.write(str("0"))
    
    file_input.write('\n')
    file_output.write('\n')

file_input.close()
file_output.close()