carross = {"celta" : 10000, "HB20" : 20000, "Renegade" : 1000000}

def achar_carro_mais_caro(carros):
    carro_mais_caro = ""
    valor_do_mais_caro = 0
    for carro in carros:
        if carros[carro] >= valor_do_mais_caro:
            carro_mais_caro = carro
            valor_do_mais_caro = carros[carro]
    return carro_mais_caro

print(achar_carro_mais_caro(carross))
