
def criar_matiz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            if j % 2 == 0:
                matriz[i].append(1)
            else:
                matriz[i].append(0)
    return matriz

linha = 5
coluna = 10

matriz = criar_matiz(linha,coluna)
for linha in matriz:
    print(linha)
