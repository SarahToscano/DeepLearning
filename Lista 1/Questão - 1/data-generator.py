import random 
random.seed(1) #incializa semente para garantir que sempre sejam obtidos os mesmo conjuntos de dados

input_clean = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], 
               [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
max_ratio=0.1
samples = 2 #define o numero de amostras de teste para cada tipo de entrada

column= len(input_clean[0]) #Tamanho dos dados de entrada a cada leitura
rown=len(input_clean)*samples
ruido=[0]*column #salva as informaçoes sobre ruido

file_input = open('./input_x.txt', 'w')

count=0

for i in range (0, len(input_clean)):
    print('Tipo de Entrada:', i)
    for j in range (0, samples):
        print('  Amostra:', j)
        for k in range(0, column): #Analisa as posição de inserção do ruido randomicamente
            ruido[k]=random.randrange(0, 2) #0=sem ruido, 1=ruido
        print(ruido)
        for k in range(0, column):
            if(ruido[k]==0): #sem ruido
                file_input.write(str(input_clean[i][k]))
            else:
                file_input.write(str(input_clean[i][k] + random.uniform(-max_ratio, max_ratio))) #insere o  ruido
            if(k==2):
                file_input.write('\n')
            else:
                file_input.write(',')
        count+=1
        
file_input.close()


classes = ["1,0,0,0,0,0,0,0", 
           "0,1,0,0,0,0,0,0", 
           "0,0,1,0,0,0,0,0", 
           "0,0,0,1,0,0,0,0",
           "0,0,0,0,1,0,0,0", 
           "0,0,0,0,0,1,0,0", 
           "0,0,0,0,0,0,1,0", 
           "0,0,0,0,0,0,0,1"]


