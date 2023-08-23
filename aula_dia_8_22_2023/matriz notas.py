notas = [[10, 7, 8, 5, 3], [7, 3, 4, 9, 8], [10, 7, 8, 10, 9], [10, 7, 8, 9, 10], [10, 7, 8, 5, 6]]
pesos = [1, 2, 3, 4, 1]


def calcular_notas(notas_, pesos_):
    resultados = []
    for i in range(len(notas_)):
        resultados.append([])
        for j in range(len(notas_[0])):
            resultados[i].append(notas_[i][j] * pesos_[i])
    return resultados


def mostrar_matriz(matriz):
    for linha in matriz:
        print(linha)

def calcular_nota_final(resultados_):
    notas_ = []
    for i in range(len(resultados_[0])):
        notas_.append(0)
    for i in range(len(resultados_)):
        for j in range(len(resultados_[0])):
            notas_[j] = notas_[j] + resultados_[i][j]
    for i in range(len(notas_)):
        notas_[i] = notas_[i] / 11
    return notas_

resultado = calcular_notas(notas,pesos)
final = calcular_nota_final(resultado)
print("\nNotas: ")
mostrar_matriz(notas)
print("\nResultados: ")
mostrar_matriz(resultado)
print("\nFinal: ")
print(final)
