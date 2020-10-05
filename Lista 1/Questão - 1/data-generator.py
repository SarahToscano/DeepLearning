import random 
random.seed(1) #incializa semente para garantir que sempre sejam obtidos os mesmo conjuntos de dados

input_clean = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], 
               [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
max_ratio=0.1
samples = 50 #num de amostras de teste para cada tipo de entrada, linhas do arquivo de entrada = samples*8

count=0
column= len(input_clean[0]) #Tamanho dos dados de entrada a cada leitura
rown=len(input_clean)*samples
ruido=[0]*column #salva as informaçoes sobre ruido
file_input = open('./input_x.txt', 'w')
lista=[]
#Arquivo de entrada
for i in range (0, len(input_clean)):
    #print('Tipo de Entrada:', i)
    for j in range (0, samples): #Para cada tipo de dado ele cria um conjuto n com ruidos ou nao
        #print('  Amostra:', j)
        for k in range(0, column): #Analisa as posição de inserção do ruido randomicamente
            ruido[k]=random.randrange(0, 2) #0=sem ruido, 1=ruido
        #print(ruido)
        for k in range(0, column):
            if(ruido[k]==0): #sem ruido
                a=input_clean[i][k]
                file_input.write(str(a))
                lista.append(a)
            else:
                a=input_clean[i][k] + random.uniform(-max_ratio, max_ratio)
                file_input.write(str(a)) #insere o  ruido
                lista.append(a)
            if(k==2):
                file_input.write('\n')
            else:
                file_input.write(',')
        count+=1
        
file_input.close()

size_out= len(lista)
i=0; aux=0
code_bin = [0]*column
peso=[2,1,0]
out=[0]*8
file_output = open('./output_y.txt', 'w')

#Arquivo de saida
while(i< size_out):
    for j in range (0, column):
        if(lista[i]<=0.1): #Valores <=0.1 são equivalentes a 0
            code_bin[j]=0 
        else:
            code_bin[j]=1 #Valores >= 0.9 são equivalentes a 1
        i+=1
    for b in range(column-1,-1,-1): 
        aux+=code_bin[b]* (2 **peso[b]) #calcula numero decimal equivalente ao binario da saida
    out[aux]=1 #seta o bit para 1
    for k in range (0, 8):
        file_output.write(str(out[k])) #escreve todos os bits sem o '[' e ']'
        if(k!=7):
            file_output.write(',')
        else:
            file_output.write("\n")
    aux=0
    out=[0]*8 #zera o vetor de saida para ser reescrito

file_output.close()




