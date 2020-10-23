import math
import random
import numpy as np
random.seed(0) #incializa semente para garantir que sempre sejam obtidos os mesmo conjuntos de dados

k =5
back_step=[0]*k
future_step=[0]*3

file_input = open('./data_x.txt', 'w')
file_output = open('./data_y.txt', 'w')

for n in range (0,400):

    for i in range (1,k+1):
        back_step[i-1]= math.sin(n-i + pow(math.sin(n-i),2))
        file_input.write(str(back_step[i-1]))
        if(i!=k):
            file_input.write(', ')
        else:
            file_input.write('\n')
            
    for i in range(1,4):
        future_step[i-1]= math.sin(n+i + pow(math.sin(n+i),2) )
        file_output.write(str(future_step[i-1]))
        if(i!=3):
            file_output.write(', ')
        else:
            file_output.write('\n')
    print(n)

    back_step=[0]*k
    future_step=[0]*3

file_input.close()
file_output.close()