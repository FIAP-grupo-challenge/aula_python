import requests

def get_ficha_tecnica(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url).json()
    return response


def printar_ficha_tecnica(pokemon):
    ficha_tecnica = get_ficha_tecnica(pokemon)
    for linha in ficha_tecnica:
        print(f"{linha} : {ficha_tecnica[linha]}")


def printar_abilidades(pokemon):
    ficha_tecnica = get_ficha_tecnica(pokemon)
    print(ficha_tecnica["abilities"])

printar_abilidades("pikachu")


