'''
#1)	Faça uma função que recebe uma matriz como parâmetro e a printa
#elemento a elemento.(1 ponto)
def printa_elementos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"matriz[{i}][{j}] = {matriz[i][j]}")
    return

#2)	Faça uma função que recebe uma matriz como parâmetro e printa linha a linha,
#forma que estamos mais acostumado a ver uma matriz.(1 ponto)

def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return


#3)	Faça uma função que recebe o número de linhas e colunas como parâmetros e cria
#uma matriz de dimensões linhas x colunas contendo somente zeros (2 pontos)

def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(0)
    return matriz

#matriz = cria_matriz(3,4)
#mostra_matriz(matriz)
#printa_elementos(matriz)

#4)	Crie uma matriz 8x8 contendo o padrão de um tabuleiro de xadrez (2 pontos).
#Explique em um comentário no código seu raciocínio.(2 pontos)

xadrez = cria_matriz(8,8)
for i in range(len(xadrez)):
    for j in range(len(xadrez[0])):
        if i%2:
            if j%2:
                xadrez[i][j] = 0
            else:
                xadrez[i][j] = 1
        else:
            if j%2:
                xadrez[i][j] = 1
            else:
                xadrez[i][j] = 0
#mostra_matriz(xadrez)

#num tabuleirode xadrez deve-se alternar as cores branco e preto a cada linha, porém
#linhas consecutivas devem ter o padrão de cor defasado, por exemplo:
#0 1 0 1
#1 0 1 0
#assim percebemos que o padrão de alternancia das cores deve iniciar com 0 em linhas
# pares e manter 0 nas colunas pares.
#o contrário deve acontecer nas linhas ímpares, ou seja, linhas impares e colunas pares
#devem ter 1, linhas impares colunas impares, 0

from time import time
def matriz_distancia(lista_x,lista_y):
    distancias = cria_matriz(len(x),len(x))
    for i in range(len(lista_x)):
        for j in range(i):
            dist_ij = round(((lista_x[i] - lista_x[j])**2 + (lista_y[i]-lista_y[j])**2)**0.5)
            distancias[i][j] = dist_ij
            distancias[j][i] = dist_ij
    return distancias


def matriz_distancia_lento(lista_x,lista_y):
    distancias = cria_matriz(len(x),len(x))
    for i in range(len(lista_x)):
        for j in range(len(lista_x)):
            dist_ij = round(((lista_x[i] - lista_x[j])**2 + (lista_y[i]-lista_y[j])**2)**0.5)
            distancias[i][j] = dist_ij
            #distancias[j][i] = dist_ij
    return distancias

x = [i for i in range(10000)]
y = [i for i in range(10000,0,-1)]
t1 = time()
matriz_dist = matriz_distancia(x,y)
t2 = time()
print(t2-t1)
#mostra_matriz(matriz_dist)

t1 = time()
matriz_dist = matriz_distancia_lento(x,y)
t2 = time()
print(t2-t1)
'''




whiskeys = {
    'tipo' : ['bourbon','blended','scotch','single malt','double malt'],
    '%alcoolico' : [41,50,35,62,37],
    'volume (ml)' : [1000,750,50,100,2000],
    'idade' : [15,12,8,8,10],
    'preço' : [14,23,541,65,999],
    'marca' : ['Jack Daniels','White Horse','Passport','Johnnie Walker','Chanceler']
}
print(pd.DataFrame(whiskeys))
def forca_opcao(msg,lista_opcoes):
    resposta = input(msg)
    while resposta not in lista_opcoes:
        print("Digite uma opção cadastrada!")
        resposta = input(msg)
    return resposta
#pergunte ao usuário se ele é cliente ou funcionário
#se for cliente, de as opções de vinhos da casa e pergunte seu endereço
#pergunte informações a respeito de qual ele quer ver
#pergunte se ele vai comprar o vinho escolhido no item anterior
#caso queira, adicione ao carrinho dele o vinho e seu preço
compra = {
    'valor total' : 0,
    'garrafas' : {},
    'endereco' : {
        'rua' : '',
        'numero': '',
        'cep' : '',
        'bairro' : '',
        'cidade' :''
    },
    'nome' : ''
}
cliente_ou_funcionario = forca_opcao(f"Voce é cliente ou funcionário ? (c/f) ",['c','f'])

if cliente_ou_funcionario == 'c':
    nome = input("Diga seu nome : ")
    compra['nome'] = nome
    for key in compra['endereco'].keys():
        info = input(f"Diga seu/a {key} : ")
        compra['endereco'][key] = info
    print(f"Seja bem vindo/a {nome}!")
    while True:
        print("Essas são nossas opções de whiskeys:")
        for i in range(len(whiskeys['marca'])):
            print(f"{i} : {whiskeys['marca'][i]}")
        opcao = int(forca_opcao("Por qual voce mais se interessou ? ",['0','1','2','3','4']))
        print("Essas são as informações sobre o whiskey escolhido:")
        for key in whiskeys.keys():
            print(f"{key} : {whiskeys[key][opcao]}")
        comprar = forca_opcao("Voce vai levar ? (s/n)",['s','n'])
        if comprar == 's':
            compra['valor total'] += whiskeys['preço'][opcao]
            marca = whiskeys['marca'][opcao]
            if marca not in compra['garrafas']:
                compra['garrafas'][marca] = 1
            else:
                compra['garrafas'][marca] +=1
        continuar = forca_opcao('Você quer comprar mais whikeys ? (s/n) ',['s','n'])
        if continuar == 'n':
            print("Resumo do seu pedido : ")
            for key in compra.keys():
                if type(compra[key]) is dict:
                    for key2 in compra[key].keys():
                        print(f"{key2} : {compra[key][key2]}")
                else:
                    print(f"{key} : {compra[key]}")

            break

