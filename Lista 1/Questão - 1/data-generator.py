'''
******************************
Criação do arquivo de entrada: 
******************************

    Objetivo: a partir do conjuto de dados do input_clean gerar múltiplas variações com a inserção ou não de ruído,
                neste caso o ruído é definido como sendo o max_ratio. Assim, podem ser subtraido ou adicionado ao input_clean
                um valor x tal que, -max_ratio <= x <=max_ratio. Nesse código para cada lista do input_clean são geradas samples
                variações.

    Metodologia: 1- Para cada elemento do inpuit_clean é decidido aleatoriamente a inserção de ruido. 0 sem ruido e 1 com ruido
                 2- Caso o dado não tenha ruido, ele é escrito no arquivo no seu formato original.
                 3- Caso contrário, é definido um random entre os limites do max_ratio para determinar o seu ruido
                 4- Em seguida ele é escrito no arquivo de saida.

'''

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


'''
*****************************
Criação do arquivo de saida: 
*****************************

    Objetivo: Para cada linha do arquivo de entrada, deve-se encontrar o seu binário de 8 bits BCD equivalente no "código anel"
    https://www.passeidireto.com/arquivo/33887484/sistemas-digitais-eletronica-digital-apostila

    Metodologia: 1- Analisa se o dado é equivalente a 1 ou 0 independete de ter ruido ou não.
                 2- Através da análise dos 3 bits lidos na etapa 1, sabe-se qual o equivalente do numero em decimal
                 3- Por fim, o número em decimal é transformado para o BCD código em anel em 8 bits e é escrito no arquivo de saida

'''

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